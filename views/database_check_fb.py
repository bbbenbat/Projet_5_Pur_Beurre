# !/usr/bin/env python
# -*- coding: utf-8 -*-
""" This module contains the class DatabaseCheckFb who manages the views
from database_check module."""

from controllers import database_check

database_check = database_check.CheckDatabase()


class DatabaseCheckFb:

    def check_connect(self, req):
        try:
            db = database_check.check_connection_db(req)
            return db
        except:
            print("Mot de passe incorrect!\n")

    def pwd(self):
        """ To have the password and use it with check_connection function.
         loop if the password is not good. """
        passwo = 0
        while passwo == 0:
            passwo = input("Veuillez saisir le mot de passe de connexion:\n")
            check = self.check_connect(passwo)
            if check is None:
                passwo = 0
            else:
                return check

    def check_database(self):
        check_create_db = database_check.check_datab()
        if check_create_db == 1:
            print("Création de la base de données...")
            database_check.create_db()
        database = self.pwd()
        return database
