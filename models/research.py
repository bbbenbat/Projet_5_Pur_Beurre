# !/usr/bin/env python
# -*- coding: utf-8 -*-
from peewee import DateTimeField, ForeignKeyField

from models import orm_data as od, subcategory as sc, product as pr


class Research(od.BaseModel):
    """ Research table
    Columns : id, id_subcategory, id_product"""
    date = DateTimeField(null=True)
    id_subcategory = ForeignKeyField(column_name='id_subcategory',
                                     field='id', model=sc.Subcategory,
                                     null=True)
    id_product = ForeignKeyField(column_name='id_product',
                                 field='id', model=pr.Product, null=True)

    class Meta:
        table_name = 'research'
