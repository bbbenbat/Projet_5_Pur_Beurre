# !/usr/bin/env python
# -*- coding: utf-8 -*-
from peewee import *

from models import orm_data as od, subcategory as sc
from misc import tools


class Product(od.BaseModel):
    """ Product table
     Columns : id, barcode, categories_hierarchy, id_category, ingredient, name, nutriscore, url"""
    barcode = CharField(null=True)
    categories_hierarchy = CharField()
    id_category = ForeignKeyField(column_name='id_category', field='id', model=sc.Subcategory, null=True)
    ingredient = CharField(null=True)
    name = CharField(null=True)
    nutriscore = CharField(null=True)
    url = CharField(null=True)

    class Meta:
        table_name = 'product'
