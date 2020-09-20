# !/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import tools

listAllProduct = []
listSQl = []


def list_subcategories():
    """ Return the subcategories from subcategories.json """
    global LIST_SUBCATEGORIES
    LIST_SUBCATEGORIES = tools.read_json('subcategories.json')
    return LIST_SUBCATEGORIES


def api_subcategory(categ, req1, req2):
    """ function for API connexion for the subcategories
    Used in start_init."""
    global API_URL, parameters, data
    API_URL = "https://fr.openfoodfacts.org/cgi/search.pl?"
    ACTION = "process"
    TAGTYPE_0 = "categories"
    TAG_CONTAINS_0 = "contains"
    TAG_0 = categ
    JSON = "true"
    PAGE = req1
    PAGE_SIZE = req2
    FIELDS = "product_name,nutrition_grades_tags,url,code,ingredients_text_fr,categories,stores_tags,categories_hierarchy"
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
    # Check that all fields are in data_api, if not it will be created with '' value
    data_api_checked = tools.check_list(data_api, FIELDS.split(','))
    return data_api_checked


def ReqSql(x):
    """ Select and change the order of values, save in a list for the SQL upload
    Return a list for database insertion.
    Used in start_init"""
    for line in x:
        if 'ingredients_text_fr' in line.keys():
            ingredients = tools.rp2cara(line["ingredients_text_fr"], '(', ')', '/')
            # print(line["ingredients_text_fr"])
            tupleSql = (
                line["product_name"], line["nutrition_grades_tags"][0], line["url"], line["code"], ingredients,
                line["id_category"], line["stores_tags"], line["categories_hierarchy"])
            listSQl.append(tupleSql)
        elif 'ingredients_text_en' in line.keys():
            ingredients = tools.rp2cara(line["ingredients_text_en"], '(', ')', '/')
            # print(ingredients)
            tupleSql = (
                line["product_name"], line["nutrition_grades_tags"][0], line["url"], line["code"], ingredients,
                line["id_category"], line["stores_tags"], line["categories_hierarchy"])
            listSQl.append(tupleSql)
        else:
            ingredients = (line["product_name"])
            # print(ingredients)
            tupleSql = (
                line["product_name"], line["nutrition_grades_tags"][0], line["url"], line["code"], ingredients,
                line["id_category"], line["stores_tags"], line["categories_hierarchy"])
            listSQl.append(tupleSql)
    return listSQl
