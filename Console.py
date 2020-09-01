# !/usr/bin/env python
# -*- coding: utf-8 -*-
import SQL_connection

SQL_connection.connect()


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
                SQL_connection.ListCat()
                sel_cat = int(input("Entrer le numéro de catégorie que vous recherchez :\n"))
                if sel_cat >= 1 and sel_cat <= 4:
                    while True:
                        SQL_connection.ListProd(sel_cat)
                        sel_product = int(input("Entrer le numéro du produit que vous recherchez :\n"))
                        try:
                            print("Affichage produit de substitution")
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