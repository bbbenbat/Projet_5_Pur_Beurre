# !/usr/bin/env python
# -*- coding: utf-8 -*-

from admin import append
from misc import tools

api = append.Api()
tools = tools.Tools()


class AppendFb:
    """ Visual return from append.py. """

    def show_old_product(self, list_old_product):
        """ Show products already saved in database. """
        for req in list_old_product:
            print("Existe déjà, Produit:", req[0], "| Code-barre:", req[1])

    def show_product(self, list_product):
        """ Show the products save to database. """
        for req in list_product:
            print("Product:", req[0], "Store:", req[1])

    def show_error(self, list_error):
        """ Show error from saving. """
        for req in list_error:
            print("Erreur sur:", req[0], req[1])

    def download_data(self):
        """ Save Api data to local database. """
        print("Mise à jour des produits en cours...")
        error = api.save_data()
        self.show_error(error[0])
        self.show_old_product(error[1])

    def start_append(self):
        """ Ask to user if he wants to save new products. """
        check_data = api.check_data()
        if check_data == 1:
            # download data
            self.download_data()
        else:
            print("Souhaitez-vous mettre à jour les articles?")
            maj_user = int(tools.check_value('Oui = 1, Non = 2', 1, 2))
            if maj_user == 1:
                self.download_data()
            else:
                pass
