import tempfile
import numpy as np

from flask import current_app
from scipy.io.wavfile import write

from app.main import synthesizer
from app.main import vocoder
from app.main import client

from app.main.util.transliterate import translit
from app.main.util.tacotron.model import Synthesizer
from app.main.util.vocoder.vocoder import infer_waveform


def voice_text(voice_id, query_id, text):
    embed = None

    with tempfile.TemporaryFile(mode='w+b') as f:
        client.download_fileobj(
            current_app.config['BUCKET_NAME'], 
            f'{voice_id}.npy', 
            f
        )
        f.seek(0)
        embed = np.load(f, allow_pickle=True)
    
    texts = [translit(t) for t in text.split("\n")]

    embeds = np.stack([embed] * len(texts))

    specs = synthesizer.synthesize_spectrograms(texts, embeds)
    breaks = [spec.shape[1] for spec in specs]
    spec = np.concatenate(specs, axis=1)

    wav = infer_waveform(vocoder, spec)

    b_ends = np.cumsum(np.array(breaks) * Synthesizer.hparams.hop_size)
    b_starts = np.concatenate(([0], b_ends[:-1]))
    wavs = [wav[start:end] for start, end, in zip(b_starts, b_ends)]
    breaks = [np.zeros(int(0.15 * Synthesizer.sample_rate))] * len(breaks)
    wav = np.concatenate([i for w, b in zip(wavs, breaks) for i in (w, b)])

    wav = wav / np.abs(wav).max() * 0.97

    result = tempfile.TemporaryFile()
    write(result, Synthesizer.sample_rate, wav)
    result.seek(0)
    client.upload_fileobj(result, current_app.config['BUCKET_NAME'], f'{query_id}.wav')

    return {
        'status': 'success',
        'message': 'Text was voiced'
    }, 200
