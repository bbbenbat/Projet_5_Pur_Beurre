# !/usr/bin/env python
# -*- coding: utf-8 -*-

from controllers import orm

orm_imp = orm.Orm()


class Append_fb:
    """  """

    def show_old_product(self, list_old_product):
        """  """
        for req in list_old_product:
            print("Existe déjà, PRODUIT :", req[0])

    def show_product(self, list_product):
        """  """
        for req in list_product:
            print("Product:", req[0], "Store:", req[1])

    def show_error(self, list_error):
        """  """
        for req in list_error:
            print("Erreur sur:", req[0], req[1])
