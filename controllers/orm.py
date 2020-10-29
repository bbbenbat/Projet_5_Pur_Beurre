# !/usr/bin/env python
# -*- coding: utf-8 -*-
""" This module contains a class who manages all Sql request via the
 peewee module. """

from datetime import datetime

from peewee import fn, JOIN

from models.product import Product
from models.product_store import ProductStore
from models.research import Research
from models.store import Store
from models.subcategory import Subcategory as sc


class Orm:
    """ All SQL requests via Peewee ORM """

    def subcat(self, subcat_file):
        """ Update categories from settings.json file, in Subcategory table.
        Used in append."""
        # Search the last id
        for req in subcat_file:
            try:
                # the next id from Subcategory table
                result = (sc.select(fn.MAX(sc.id)).scalar()) + 1
                try:
                    # sc.insert(id=last_id, name=req).execute()
                    sc.insert(id=result, name=req).execute()
                except:
                    pass
            except:
                try:
                    # sc.insert(id=last_id, name=req).execute()
                    sc.insert(name=req).execute()
                except:
                    pass

    def name_subcategory(self):
        """ Give the name of each category of Subcategory table.
        Used in append."""
        name_cat = sc.select()
        return name_cat

    def save_data(self, list):
        """ Check and save API's data to the database."""
        list_old_product = []
        list_product = []
        list_error = []
        for line in list:
            # if product is not in the table (check with name and barcode)
            query_pr = Product.select().where(Product.name == line[0],
                                              Product.barcode == line[3])
            if query_pr.exists():
                list_old_product.append([line[0], line[3]])
                pass
            else:  # save product
                exe_pr = Product.insert(name=line[0], nutriscore=line[1],
                                        url=line[2],
                                        barcode=line[3], ingredient=line[4],
                                        id_category=line[5],
                                        categories_hierarchy=line[7])
                id_pr = exe_pr.execute()  # save Product table id in id_pr
                check_st = line[6]
                if check_st is not None:  # if there is a store with product
                    for sto in check_st:  # check if store is in Store table
                        id_st = Store.select().where(Store.name == sto)
                        if id_st.exists():
                            pass
                        else:
                            Store.insert(name=sto).execute()  # create store
                            id_st = Store.select().where(Store.name == sto)
                        list_product.append([id_pr, id_st])
                        try:  # save relation between product & store
                            ProductStore.insert(product_id=id_pr,
                                                store_id=id_st).execute()
                        except:
                            list_error.append([id_pr, id_st])
        return list_old_product, list_product, list_error

    def select_category(self):
        """ Give the categories regarding the subcategories of the database.
        The categories are the first word of the subcategories. """
        select_cat = []
        s_cat = sc.select()
        for cat in s_cat:
            cate = cat.name.split()[:1]
            if cate[0] in select_cat:
                pass
            else:
                select_cat.append(cate[0])
        return select_cat

    def select_sub_category(self, req):
        """ Give the subcategories regarding the category selected(req).
        Used in console."""
        ssub_cat = sc.select().where(sc.name.iregexp(req))
        return ssub_cat

    def list_prod(self, req):
        """ Request for the bests product, selected by nutriscore value. """
        produ = Product.select().where(Product.id_category == req). \
            order_by(Product.nutriscore.asc())
        return produ

    def find_store(self, req):
        """ Show all stores of the product (req).
        Used in list_prod()."""
        list_store = []
        query = (ProductStore
                 .select()
                 .join(Product, JOIN.INNER)
                 .switch(ProductStore)
                 .join(Store, JOIN.INNER)
                 .where(ProductStore.product == req))
        for row in query:
            list_store.append(row.store.name)
        # Return list of values without []
        return str(list_store).strip('[]')

    def save_user_select(self, req, req1, req2):
        """ req is the dict of best products
        req1 is the subcategory selected by user
        req2 is the product selected by user. """
        Research.insert(id_product=req[req2],
                        id_subcategory=req1, date=datetime.now()).execute()

    def read_research(self):
        """ Show the research saved.
        Used in console."""
        list_research = []
        # Use the many to many relation
        for row in Research \
                .select(Research.id_subcategory, Research.id_product,
                        Product.name.alias('product'),
                        sc.name.alias('subcat'), Product.nutriscore,
                        Product.ingredient, Product.url,
                        Research.date) \
                .join(Product) \
                .switch(Research) \
                .join(sc) \
                .order_by(Research.date) \
                .dicts():
            list_research.append(row)
        return list_research
