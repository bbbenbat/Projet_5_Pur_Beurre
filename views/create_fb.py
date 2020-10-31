# !/usr/bin/env python
# -*- coding: utf-8 -*-
""" This module contains the class CreateFb who manages the views from create
 module."""

from admin import create

create_dbb = create.CreateTables()


class CreateFb:
    """ Visual return from create.py. """

    def start_create(self):
        """ Create the tables if not exist. """
        create_dbb.create_tables
