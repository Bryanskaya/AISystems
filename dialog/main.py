import re

from commands import *
from data import conDict
from prepareData import initPrefer, resetPrefer
from preprocessing import preprocessing, updateCon, updateDurability
from rules import *


def _getAnswer():
    while True:
        answer = input().lower()
        if answer == "да":
            return True
        elif answer == "нет":
            return False

        cmdYesNoValidation()


def isFound():
    cmdWasFound()
    return _getAnswer()


def isAdd():
    cmdAddDefinition()
    return _getAnswer()


def isReset():
    cmdResetDefinition()
    return _getAnswer()


def processDefinition(dictPrefer, data):
    f = 0
    for rule in RULE_ARR:
        regexp = re.compile(rule)
        match = regexp.match(data)
        if match is not None:
            resDict = match.groupdict()

            if rule == NOT_SIMILAR_TO_BRAND or rule == I_DISLIKE_BRAND:
                dictPrefer["dislikes"].append(resDict["similar_name"])
            elif rule == SIMILAR_TO_BRAND or rule == I_LIKE_BRAND:
                dictPrefer["likes"].append(resDict["similar_name"])
            elif rule == WANT_ABSTRACT_OBJ:
                dictPrefer["smell"].append(resDict["obj"])
            elif rule == WANT_ABSTRACT_OBJ_KINDPARFUM:
                dictPrefer["smell"].append(resDict["obj"])

                if resDict["kind_parfum"] is not None:
                    dictPrefer["consentration"].append(updateCon(resDict["kind_parfum"]))
            elif rule == WANT_ABSTRACT:
                dictPrefer["smell"].append(resDict["tag1"])
            elif rule == WHAT_EXISTS_KINDPARFUM:
                dictPrefer["consentration"].append(updateCon(resDict["kind_parfum"]))
            elif rule == I_LIKE_TAG:
                dictPrefer["smell"].append(resDict["tag1"])
            elif rule == I_LIKE_OBJ:
                dictPrefer["smell"].append(resDict["obj"])
            elif rule == COUNTRY_EXT_KINDPARFUM_1 or rule == COUNTRY_EXT_KINDPARFUM_2:
                if resDict["country"] is not None:
                    dictPrefer["country"].append(resDict["country"])
                if resDict["country_ext"] is not None:
                    dictPrefer["country"].append(resDict["country_ext"])

                dictPrefer["consentration"].append(updateCon(resDict["kind_parfum"]))
            elif rule == COUNTRY_EXT:
                if resDict["country"] is not None:
                    dictPrefer["country"].append(resDict["country"])
                if resDict["country_ext"] is not None:
                    dictPrefer["country"].append(resDict["country_ext"])
            elif rule == SHOW_DURABILITY:
                dictPrefer["durability"].append(updateDurability(resDict["durability"]))

            f = 1
            break

    if f == 0:
        cmdMissunderstanding()
    cmdFind(dictPrefer)


def dialog():
    dictPrefer = initPrefer()

    while True:
        cmdDescribe()
        data = input()
        dataProcessed = preprocessing(data)
        processDefinition(dictPrefer, dataProcessed)

        while True:
            if isFound():
                cmdGoodBye()
                return
            elif isAdd():
                break
            elif isReset():
                resetPrefer(dictPrefer)
                cmdResetDefinitionComplete()
                break


def main():
    cmdWelcome()
    dialog()


if __name__ == "__main__":
    main()
