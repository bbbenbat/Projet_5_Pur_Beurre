# !/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import tools

# import orm_request


listAllProduct = []
# LIST_CATEGORIES = ('pizza', 'pain-de-mie', 'saucisson', 'quiche')
# LIST_CATEGORIES = ('pizza au thon', 'pizza vegetarienne', 'pizza au fromage', 'pizza au poulet')
listSQl = []



def list_categories():
    global LIST_CATEGORIES
    category_1 = 'pizza au thon'
    category_2 = 'pizza aux legumes'
    category_3 = 'pizza au fromage'
    category_4 = 'pizza au jambon'
    LIST_CATEGORIES = (category_1, category_2, category_3, category_4)
    return LIST_CATEGORIES


# function for API connexion
def api_category(categ):
    global API_URL, parameters, data
    API_URL = "https://fr.openfoodfacts.org/cgi/search.pl?"
    ACTION = "process"
    TAGTYPE_0 = "categories"
    TAG_CONTAINS_0 = "contains"
    TAG_0 = categ
    JSON = "true"
    PAGE = 1
    PAGE_SIZE = 20
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
    data_api = res.json()
    return data_api



# change the order of values and save in a list for the SQL upload
def ReqSql(x):
    fr_ing = 0
    en_ing = 0
    for line in x:
        # tupleSql = (line["product_name"], line["nutriscore_grade"], line["url"], line["code"], line["stores"], line["categories"], line["id_category"])
        if 'ingredients_text_fr' in line.keys():
            ingredients = tools.rp2cara(line["ingredients_text_fr"],'(',')','/')
            #print(line["ingredients_text_fr"])
            tupleSql = (
            line["product_name"], line["nutriscore_grade"], line["url"], line["code"], ingredients,
            line["id_category"], line["stores"])
            listSQl.append(tupleSql)
            fr_ing += 1
        else:
            ingredients = tools.rp2cara(line["ingredients_text_en"], '(', ')', '/')
            print(ingredients)
            tupleSql = (
            line["product_name"], line["nutriscore_grade"], line["url"], line["code"], ingredients,
            line["id_category"], line["stores"])
            listSQl.append(tupleSql)
            print("------",ingredients)
            en_ing += 1
    print("FR : ", fr_ing, "EN : ", en_ing)
    print("liste pour insertion sql", listSQl)
    return listSQl






