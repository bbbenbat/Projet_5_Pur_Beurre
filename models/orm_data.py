# !/usr/bin/env python
# -*- coding: utf-8 -*-
""" This module create the peewee connection to the database.
pwd() method is used to secure the Mysql password of DB"""

from peewee import Model

from views import database_check_fb

database_ck = database_check_fb.DatabaseCheckFb()
database = database_ck.pwd()


class UnknownField(object):
    def __init__(self, *_, **__): pass


class BaseModel(Model):
    class Meta:
        database = database
