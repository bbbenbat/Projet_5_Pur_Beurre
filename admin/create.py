# !/usr/bin/env python
# -*- coding: utf-8 -*-

from models import orm_data as od, subcategory as sc, \
    product as pr, product_store as ps, research as rs, store as st


class CreateDbb:
    """ Start this class for the first installation or re-installation.
    Delete tables (if exist) and create it."""

    @property
    def __delete_dbb(self):
        od.database.drop_tables([sc.Subcategory, pr.Product,
                                 rs.Research, st.Store, ps.ProductStore])
    @property
    def __create_dbb(self):
        od.database.create_tables([sc.Subcategory, pr.Product,
                                   rs.Research, st.Store, ps.ProductStore])

    def exec_req(self):
        self.__delete_dbb
        self.__create_dbb


if __name__ == '__main__':
    create_dbb = CreateDbb()
    create_dbb.exec_req()

