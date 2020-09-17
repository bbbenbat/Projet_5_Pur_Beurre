# !/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import tools

listAllProduct = []
listSQl = []


def list_subcategories():
    """  """
    global LIST_SUBCATEGORIES
    category_1 = 'pizza au thon'
    category_2 = 'pizza aux legumes'
    category_3 = 'pizza au fromage'
    category_4 = 'pizza au jambon'
    category_5 = 'yaourt aux fruits'
    category_6 = 'yaourt au chocolat'
    category_7 = 'yaourt nature'
    category_8 = 'yaourt au caramel'
    category_9 = 'confiture à la fraise'
    category_10 = 'confiture à la framboise'
    category_11 = 'confiture d abricot'
    category_12 = 'confiture d orange'
    category_13 = 'jus de pomme'
    category_14 = 'jus d orange'
    category_15 = 'jus de raisin'
    category_16 = 'jus d ananas'
    LIST_SUBCATEGORIES = (
        category_1, category_2, category_3, category_4, category_5, category_6, category_7, category_8, category_9,
        category_10, category_11, category_12, category_13, category_14, category_15, category_16)
    return LIST_SUBCATEGORIES


def api_category(categ):
    # function for API connexion
    global API_URL, parameters, data
    API_URL = "https://fr.openfoodfacts.org/cgi/search.pl?"
    ACTION = "process"
    TAGTYPE_0 = "categories"
    TAG_CONTAINS_0 = "contains"
    TAG_0 = categ
    JSON = "true"
    PAGE = 1
    PAGE_SIZE = 5
    FIELDS = "product_name,nutrition_grades_tags,code,url,categories,stores_tags,categories_hierarchy"
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


def ReqSql(x):
    # change the order of values and save in a list for the SQL upload
    fr_ing = 0
    en_ing = 0
    for line in x:
        if 'ingredients_text_fr' in line.keys():
            ingredients = tools.rp2cara(line["ingredients_text_fr"], '(', ')', '/')
            # print(line["ingredients_text_fr"])
            tupleSql = (
                line["product_name"], line["nutrition_grades_tags"][0], line["url"], line["code"], ingredients,
                line["id_category"], line["stores_tags"], line["categories_hierarchy"])
            listSQl.append(tupleSql)
            fr_ing += 1
        else:
            ingredients = tools.rp2cara(line["ingredients_text_en"], '(', ')', '/')
            #print(ingredients)
            tupleSql = (
                line["product_name"], line["nutrition_grades_tags"][0], line["url"], line["code"], ingredients,
                line["id_category"], line["stores_tags"], line["categories_hierarchy"])
            listSQl.append(tupleSql)
            #print("------", ingredients)
            en_ing += 1
    print("FR : ", fr_ing, "EN : ", en_ing)
    print("liste pour insertion sql", listSQl)
    return listSQl
