# !/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import orm_request as ORMR
import orm_data as ORMD
import API_connection as APIC
import tools


def main():
    page = ORMR.check_delete()
    for cate in APIC.list_subcategories():
        #print("!!!!! CATE", cate)
        # to find the ID of the category in Subcategory table
        id_category = ORMR.id_category(cate)
        # we call the function api_subcategory for the API connection
        data = APIC.api_subcategory(cate, page[0], page[1])
        # we create a global list with all dictionaries
        for row in data:
            row['id_category'] = id_category
            APIC.listAllProduct.append(row)
    # Call the function to create a list checked for the SQL integration
    all_product = APIC.ReqSql(APIC.listAllProduct)
    # Call the function to save data to the database in the table (TProduct)
    print(all_product)
    ORMR.save_data(all_product)


if __name__ == '__main__':
    main()
