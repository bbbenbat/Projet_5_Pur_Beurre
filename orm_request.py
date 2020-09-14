# !/usr/bin/env python
# -*- coding: utf-8 -*-
from peewee import *
from orm_data import Category, Product, Research, Product, Store, ProductStore, database as database
import API_connection
import tools

API_LIST = API_connection.list_categories()


# print(A)
# database.connect()
def list_cat():
    for cat in Category.select().order_by(Category.id.asc()):
        print(cat.id, cat.name)


def id_category(cat):
    id_cat = Category.get(Category.name == cat).id
    print(id_cat)
    return id_cat


def list_prod(x):
    for prod in Product.select().where(Product.id_category == 1):
        print(prod.id, "|", prod.name)


def import_bdd(req):
    """ This class sends the data to the Product Table """
    print("*/*", req)
    Product.insert_many(req, fields=[Product.name, Product.nutriscore, Product.url, Product.barcode, Product.ingredient,
                                     Product.id_category]).execute()


def create_cat():
    """ Create categories selected on API connexion, in Category table."""
    for req in API_LIST:
        try:
            Category.insert(name=req).execute()
        except:
            pass


def create_table():
    """WARNING : Delete et Create all tables of PUR_BEURRE Database!!!"""
    # database.connect()
    database.drop_tables([Category, Product, Research, Store, ProductStore])
    database.create_tables([Category, Product, Research, Store, ProductStore])
    # database.close()


def check_data(list):
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
                                    id_category=line[5])
            # save the Product id on the new product
            id_pr = exe_pr.execute()
            ### Store section
            # check_s = line[6]
            check_st = tools.splite_tuple_to_liste(line[6])
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

# create_table()
# create_cat()
