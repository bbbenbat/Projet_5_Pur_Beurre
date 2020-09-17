# !/usr/bin/env python
# -*- coding: utf-8 -*-
from peewee import *
import tools


database = tools.pwd()
# Database is the Mysql connector to Pur Beurre database.
# pwd function is used to secure the Mysql password of DB

class UnknownField(object):
    def __init__(self, *_, **__): pass


class BaseModel(Model):
    class Meta:
        database = database


class Category(BaseModel):
    name = CharField(null=True, unique=True)

    class Meta:
        table_name = 'category'


class Product(BaseModel):
    barcode = CharField(null=True, unique=False)
    id_category = ForeignKeyField(column_name='id_category', field='id', model=Category, null=True)
    ingredient = CharField(null=True)
    name = CharField(null=True)
    nutriscore = CharField(null=True)
    url = CharField(null=True)
    categories_hierarchy = CharField(null=False)

    class Meta:
        table_name = 'product'


class Store(BaseModel):
    name = CharField(null=True, unique=True)

    class Meta:
        table_name = 'store'


class ProductStore(BaseModel):
    product = ForeignKeyField(column_name='product_id', field='id', model=Product)
    store = ForeignKeyField(column_name='store_id', field='id', model=Store)

    class Meta:
        table_name = 'product_store'
        indexes = (
            (('product', 'store'), True),
        )
        # primary_key = CompositeKey('product', 'store')


class Research(BaseModel):
    date = DateTimeField(null=True)
    id_product = ForeignKeyField(backref='product_id_product_set', column_name='id_product', field='id', model=Product,
                                 null=True)
    id_product_best = IntegerField(null=True)

    class Meta:
        table_name = 'research'
