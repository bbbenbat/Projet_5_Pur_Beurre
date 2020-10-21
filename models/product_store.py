# !/usr/bin/env python
# -*- coding: utf-8 -*-
from peewee import *

from models import orm_data as od, product as pr, store as st
from misc import tools


class ProductStore(od.BaseModel):
    """ ProductStore table
    Many to many between Product and Store tables
    Columns : id, product, store"""
    product = ForeignKeyField(column_name='product_id', field='id', model=pr.Product)
    store = ForeignKeyField(column_name='store_id', field='id', model=st.Store)

    class Meta:
        table_name = 'product_store'
        indexes = (
            (('product', 'store'), True),
        )