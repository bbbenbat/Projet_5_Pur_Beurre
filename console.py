# !/usr/bin/env python
# -*- coding: utf-8 -*-
from peewee import *
import orm_request
from orm_data import Category, Product, Research, Product, Store, ProductStore, database as database
from tools import ask_integer

#SQL_connection.connect()
ORMR = orm_request



def user_input():
    global sel_welcome
    sel_welcome = int(input("Bienvenue sur l'application PurBeurre!\n"
                            "Que souhaitez-vous faire (saisir un chiffre)?\n"
                            "Avoir un produit de remplacement plus sain |1|\n"
                            "Voir mon historique de recherche |2|\n"
                            ))
    return sel_welcome

def main():
    while True:
        user_input()
        if sel_welcome == 1:
            while True:
                select_cat = ORMR.select_category()
                ask_integer("Catégorie", 0, )
                user_cat = int(input("Entrer le numéro de catégorie que vous recherchez :\n"))
                check = 4 #Category.select(fn.COUNT(Category.id))
                if user_cat >= 0 and user_cat <= check:
                    while True:
                        print("categorie selectionnee : ",select_cat[user_cat])
                        select_sub_cat = ORMR.select_sub_category(select_cat[user_cat])
                        #ORMR.list_prod(sel_cat)
                        user_prod = int(input("Entrer le numéro du produit que vous recherchez :\n"))
                        try:
                            print("saisie user pour le numéro de produit :", user_prod)
                            prod = ORMR.list_prod(user_prod)
                            break
                        except:
                            print("Veuillez entrer un chiffre correspondant à un produit!")
                else:
                    print("Veuillez entrer un chiffre correspondant à une catégorie!")
        elif sel_welcome == 2:
            print("Todo")
            start = 0
        else:
            print("veuillez resaisir un choix compris entre 1 et 2")

if __name__ == "__main__" :
    main()