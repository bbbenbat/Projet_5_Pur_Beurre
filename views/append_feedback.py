# !/usr/bin/env python
# -*- coding: utf-8 -*-

from admin import append
from misc import tools

api = append.Api()


class Append_fb:
    """ Visual return from append.py. """

    def show_old_product(self, list_old_product):
        """ Show products already saved in database. """
        for req in list_old_product:
            print("Existe déjà, PRODUIT :", req[0])

    def show_product(self, list_product):
        """ Show the products save to database. """
        for req in list_product:
            print("Product:", req[0], "Store:", req[1])

    def show_error(self, list_error):
        """ Show error from saving. """
        for req in list_error:
            print("Erreur sur:", req[0], req[1])

    def start_append(self):
        """ Ask to user if he wants to save new products. """
        print("Souhaitez-vous mettre à jour les articles?")
        maj_user = int(tools.check_value('Oui = 1, Non = 2', 1, 2))
        if maj_user == 1:
            error = api.save_data()
            self.show_error(error[0])
            self.show_old_product(error[1])
        else:
            pass
