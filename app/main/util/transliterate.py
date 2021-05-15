ukr2eng = {
    'а': 'ah',
    'б': 'b',
    'в': 'v',
    'г': 'h',
    'ґ': 'g',
    'д': 'd',
    'е': 'eh',
    'э': 'eh',
    'є': 'jeh',
    'ж': 'zh',
    'з': 'z',
    'и': 'ih',
    'ы': 'ih',
    'і': 'ee',
    'ї': 'yee',
    'й': 'y',
    'к': 'k',
    'л': 'l',
    'м': 'm',
    'н': 'n',
    'о': 'o',
    'п': 'p',
    'р': 'r',
    'с': 's',
    'т': 't',
    'у': 'oo',
    'ф': 'f',
    'х': 'kh',
    'ц': 'ts',
    'ч': 'ch',
    'ш': 'sh',
    'щ': 'shch',
    'ь': 'j',
    'ю': 'joo',
    'я': 'jah'
}


def translit(text):
  text = text.replace('ьо', 'jyo')
  text = text.replace('—', '-')
  text = text.replace('“', '')
  text = text.replace('”', '')

  if '\'є' in text:
    text = text.replace('\'є', 'yeh')
  if '\'я' in text:
    text = text.replace('\'я', 'ya')
  if '\'ю' in text:
    text = text.replace('\'ю', 'yu')

  if 'ьє' in text:
    text = text.replace('ьє', 'jyeh')
  if 'ья' in text:
    text = text.replace('ья', 'jya')
  if 'ью' in text:
    text = text.replace('ью', 'jyu')

  if text[0] == 'є':
    text = text.replace('\'є', 'yeh')
  if text[0] == 'я':
    text = text.replace('\'я', 'ya')
  if text[0] == 'ї':
    text = text.replace('\'ю', 'yu')

  result = [''] * len(text)
  for i, letter in enumerate(text.lower()):
    if letter == 'є' and text[i - 1] in ['а', 'е', 'и', 'і', 'ї', 'я', 'у', 'ю', 'є', 'о']:
      result[i] = 'yeh'
    elif letter == 'я' and text[i - 1] in ['а', 'е', 'и', 'і', 'ї', 'я', 'у', 'ю', 'є', 'о']:
      result[i] = 'ya'
    elif letter == 'ю' and text[i - 1] in ['а', 'е', 'и', 'і', 'ї', 'я', 'у', 'ю', 'є', 'о']:
      result[i] = 'yu'
    elif letter in list(ukr2eng.keys()):
      result[i] = ukr2eng.get(letter)
    else:
      result[i] = letter
  
  return ''.join(result)
