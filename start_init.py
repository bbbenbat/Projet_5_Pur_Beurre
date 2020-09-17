# !/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import orm_request as ORMR
import orm_data as ORMD
import API_connection as APIC
import tools

def main():
    # loop for each category
    ORMR.create_table()
    ORMR.create_cat()
    for cate in APIC.list_subcategories():
        # to find the ID of the category in Category table
        id_category = ORMR.id_category(cate)
        # we call the function api_category for the API connection
        data = APIC.api_category(cate)
        # we put the dictionary to the list
        ApilistProduct = data['products']
        # we create a global list with all dictionaries
        for row in ApilistProduct:
            row['id_category'] = id_category
            APIC.listAllProduct.append(row)
        # print(listAllProduct)
    # DescStore(listAllProduct)
    ##SQL_CONNECT.ImportStore(descStore)
    # Call the function to create the list for the SQL integration
    all_product = APIC.ReqSql(APIC.listAllProduct)
    # Call the function to save data to the database in the table (TProduct)
    #ORMR.import_bdd(all_product)
    ORMR.check_data(all_product)
    ##IMP_BDD(aze)


if __name__ == '__main__':
    main()