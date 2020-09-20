# !/usr/bin/env python
# -*- coding: utf-8 -*-
from peewee import *
from orm_data import Subcategory, Research, Product, Store, ProductStore, database
import API_connection
from datetime import datetime
import time

API_LIST = API_connection.list_subcategories()
select_cat = []
select_sub_cat = {}


def create_table():
    """WARNING : Delete et Create all tables of PUR_BEURRE Database!!!
    Used in start_init."""
    # database.connect()
    database.drop_tables([Subcategory, Product, Research, Store, ProductStore])
    database.create_tables([Subcategory, Product, Research, Store, ProductStore])
    # database.close()


def create_subcat():
    """ Create categories selected on API connexion, in Subcategory table.
    Used in start_init."""
    for req in API_LIST:
        try:
            Subcategory.insert(name=req).execute()
        except:
            pass


def check_delete():
    """ As to user if he want to :
    - delete and create tables from Pur Beurre database
    - update the subcategories (reference product) since subcategories.json
    Used in start_init."""
    # ask delete and create tables from Pur Beurre database
    delete_db = int(input(
        """Voulez-vous effacer l'ensemble des données de la base Pur Beurre (les données seront DEFINITIVEMENT perdues)?
        => OUI = taper 1
        => NON = taper 2\n"""))
    if delete_db == 1:
        create_table()
        create_subcat()
        print("Effacement de la base de donnée et mise à jour des produits de réference.")
        print("La mise à jour des produits de substitution va se faire dans quelques secondes.\n")
        time.sleep(2.0)
    elif delete_db == 2:
        # ask if update the subcategories (reference product) since subcategories.json
        update_subcat = int(input(
            """Voulez vous mettre à jour les produits de référence (apres avoir mis à jour le fichier subcategories.json)?
            => OUI = taper 1
            => NON = taper 2\n"""))
        if update_subcat == 1:
            create_subcat()
            print("Mise à jour des produits de réference.")
            print("La mise à jour des produits de substitution va se faire dans quelques secondes.\n")
            time.sleep(2.0)
        elif update_subcat == 2:
            pass
        else:
            print(
                "Erreur de saisie!!!\n"
                "Veuillez relancer l'application si vous souhaitez effacer la base de donnée ou modifier les produits de référence.\n"
                "La mise à jour des produits de substitution va se faire dans 5 secondes.\n")
            time.sleep(8.0)
    else:
        print(
            "Erreur de saisie!!!\n"
            "Veuillez relancer l'application si vous souhaitez effacer la base de donnée ou modifier les produits de référence.\n"
            "La mise à jour des produits de substitution va se faire dans quelques secondes.\n")
        time.sleep(8.0)
    while True:
        # ask page number
        page = int(input("Quel numéro de page souhaitez-vous (entre 1 et 9)?\n"))
        if 1 <= page <= 9:
            break
        else:
            print("Mauvaise chiffre, veuillez resaisir:\n ")
    while True:
        # ask number of product
        num_prod = int(input("Combien de produits de substitution souhaitez-vous (entre 1 et 100)?\n"))
        if 1 <= num_prod <= 100:
            break
        else:
            print("Mauvaise chiffre, veuillez resaisir:\n ")
    return page, num_prod


def id_category(cat):
    """ Give the id of each category of Subcategory table.
    Used in start_init."""
    id_cat = Subcategory.get(Subcategory.name == cat).id
    print(id_cat)
    return id_cat


def save_data(list):
    """ Check and save API's data to the database.
    Used in start_init."""
    for line in list:
        ### Product section
        # if product is not in the table (check with name and barcode)
        query_pr = Product.select().where(Product.name == line[0], Product.barcode == line[3])
        if query_pr.exists():
            print("Existe déjà!, PRODUIT :", line[0], "BARCODE" == line[3])
            pass
        else:
            # save product
            exe_pr = Product.insert(name=line[0], nutriscore=line[1], url=line[2],
                                    barcode=line[3], ingredient=line[4],
                                    id_category=line[5], categories_hierarchy=line[7])
            # save the Product table id in id_pr variable
            id_pr = exe_pr.execute()
            ### Store section
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
    s_cat = Subcategory.select()
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
    ssub_cat = Subcategory.select().where(Subcategory.name.iregexp(req))
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
    x = 1
    dico_product = {}
    produ = Product.select().where(Product.id_category == req).order_by(Product.nutriscore.asc())
    for prod in produ:
        if z <= 5:
            List_store = find_store(prod.id)
            print("Choix numéro", z, ":", prod.name, "| score : ", prod.nutriscore, "| Magasins : ", List_store,
                  "| Lien :",
                  prod.url, "| \n ==> description :",
                  prod.ingredient, "\n======================================================")
            dico_product.update({z: prod.id})
            x += 1
        z += 1
    return dico_product, y, x - 1


def find_store(req):
    """ Show all stores of the product (req).
    Used in list_prod()."""
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
    req2 is the minimal number for choice user
    req3 is the maximal number for choice user
    Used in console."""
    x = 0
    while x == 0:
        choice = int(input("=============================================\n"
                           "= Quel produit souhaitez-vous sauvegarder ? =\n"
                           "=============================================\n"))
        if req2 <= choice <= req3:
            Research.insert(id_product_best=req[choice], id_product=req1, date=datetime.now()).execute()
            print("Sélection sauvegardée!\n")
            x = 1
        else:
            print("Veuillez entrer un chiffre compris entre ", req2, " et ", req3)


def read_research():
    """ Show the research saved.
    Used in console."""
    print("==================================================================")
    # Use the many to many relation
    for row in Research \
            .select(Research.id_subcategory, Research.id_product_best, Product.name.alias('product'),
                    Subcategory.name.alias('subcat'), Product.nutriscore, Product.ingredient,
                    Research.date) \
            .join(Product) \
            .switch(Research) \
            .join(Subcategory) \
            .order_by(Research.date) \
            .dicts():
        print(
            row["date"], "|| Produit :", row['subcat'], "|| Meilleure proposition :", row['product'], "| Score :",
            row['nutriscore'], "| Ingrédients :", row['ingredient'])
        print("==================================================================")
