# !/usr/bin/env python
# -*- coding: utf-8 -*-
""" This module contains the class CreateFb who manages the views from create
 module."""

from admin import create
from controllers import database_check

create_dbb = create.CreateTables()
database_check = database_check.CheckDatabase()


class CreateFb:
    """ Visual return from create.py. """

    def start_create(self):
        """ Ask to user if he wants to save new products. """

    check_table = database_check.check_table_exists()
    if check_table is False:
        print("Création des tables dans la base de données...")
        create_dbb.create_tables
