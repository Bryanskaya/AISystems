from data import namesUI, giveRecommendationFull, df


def initPrefer():
    return {"likes": [], "dislikes": [], "consentration": [],
            "smell": [], "country": [], "durability": []}


def resetPrefer(dictPrefer):
    for key in dictPrefer.keys():
        dictPrefer[key] = []
    return dictPrefer


def _replaceBrand(inputArr):
    brandArr = []
    brandUI = {}
    for i in range(len(namesUI)):
        brandUI[namesUI[i].lower()] = i

    for brand in inputArr:
        curName = brand.lower()
        if curName in brandUI.keys():
            brandArr.append(namesUI[brandUI[curName]])
    return brandArr


def _replaceCountry(inputArr):
    countryArr = []
    countryDict = {"россия": "Россия", "франция": "Франция", "оаэ": "ОАЭ",
                   "сша": "США", "италия": "Италия", "германия": "Германия",
                   "итальянский": "Италия", "российский": "Россия", "немецкий": "Германия",
                   "германский": "Германия", "французский": "Франция", "арабский": "ОАЭ",
                   "американский": "США"}
    for country in inputArr:
        curCountry = country.lower()
        if curCountry in countryDict.keys():
            countryArr.append(countryDict[curCountry])
    return countryArr


def find(paramDict):
    paramDict["likes"] = _replaceBrand(paramDict["likes"])
    paramDict["dislikes"] = _replaceBrand(paramDict["dislikes"])
    paramDict["country"] = _replaceCountry(paramDict["country"])
    return giveRecommendationFull([], paramDict["country"], [],
                           paramDict["consentration"], [], paramDict["smell"],
                           paramDict["likes"], paramDict["dislikes"], paramDict["durability"], df)
