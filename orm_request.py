# !/usr/bin/env python
# -*- coding: utf-8 -*-
from peewee import *
from orm_data import Category, Product, Research, Product, Store, ProductStore, database as database
import API_connection
import tools

API_LIST = API_connection.list_categories()
select_cat = []
select_sub_cat = {}

"""
def list_cat():
    for cat in Category.select().order_by(Category.id.asc()):
        print(cat.id, cat.name)
"""

def id_category(cat):
    """ Give the id of each category of Category table.
    Used in start_init."""
    id_cat = Category.get(Category.name == cat).id
    print(id_cat)
    return id_cat


def create_cat():
    """ Create categories selected on API connexion, in Category table.
    Used in start_init."""
    for req in API_LIST:
        try:
            Category.insert(name=req).execute()
        except:
            pass


def create_table():
    """WARNING : Delete et Create all tables of PUR_BEURRE Database!!!
    Used in start_init."""
    # database.connect()
    database.drop_tables([Category, Product, Research, Store, ProductStore])
    database.create_tables([Category, Product, Research, Store, ProductStore])
    # database.close()


def check_data(list):
    """ Check and save API's data to the database.
    Used in start_init."""
    for line in list:
        ### Product section
        # if product is not in the table (check with name and barcode)
        query_pr = Product.select().where(Product.name == line[0], Product.barcode == line[3])
        if query_pr.exists():
            print("Existe déjà!")
            pass
        else:
            # save product
            exe_pr = Product.insert(name=line[0], nutriscore=line[1], url=line[2],
                                    barcode=line[3], ingredient=line[4],
                                    id_category=line[5], categories_hierarchy=line[7])
            # save the Product id on the new product
            id_pr = exe_pr.execute()
            ### Store section
            print(line[6])
            # check_st = tools.splite_tuple_to_liste(line[6])
            check_st = line[6]
            # print(">",check_st)
            # if there is a store with the product
            if check_st is not None:
                # for each store
                for sto in check_st:
                    # check if store is in Store table
                    id_st = Store.select().where(Store.name == sto)
                    if id_st.exists():
                        # id_st = 0
                        pass
                    else:
                        # create store in Store table
                        Store.insert(name=sto).execute()
                        id_st = Store.select().where(Store.name == sto)
                    print("product", id_pr, "store :", id_st)
                    ### Product_store section
                    # save the relation between product and store in Product_store table
                    try:
                        ProductStore.insert(product_id=id_pr, store_id=id_st).execute()
                    except:
                        print("Erreur sur :", id_pr, id_st)


def select_category():
    """ Give the categories regarding the subcategories of the database.
     The categories are the first word of the subcategories.
     Used in console."""
    aze = Category.select()
    for cat in aze:
        cate = cat.name.split()[:1]
        if cate[0] in select_cat:
            pass
        else:
            select_cat.append(cate[0])
    for cat in enumerate(select_cat):
        print(cat[0], cat[1])
    return select_cat


def select_sub_category(req):
    """ Give the subcategories regarding the category selected(req).
    Used in console."""
    aze = Category.select().where(Category.name.iregexp(req))
    for sub in aze:
        # print(sub)
        select_sub_cat.update({sub.id: sub.name})
        # print(select_sub_cat)
    for sub_cat in sorted(select_sub_cat.items(), key=lambda t: t[0]):
        print(sub_cat[0], sub_cat[1])
    return select_sub_cat


def list_prod(req):
    """ Give the bests product, selected by nutriscore value.
    Used in console."""
    x = 1
    print(">>> >>>", req)
    produ = Product.select().where(Product.id_category == 9).order_by(Product.nutriscore.asc())
    for prod in produ:
        print("Choix numéro", x, ":", prod.name, ", score nutritionnel : ", prod.nutriscore)
        x += 1

# list_prod(9)
# select_sub_category()
# create_table()
# create_cat()
