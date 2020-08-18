import requests


def api_category(category):  # class for API connexion
    global API_URL, parameters, data
    API_URL = "https://fr.openfoodfacts.org/cgi/search.pl?"
    ACTION = "process"
    TAGTYPE_0 = "categories"
    TAG_CONTAINS_0 = "contains"
    TAG_0 = category
    JSON = "true"
    PAGE = 1
    PAGE_SIZE = 10
    FIELDS = "product_name,nutriscore_grade,code,url,categories,stores"
    parameters = {'action': ACTION,
                  'tagtype_0': TAGTYPE_0,
                  'tag_contains_0': TAG_CONTAINS_0,
                  'tag_0': TAG_0,
                  'json': JSON,
                  'page': PAGE,
                  'page_size': PAGE_SIZE,
                  'fields': FIELDS}
    res = requests.get(API_URL, parameters)
    data = res.json()


listAllProduct = []
LIST_CATEGORIES = ('pizza', 'sodas', 'saucisson', 'quiche')


def main():
    # loop for each category
    for cate in LIST_CATEGORIES:
        # we call on  fait 4 boucles (nombre de catégories)
        api_category(cate)  # pour chaque boucle on appelle la fonction de connexion
        listProduct = data['products']  # on integre les données dans une variable

        for row in listProduct:
            # je parcours toutes les données de products
            # print(x)
            listAllProduct.append(row)
    print(listAllProduct)


if __name__ == '__main__':
    main()
