# !/usr/bin/env python
# -*- coding: utf-8 -*-
""" This module create the peewee connection to the database. """

from peewee import Model

from views import database_check_fb

database_ck = database_check_fb.DatabaseCheckFb()
database = database_ck.check_database()


# Database is the Mysql connector to Pur Beurre database.
# pwd function is used to secure the Mysql password of DB


class UnknownField(object):
    def __init__(self, *_, **__): pass


class BaseModel(Model):
    class Meta:
        database = database
