HELP = r'(?P<help>(посоветовать|помочь|предложить|подсказать|показать|порекомендовать|посмотреть|ознакомиться))'
NOT_KNOW_GENERAL = r'(?P<not_know_general>(не.*знать).*(хотеть|надо))'

GENERAL_QUESTION = r'(?P<general_question>(что|какой))'
KIND_PARFUM = r'(?P<kind_parfum>(дух|туалетный вода|парфюмерный вода|масляный дух))'
EXIST = r'(?P<exist>(есть|в наличие|в продажа|купить|мочь|предложить|представить))'

WANT = r'(?P<want>(хотеться|хотеть|нужно|нужный|надо|искать|есть))'
TAG = r'((повседневный|свежий|спортивный|сладкий|чистый|праздничный|нежный|женственный|стойкий|плотный|насыщенный|чувственный|томный|тяжёлый|интенсивный|сухой|роскошный|тёплый|сливочный|таинственный|лёгкий|бодрящий|энергичный|тонизировать|яркий|необычный|тонкий|ненавязчивый|морской|спокойный|активный|острый|массивный|терпкий|пряно-горький|мягкий|пряный|древесный|притягательный))'
OBJ = r'(?P<obj>(шоколад|карамель|дым|благовоние|смола|ладан|табак|мускус|ваниль|кофе|чёрный чай|роза|сандал|мох|земля|металл|кедр|апельсин|лайм|грейпфрут|лимон|бергамот|виноград|персик|горный воздух|морозный свежесть|огурец|яблоко|белый чай|зелёный чай|перец|корица|гвоздик|куркума|имбирь|орех|лаванда|герань|трава|лист|арбуз|лилия|сахар|специя|бумага))'
KIND_PARFUM_ADD = r'(?P<kind_parfum_add>(запах|аромат|парфюм))'
KIND_PARFUM_EXT = r'({}|{})'.format(KIND_PARFUM, KIND_PARFUM_ADD)
GENERAL_EXT = r'({}|{})'.format(GENERAL_QUESTION, WANT)

LIKE = r'(?P<like>(нравиться|обожать|любить))'
DISLIKE = r'(?P<dislike>(не переносить|не нравиться|не подходить|не любить|терпеть не мочь|ненавидеть))'

NOT = r'(?P<not>(но не|а не))'
SMELL_AS = r'(?P<smell_as>(с запах|пахнуть))'

SIMILAR_TO = r'(?P<similar_to>(похожий|на подобие|аналог|тип))'
NOT_SIMILAT_TO = r'(?P<not_similar_to>(не похожий|отличный от))'
NAME = r'(?P<similar_name>(shalimar|3 l\'imperatrice|1001 nights|sabina|resolute gold|oath for him|twist|ck everyone|bad boy|eau de lacoste|l.12.12 blanc|ange ou demon|samsara eau de parfum|new your amber|renata|lanvin eclat d arpege|moschino toy boy|cartier declaration d un soi|channel №5|prada day for night|escentric molecules escentric 02|the only one|flora by gucci|gorgeous gardenia|la petite robe noire ma robe cocktail|la petite robe noire ma robe sous le vent))'
DISLIKE_EXT = r'({}|{})'.format(DISLIKE, NOT_SIMILAT_TO)

COUNTRY = r'(?P<country>(италия|франция|оаэ|сша|россия|германия))'
COUNTRY_ADD = r'(?P<country_ext>(итальянский|российский|немецкий|германский|французский|арабский|американский))'
COUNTRY_EXT = r'.*({}|{}).*'.format(COUNTRY, COUNTRY_ADD)
COUNTRY_EXT_KINDPARFUM_1 = r'.*{}.*{}.*'.format(COUNTRY_EXT, KIND_PARFUM)
COUNTRY_EXT_KINDPARFUM_2 = r'.*{}.*{}.*'.format(KIND_PARFUM, COUNTRY_EXT)

SHOW_ANY = r'.*({}|{}).*'.format(HELP, NOT_KNOW_GENERAL)

DURABILITY = r'(?P<durability>(средний|высокий|очень высокий))'
SHOW_DURABILITY = r'.*{} стойкость.*'.format(DURABILITY)

WHAT_EXISTS = r'.*{}.*{}.*'.format(GENERAL_QUESTION, EXIST)
WHAT_EXISTS_KINDPARFUM = r'.*{}.*{}.*'.format(GENERAL_EXT, KIND_PARFUM)

WANT_ABSTRACT = r'.*{}.*(?P<tag1>{}).*{}.*'.format(WANT, TAG, KIND_PARFUM_EXT)
#WANT_ABSTRACT_NOT = r'.*{}.*(?P<tag1>{}) {} (?P<tag2>{})'.format(WANT, TAG, NOT, TAG)
#WANT_ABSTRACT_NOT_KINDPARFUM = r'.*{}.*(?P<tag1>{}).*{} {} (?P<tag2>{})'.format(WANT, TAG, KIND_PARFUM_EXT, NOT, TAG)

WANT_ABSTRACT_OBJ = r'.*{}.*{}.*{}.*'.format(WANT, SMELL_AS, OBJ)
WANT_ABSTRACT_OBJ_KINDPARFUM = r'.*{}.*{}.*{}.*{}.*'.format(WANT, KIND_PARFUM_EXT, SMELL_AS, OBJ)

I_LIKE_TAG = r'.*{} (?P<tag1>{}).*'.format(LIKE, TAG)
I_LIKE_OBJ = r'.*{} {}.*'.format(LIKE, OBJ)
I_LIKE_BRAND = r'.*{} {}.*'.format(LIKE, NAME)
#I_DISLIKE_TAG = r'.*{} (?P<tag1>{}).*'.format(DISLIKE, TAG)
#I_DISLIKE_OBJ = r'.*{} {}.*'.format(DISLIKE, OBJ)
I_DISLIKE_BRAND = r'.*{} {}.*'.format(DISLIKE, NAME)

SIMILAR_TO_BRAND = r'.*{}.*{}.*'.format(SIMILAR_TO, NAME)
NOT_SIMILAR_TO_BRAND = r'.*{}.*{}.*'.format(DISLIKE_EXT, NAME)

RULE_ARR = [NOT_SIMILAR_TO_BRAND,
            SIMILAR_TO_BRAND,
            WANT_ABSTRACT_OBJ_KINDPARFUM,
            WANT_ABSTRACT_OBJ,
            #WANT_ABSTRACT_NOT_KINDPARFUM,
            #WANT_ABSTRACT_NOT,
            COUNTRY_EXT_KINDPARFUM_1,
            COUNTRY_EXT_KINDPARFUM_2,
            SHOW_DURABILITY,
            WANT_ABSTRACT,
            WHAT_EXISTS_KINDPARFUM,
            #I_DISLIKE_TAG,
            #I_DISLIKE_OBJ,
            I_DISLIKE_BRAND,
            I_LIKE_TAG,
            I_LIKE_OBJ,
            I_LIKE_BRAND,
            COUNTRY_EXT,
            WHAT_EXISTS,
            SHOW_ANY]

