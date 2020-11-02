# !/usr/bin/env python
# -*- coding: utf-8 -*-
""" This modules manages the user interface for the product research. """

from controllers import orm
from misc import tools

orm_imp = orm.Orm()
tools = tools.Tools()


class Console:
    """ Visual interface for the application."""

    def console(self):
        """ Start menu, user can choice :find substitute product
        or see the historic of research. """
        controle_point = 1
        while controle_point == 1:
            sel_welcome = self.welcome_input()
            controle_point = tools.check_value_break(
                sel_welcome, controle_point)
            if sel_welcome == 1:
                while controle_point == 2:
                    # Print category.
                    select_cate = self.categories()
                    # Number of categories.
                    last_select_cat = len(select_cate) - 1
                    user_cat = self.check_value('catégorie',
                                                0, last_select_cat)
                    controle_point = tools.check_value_break(
                        user_cat, controle_point)
                    while controle_point == 3:
                        sub_categ = self.subcategories(
                            orm_imp.select_sub_category(select_cate[user_cat]),
                            select_cate[user_cat])
                        user_prod = self.check_list_value('Produit', sub_categ)
                        controle_point = tools.check_value_break(
                            user_prod, controle_point)
                        while controle_point == 4:
                            controle_point = self.proposal_product(user_prod)
            elif sel_welcome == 2:
                self.show_research()
                controle_point = 1
            else:
                print("Veuillez resaisir un choix compris entre 1 et 2.")
                controle_point = 1

    def welcome_input(self):
        """ Main section """
        sel_welcome = int(input("==============================\n"
                                "==========PUR BEURRE==========\n"
                                "= Que souhaitez-vous faire ? =\n"
                                "==============================\n"
                                "Avoir un produit plus sain : tapez 1\n"
                                "Voir mon historique de recherche : tape 2\n"
                                "Taper 99 à tout moment pour "
                                "revenir en arrière."
                                ))
        return sel_welcome

    def categories(self):
        """ Show the categories. """
        self.select_cat = orm_imp.select_category()
        print("CATEGORIES:")
        for cat in enumerate(self.select_cat):
            print(cat[0], cat[1])
        return self.select_cat

    def subcategories(self, ssub_cat, user_cat):
        """ Show the subcategories (reference products). """
        select_sub_cat = {}
        min_sub_cat = []
        print("POUR LA CATEGORIE", user_cat, ":")
        for sub in ssub_cat:
            select_sub_cat.update({sub.id: sub.name})
        for sub_cat in sorted(select_sub_cat.items(), key=lambda t: t[0]):
            print(sub_cat[0], sub_cat[1].replace('_', ' '))
            min_sub_cat.append(sub_cat[0])
        return min_sub_cat

    def proposal_product(self, user_prod):
        """ Show the best products and permit to save,
        make another research or go back to main section. """
        # Give the bests product, selected by nutriscore value.
        prod0 = orm_imp.list_prod(user_prod)
        prod = self.show_proposal(prod0)
        user_choice = int(input(
            "==============================\n"
            "= Que souhaitez-vous faire ? =\n"
            "==============================\n"
            "- Sauvegarder un produit proposé : taper 1\n"
            "- Faire une autre recherche produit : taper 2\n"
            "- Retourner à l'écran principal : taper 3\n"))
        if user_choice == 1:  # save product, go to main section
            self.save_product(prod[0], prod[1], prod[2], user_prod)
            self.controle_point = 1
        elif user_choice == 2:  # goback to product research section
            self.controle_point = 2
        elif user_choice == 3:  # go to main section
            self.controle_point = 1
        else:
            print("Veuillez entrer un chiffre compris entre 1 et 3.")
            self.controle_point = 4
        return self.controle_point

    def show_proposal(self, req):
        """ Give the bests product, selected by nutriscore value."""
        z = 1
        y = z
        x = 1
        self.dico_product = {}
        for prod in req:
            if z <= 5:
                List_store = orm_imp.find_store(prod.id)
                print("Choix numéro", z, ":", prod.name, "| score : ",
                      prod.nutriscore, "| Magasins : ", List_store,
                      "| Lien :",
                      prod.url, "| \n ==> description :",
                      prod.ingredient, "\n==================================")
                self.dico_product.update({z: prod.id})
                x += 1
            z += 1
        return self.dico_product, y, x - 1

    def show_research(self):
        """ Show all research saved. """
        self.list_research = orm_imp.read_research()
        print("========================================================")
        for row in self.list_research:
            print(
                row["date"], "|| Produit :", row['subcat'],
                "|| Meilleure proposition :", row['product'], "| Score :",
                row['nutriscore'], "| Lien :", row['url'],
                "| Ingrédients :", row['ingredient'])
            print("========================================================")

    def save_product(self, prod_0, prod_1, prod_2, user_prod):
        """ Save the product selected by user. prod_1: min number for the selection,
        prod_2: max number, prod_0:dictionary with the best products,
        user_prod= subcategory id."""
        print("=============================================\n"
              "= Quel produit souhaitez-vous sauvegarder ? =\n"
              "=============================================\n")
        choice = self.check_value('Produit préféré', prod_1, prod_2)
        x = 0
        while x < 3:
            try:
                orm_imp.save_user_select(prod_0, user_prod, choice)
                print("Sélection sauvegardée!\n")
                break
            except:
                print("Erreur lors de l'enregistrement, tentative n°", x)
                x += 1
                if x == 3:
                    print("Impossible d'enregistré cette recherche, "
                          "veuillez recommencer.")

    def check_value(self, name, min_int, max_int):
        """ Check if the values are correct """
        while True:
            numb = input(f"-- {name} : Entrez une valeur comprise "
                         f"entre {min_int} et {max_int} : ")
            try:
                check = int(numb)
                if check == 99 or min_int <= check <= max_int:
                    break
            except ValueError:
                pass
        return check

    def check_list_value(self, name, list_int):
        """ Check if the values are correct """
        while True:
            numb = input(f"-- {name} : "
                         f"Entrez une de ces valeurs : {list_int} : ")
            try:
                check = int(numb)
                if check in list_int or check == 99:
                    break
            except ValueError:
                pass
        return check
