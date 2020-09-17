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
                last_select_cat = len(select_cat) - 1
                user_cat = int(input("=> Entrer le numéro de catégorie que vous recherchez :\n"))
                check = Category.select().count()
                if user_cat >= 0 and user_cat <= last_select_cat:
                    while True:
                        sub_categ = ORMR.select_sub_category(select_cat[user_cat])
                        user_prod = int(input("=> Entrer le numéro du produit que vous recherchez :\n"))
                        print("USER_PROD",user_prod)
                        check_input = 0
                        while sub_categ[1] <= user_prod <= sub_categ[2] and check_input == 0:
                            prod = ORMR.list_prod(user_prod)
                            print("PROD",prod)
                            user_choice = int(input(
                                "=> Que souhaitez-vous faire?\n - Sauvegarder un produit proposé : taper 1\n - Faire une autre recherche produit : taper 2\n - Retourner à l'écran principal : taper 3\n"))
                            if user_choice == 1:
                                # Ask to user which product must be saved
                                # Save the research to Research table
                                ORMR.save_user_select(prod[0], user_prod, prod[1], prod[2])
                                # print("Sélection sauvegardée!\n")
                            elif user_choice == 2:
                                # goback to product research section
                                print("Entrer le numéro de catégorie que vous recherchez :\n")
                                break
                            elif user_choice == 3:
                                # go to Main section
                                print("Retour écran principal!")
                            else:
                                print("!!! Veuillez entrer un chiffre compris entre 1 et 3 !!!")
                        else:
                            print("!!! Veuillez entrer un nombre compris entre", sub_categ[1], "et", sub_categ[2], "!!!")
                else:
                    print("!!! Veuillez entrer un chiffre correspondant à une catégorie!!!")
        elif sel_welcome == 2:
            print("Todo")
            start = 0
        else:
            print("veuillez resaisir un choix compris entre 1 et 2")


if __name__ == "__main__":
    main()
