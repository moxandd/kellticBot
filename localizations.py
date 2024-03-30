
localizations = {
    "ru": {
        "Hello! Please, choose your language :)": "Привет! Пожалуйста, выбери свой язык :)",
        "Succesfully! Using English now": "Успешно! Теперь говорим по-русски"
    }
}

def translate(sentence, language='en'):
    if language == 'en':
        return sentence
    try:
        return localizations[language][sentence]
    except:
        raise Exception("Unable to translate...")
    