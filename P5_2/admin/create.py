# !/usr/bin/env python
# -*- coding: utf-8 -*-

from models import orm_data as od, subcategory as sc, product as pr, product_store as ps, research as rs, store as st


class CreateDbb:
    def delete_dbb(self):
        od.database.drop_tables([sc.Subcategory, pr.Product, rs.Research, st.Store, ps.ProductStore])

    def create_dbb(self):
        od.database.create_tables([sc.Subcategory, pr.Product, rs.Research, st.Store, ps.ProductStore])


if __name__ == '__main__':
    create_dbb = CreateDbb()
    create_dbb.delete_dbb()
    create_dbb.create_dbb()
