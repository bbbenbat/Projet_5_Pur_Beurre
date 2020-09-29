# !/usr/bin/env python
# -*- coding: utf-8 -*-
import os.path
import time

import requests

from controllers import orm
from misc import tools


class Api:
    """ All API data processing with registration in the database. """
    def __init__(self):
        """ Return the subcategories from subcategories.json """
        self.list_subcategories = tools.read_json('settings.json')

    def api_subcategory(self, categ):
        """ function for API connexion for the subcategories
        Used in start_init."""
        global API_URL, parameters, data
        API_URL = "https://fr.openfoodfacts.org/cgi/search.pl?"
        ACTION = "process"
        TAGTYPE_0 = "categories"
        TAG_CONTAINS_0 = "contains"
        TAG_0 = categ
        JSON = "true"
        PAGE = int(api.list_subcategories[1])
        PAGE_SIZE =  int(api.list_subcategories[2])
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
        #print(data_api_checked)
        return data_api_checked

    def clean_data(self, x):
        """ Select and change the order of values, save in a list for the SQL upload
        Return a list for database insertion : list_sql.
        Used in start_init"""
        list_sql = []
        for line in x:
            if 'ingredients_text_fr' in line.keys():
                ingredients = tools.rp2cara(line["ingredients_text_fr"], '(', ')', '/')
                # print(line["ingredients_text_fr"])
                tupleSql = (
                    line["product_name"], line["nutrition_grades_tags"][0], line["url"], line["code"], ingredients,
                    line["id_category"], line["stores_tags"], line["categories_hierarchy"])
                list_sql.append(tupleSql)
            elif 'ingredients_text_en' in line.keys():
                ingredients = tools.rp2cara(line["ingredients_text_en"], '(', ')', '/')
                # print(ingredients)
                tupleSql = (
                    line["product_name"], line["nutrition_grades_tags"][0], line["url"], line["code"], ingredients,
                    line["id_category"], line["stores_tags"], line["categories_hierarchy"])
                list_sql.append(tupleSql)
            else:
                ingredients = (line["product_name"])
                # print(ingredients)
                tupleSql = (
                    line["product_name"], line["nutrition_grades_tags"][0], line["url"], line["code"], ingredients,
                    line["id_category"], line["stores_tags"], line["categories_hierarchy"])
                list_sql.append(tupleSql)
        return list_sql

    def save_data(self):
        """ Update the subcategories, products in Pur Beurre database. """
        print("PAGE",  int(api.list_subcategories[1]), "NOMBRE PRODUIT", int(api.list_subcategories[2]))
        listAllProduct = []
        orm_imp = orm.Orm()
        name_cat = orm_imp.name_subcategory()
        orm_imp.subcat(self.list_subcategories[0])
        for cate in name_cat:
            # to find the ID of the category in Subcategory table
            print(cate.name)
            data = self.api_subcategory(cate.name)
            # we create a global list with all dictionaries
            for row in data:
                row['id_category'] = int(cate.id)
                listAllProduct.append(row)
            # Call the function to create a list checked for the SQL integration
        all_product = self.clean_data(listAllProduct)
        # Call the function to save data to the database in the table (TProduct)
        print("ALL_PRODUCT :", all_product)
        orm_imp.save_data(all_product)


if __name__ == '__main__':
    # Check if settings file is in admin folder before to start.
    if os.path.isfile('settings.json'):
        api = Api()
        api.save_data()
    else:
        print("Fichier \"settings.json\" absent du dossier admin. \nVeuillez le placer dans le dossier.")
        time.sleep(5.0)
