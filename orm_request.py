# !/usr/bin/env python
# -*- coding: utf-8 -*-
from peewee import *
from orm_data import Category, Research, Product, Store, ProductStore, database
import API_connection
from datetime import datetime
import tools

API_LIST = API_connection.list_subcategories()
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
    print("CATEGORIES:")
    s_cat = Category.select()
    for cat in s_cat:
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
    select_sub_cat = {}
    min_sub_cat = []
    print("POUR LA CATEGORIE", req, ":")
    ssub_cat = Category.select().where(Category.name.iregexp(req))
    # print("REQUETE SQL NOM CATEGORIE",ssub_cat)
    for sub in ssub_cat:
        select_sub_cat.update({sub.id: sub.name})
    for sub_cat in sorted(select_sub_cat.items(), key=lambda t: t[0]):
        print(sub_cat[0], sub_cat[1])
        min_sub_cat.append(sub_cat[0])
    return select_sub_cat, min_sub_cat[0], min_sub_cat[-1]


def list_prod(req):
    """ Give the bests product, selected by nutriscore value.
    Used in console."""
    z = 1
    y = z
    dico_product = {}
    produ = Product.select().where(Product.id_category == req).order_by(Product.nutriscore.asc())
    for prod in produ:
        List_store = find_store(prod.id)
        print("Choix numéro", z, ":", prod.name, "| score : ", prod.nutriscore, "| Magasins : ", List_store, "| Lien :",
              prod.url, "| \n ==> description :",
              prod.ingredient, "\n======================================================")
        dico_product.update({z: prod.id})
        z += 1
    return dico_product, y, z - 1


def find_store(req):
    list_store = []
    query = (ProductStore
             .select()
             .join(Product, JOIN.INNER)
             .switch(ProductStore)
             .join(Store, JOIN.INNER)
             .where(ProductStore.product == req))
    for row in query:
        list_store.append(row.store.name)
    # Return list of values without []
    return str(list_store).strip('[]')


def save_user_select(req, req1, req2, req3):
    """ req is the dict of best products
     req1 is the subcategory selected by user
     choice is the best product selected by user """
    x = 0
    while x == 0:
        choice = int(input("Quel produit souhaitez-vous sauvegarder?\n"))
        if req2 <= choice <= req3:
            Research.insert(id_product_best=req[choice], id_product=req1, date=datetime.now()).execute()
            print("Sélection sauvegardée!\n")
            x = 1
        else:
            print("Veuillez entrer un chiffre compris entre ", req2, " et ", req3)


def read_research():
    print("==================================================================")
    for row in Research \
            .select(Research.id_product, Research.id_product_best, Product.name.alias('product'), Category.name.alias('subcat'),
                    Research.date) \
            .join(Product) \
            .switch(Research) \
            .join(Category) \
            .dicts():
        print(row["date"], "|| Product researched :", row['subcat'], "|| Product saved :", row['product'])
    print("==================================================================")


#read_research()
# Ask to user which product must be saved
# Save the research to Research table

# find_store(1)
# list_prod(9)
# select_sub_category()
# create_table()
# create_cat()
