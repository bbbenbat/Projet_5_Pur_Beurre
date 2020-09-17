# !/usr/bin/env python
# -*- coding: utf-8 -*-
from peewee import *
import orm_request
from orm_data import Category, Product, Research, Product, Store, ProductStore, database as database
from tools import ask_integer

# SQL_connection.connect()
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
                # ask_integer("Catégorie", 0, )
                user_cat = int(input("Entrer le numéro de catégorie que vous recherchez :\n"))
                check = Category.select().count()
                if user_cat >= 0 and user_cat <= check:
                    while True:
                        # print("categorie selectionnee : ", select_cat[user_cat])
                        sub_categ = ORMR.select_sub_category(select_cat[user_cat])
                        # ORMR.list_prod(sel_cat)
                        user_prod = int(input("Entrer le numéro du produit que vous recherchez :\n"))
                        try:
                            prod = ORMR.list_prod(user_prod)
                            user_choice = int(input("Que souhaitez-vous faire?\n - Sauvegarder un produit proposé : taper 1\n - Faire une autre recherche produit : taper 2\n - Retourner à l'écran principal : taper 3\n"))
                            if user_choice == 1:
                                # Ask to user which product must be saved
                                # Save the research to Research table
                                print("**",sub_categ, user_prod)
                                ORMR.save_user_select(prod, user_prod)
                                print("Sauvegarde produit!\n")
                            elif user_choice == 2:
                                # goback to product research section
                                print("Ecran selection produit!")
                            elif user_choice == 3:
                                # go to Main section
                                print("Retour écran principal!")
                        except:
                            print("Veuillez entrer un chiffre correspondant à un produit!")
                else:
                    print("Veuillez entrer un chiffre correspondant à une catégorie!")
        elif sel_welcome == 2:
            print("Todo")
            start = 0
        else:
            print("veuillez resaisir un choix compris entre 1 et 2")


if __name__ == "__main__":
    main()
