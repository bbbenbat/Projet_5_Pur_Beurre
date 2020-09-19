# !/usr/bin/env python
# -*- coding: utf-8 -*-
from peewee import *
import orm_request
from orm_data import Category, Product, Research, Product, Store, ProductStore, database as database
from tools import ask_integer

# SQL_connection.connect()
ORMR = orm_request


def user_input():
    print("Bienvenue sur l'application PurBeurre!\n")
    global sel_welcome
    sel_welcome = int(input("Que souhaitez-vous faire ?\n"
                            "Avoir un produit de remplacement plus sain : tapez 1\n"
                            "Voir mon historique de recherche : tape |2|\n"
                            ))
    return sel_welcome


def main():
    main_page = 0
    while main_page == 0:
        start_page = 0
        while start_page == 0:
            user_input()
            # sel_welcome = 0
            search_page = 0
            if sel_welcome == 1:
                while search_page == 0:
                    start_page = 0
                    select_cate = ORMR.select_category()
                    last_select_cat = len(select_cate) - 1
                    user_cat = int(input("=> Entrer le numéro de catégorie que vous recherchez :\n"))
                    if user_cat >= 0 and user_cat <= last_select_cat:
                        while start_page == 0:
                            sub_categ = ORMR.select_sub_category(select_cate[user_cat])
                            user_prod = int(input("=> Entrer le numéro du produit que vous recherchez :\n"))
                            check_input = 0
                            while sub_categ[1] <= user_prod <= sub_categ[2] and check_input == 0:
                                prod = ORMR.list_prod(user_prod)
                                user_choice = int(input(
                                    """
                                    => Que souhaitez-vous faire?\n 
                                    - Sauvegarder un produit proposé : taper 1\n 
                                    - Faire une autre recherche produit : taper 2\n 
                                    - Retourner à l'écran principal : taper 3\n"""))
                                if user_choice == 1:
                                    # Ask to user which product must be saved
                                    # Save the research to Research table
                                    ORMR.save_user_select(prod[0], user_prod, prod[1], prod[2])
                                    check_input = 1
                                    start_page = 1
                                    search_page = 1
                                elif user_choice == 2:
                                    # goback to product research section
                                    # print("Entrer le numéro de catégorie que vous recherchez :\n")
                                    check_input = 1
                                    start_page = 1
                                elif user_choice == 3:
                                    # go to Main section
                                    check_input = 1
                                    start_page = 1
                                    search_page = 1
                                else:
                                    print("!!! Veuillez entrer un chiffre compris entre 1 et 3 !!!")
                            # else:
                            #    print("!!! Veuillez entrer un nombre compris entre", sub_categ[1], "et", sub_categ[2],
                            #          "!!!")
                    else:
                        print("!!! Veuillez entrer un chiffre correspondant à une catégorie!!!")
            elif sel_welcome == 2:
                ORMR.read_research()
                print()
                start = 0
            else:
                print("veuillez resaisir un choix compris entre 1 et 2")


if __name__ == "__main__":
    main()
