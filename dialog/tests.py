import re

from preprocessing import preprocessing
from rules import *

userInputDict = {
    'что можете предложить?': WHAT_EXISTS,
    'что есть в наличие': WHAT_EXISTS,
    'что у вас есть в наличие': WHAT_EXISTS,
    'что у вас есть': WHAT_EXISTS,
    'какой у вас есть парфюм в наличии?': WHAT_EXISTS,
    'какой у вас парфюм есть в наличии?': WHAT_EXISTS,
    'какой у вас есть парфюм?': WHAT_EXISTS,

    'какие у вас есть духи?': WHAT_EXISTS_KINDPARFUM,
    'что есть из туалетной воды': WHAT_EXISTS_KINDPARFUM,

    'я не совсем знаю, что надо': SHOW_ANY,
    'помогите мне, пожалуйста, я совсем ничего не знаю': SHOW_ANY,

    'хочется свежий аромат': WANT_ABSTRACT,
    'хочу свежую парфюмерную воду': WANT_ABSTRACT,
    'мне очень нужен сладкий запах': WANT_ABSTRACT,
    'есть свежий масляные духи?': WANT_ABSTRACT,

    #'ищу бодрящий, но не морской': WANT_ABSTRACT_NOT,
    #'ищу свежие духи, но не морские': WANT_ABSTRACT_NOT_KINDPARFUM,

    'хочется чего-то с запахом бергамота': WANT_ABSTRACT_OBJ,
    'хочу аромат, который пахнет густым дымом': WANT_ABSTRACT_OBJ_KINDPARFUM,

    'мне нравится томный аромат': I_LIKE_TAG,
    'обожаю лаванда': I_LIKE_OBJ,
    #'я не люблю сливочные ноты': I_DISLIKE_TAG,
    #'моя мама не переносит лайм': I_DISLIKE_OBJ,

    'нужен аромат похожий на 1001 Nights': SIMILAR_TO_BRAND,
    'хочу купить аналог парфюма Sabina': SIMILAR_TO_BRAND,

    'нужен аромат не похожий на 1001 Nights': NOT_SIMILAR_TO_BRAND,

    'мне очень нравятся французские духи': COUNTRY_EXT_KINDPARFUM_1,
    'я бы хотела купить туалетную воду из Германии': COUNTRY_EXT_KINDPARFUM_2,

    'хочу купить арабский аромат': COUNTRY_EXT,

    'хочу аромат средней стойкости': SHOW_DURABILITY,
    'нужны духи очень высокой стойкости': SHOW_DURABILITY,
    'а есть что-нибудь высокой стойкости': SHOW_DURABILITY
}


def run():
    for userInput, ruleRes in userInputDict.items():
        userProcessed = preprocessing(userInput)
        print(">>> ", userProcessed)

        for rule in RULE_ARR:
            regexp = re.compile(rule)
            match = regexp.match(userProcessed)
            if match != None:
                res = match.groupdict()
                print('MATCHED: ', rule == ruleRes)
                print('RULE: ', rule)
                print('RESULT: {}\n'.format(res))


if __name__ == "__main__":
    run()