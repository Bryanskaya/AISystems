from data import df0
from params import *
from prepareData import find


def cmdOffer():
    print(DEFAULT_DATA)


def cmdWelcome():
    print(WELCOME_PHRASE)


def cmdGoodBye():
    print(GOODBYE_PHRASE)


def cmdDescribe():
    print(DESCRIBE)


def cmdDefault():
    cmdOffer()
    print(df0.loc[1:5, ["название", "пол", "бренд", "страна", "сегмент"]])
    print()


def cmdWasFound():
    print(FOUND_QUESTION)


def cmdYesNoValidation():
    print(YES_NO)


def cmdAddDefinition():
    print(ADD_DEFINITION)


def cmdResetDefinition():
    print(RESET_PHRASE)


def cmdResetDefinitionComplete():
    print(RESET_PHRASE_COMPLETE)


def cmdMissunderstanding():
    print(MISUNDERSTANDING)


def cmdGiveMustRecomendation():
    print(MUST_LIKE)


def cmdGiveMayRecomendation():
    print(MAY_LIKE)


def _printRecomendations(recArr):
    iArr = []
    n = min(len(recArr), 5)
    for i in range(n):
        iArr.append(df0.index[df0["название"] == recArr[i]].tolist()[0])
    print(df0.loc[iArr, ["название", "пол", "бренд", "страна", "сегмент"]])


def cmdFind(dictPrefer):
    recMust, recMaybe = find(dictPrefer)

    if len(recMust):
        cmdGiveMustRecomendation()
        _printRecomendations(recMust)

    if len(recMaybe):
        cmdGiveMayRecomendation()
        _printRecomendations(recMaybe)
