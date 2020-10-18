# !/usr/bin/env python
# -*- coding: utf-8 -*-
from peewee import *

from misc import tools

# Database is the Mysql connector to Pur Beurre database.
# pwd function is used to secure the Mysql password of DB
database = tools.pwd()


class UnknownField(object):
    def __init__(self, *_, **__): pass


class BaseModel(Model):
    class Meta:
        database = database


