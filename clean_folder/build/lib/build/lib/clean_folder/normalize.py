import re

UKRAINIAN_SYMBOLS = 'абвгдеєжзиіїйклмнопрстуфхцчшщьюя'
TRANSLATION = ("a", "b", "v", "g", "d", "e", "je", "zh", "z", "y", "i", "ji", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "ju", "ja")
TRANS = {}
#Data for translation

for ukr_symbol, trans_symbol in zip(UKRAINIAN_SYMBOLS, TRANSLATION):
    TRANS[ord(ukr_symbol)] = trans_symbol
    TRANS[ord(ukr_symbol.upper())] = trans_symbol.upper()
#Transliteration of symbols was created

def normalize(file_name):
    translated_name = file_name.translate(TRANS)
    if '.' in file_name:
        name, *extension = translated_name.split('.')
        new_extensions = ''
        for i in extension[:-1]:
            new_extension = re.sub(r'\W', '_', i)
            new_extensions += '_' + new_extension
        new_name = re.sub(r'\W', '_', name)
        return f'{new_name}{new_extensions}.{extension[-1]}'
    else:
        return ''
#Function for transliteration and replacement of all symbols except for Latin letters, !!!dot for extension!!!
#(other dots are replaced) and numbers with '_'

# print(normalize('П.\ри-*в.8іт.py.txt'))