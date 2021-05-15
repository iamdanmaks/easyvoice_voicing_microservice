import boto3
import pathlib
import os

from flask import Flask

from app.main.util.tacotron.model import Synthesizer
from app.main.util.vocoder.vocoder import load_model

from .config import config_by_name, Config


os.environ["CUDA_VISIBLE_DEVICES"] = ""

synthesizer = Synthesizer(
    pathlib.Path('./app/main/util/weights/tacotron'), 
    low_mem=True,
    seed=Config.SEED
)
vocoder = load_model('./app/main/util/weights/vocoder/pretrained.pt')

client = boto3.client(
        's3',
        aws_access_key_id=Config.AWS_ACCESS_KEY_ID, 
        aws_secret_access_key=Config.AWS_SECRET_ACCESS_KEY
    )

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])

    return app
