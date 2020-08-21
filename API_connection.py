# !/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import SQL_connection


# function for API connexion
def api_category(category):
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


# change the order of values and save in a list for the SQL upload
def ReqSql(x):
    for line in x:
        tupleSql = (line["product_name"], line["nutriscore_grade"], line["url"], line["code"], line["stores"], line["categories"])
        listSQl.append(tupleSql)
    # print(listSQl)
    return listSQl


listAllProduct = []
LIST_CATEGORIES = ('pizza', 'pain-de-mie', 'saucisson', 'quiche')
listSQl = []


def main():
    # loop for each category
    for cate in LIST_CATEGORIES:
        # we call the function api_category for the API connection
        api_category(cate)
        # we put the dictionary to the list
        listProduct = data['products']
        # we create a global list with the data from all categories
        for row in listProduct:
            listAllProduct.append(row)
    #print(listAllProduct)
    # Call the function to create the list for the SQL integration
    ReqSql(listAllProduct)
    # Call the function to save data to the database in the table (TProduct)
    SQL_connection.ImportBdd(listSQl)


if __name__ == '__main__':
    main()
