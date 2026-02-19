import pycountry

def get_language_list():
    languages = sorted([lang.name for lang in pycountry.languages if hasattr(lang, 'name')])
    languages.insert(0, "Auto")
    return languages
