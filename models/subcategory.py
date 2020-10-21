# !/usr/bin/env python
# -*- coding: utf-8 -*-
from peewee import CharField

from models import orm_data as od


class Subcategory(od.BaseModel):
    """ Subcategory table
    Columns : id, name"""
    name = CharField(null=True, unique=True)

    class Meta:
        table_name = 'subcategory'
