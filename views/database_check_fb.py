# !/usr/bin/env python
# -*- coding: utf-8 -*-
""" This module contains the class DatabaseCheckFb who manages the views
from database_check module."""


from controllers import database_check

database_check = database_check.CheckDatabase()


class DatabaseCheckFb:
    """ This class manages the password of the database connection. """

    def pwd(self):
        """ To have the password and use it with check_connection function.
         loop if the password is not good. """
        check = 0
        while check == 0:
            pwd = input("Veuillez saisir le mot de passe de connexion:\n")
            check = database_check.create_db(pwd)
            if check == 1:
                print("Création de la base de données...")
            if check != 0:
                database = database_check.peew_connection_db(pwd)
                return database
