import re
import pymorphy2
from nltk.tokenize import word_tokenize

morph = pymorphy2.MorphAnalyzer()


def getNormalFormWord(word):
    return morph.parse(word)[0].normal_form


def delUselessSigns(phrase):
    return re.sub("[^а-яa-z0-9'№ -]", "", phrase)


def getNormalFormPhrase(phrase):
    wordArr = word_tokenize(phrase, language="russian")
    return ' '.join(getNormalFormWord(word) for word in wordArr)


def toLower(phrase):
    return phrase.lower()


def preprocessing(phrase):
    phrase = toLower(phrase)
    phrase = delUselessSigns(phrase)
    return getNormalFormPhrase(phrase)


def updateCon(input):
    dict = {"освежать вода": 0, "одеколон": 0.2, "туалетный вода": 0.4,
            "парфюмерный вода": 0.6, "дух": 0.8, "масляный дух": 1}
    return dict[input]


def updateDurability(input):
    dict  = {"средний": 0.16666666666666666, "очень высокий": 1.0, "высокий": 0.4166666666666667}
    return dict[input]


