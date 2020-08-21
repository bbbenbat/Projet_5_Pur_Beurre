# !/usr/bin/env python
# -*- coding: utf-8 -*-
import mysql.connector
import sys

# class SQL:
# """ This class sends the data to the Product Table """


connection = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="Saitam@54",
    database="PUR_BEURRE"
)


def ImportBdd(req):
    connection = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="Saitam@54",
        database="PUR_BEURRE"
    )
    curs = connection.cursor()
    # SQL request
    sql = "INSERT INTO Product (name, nutriscore, url, barcode, store, description) VALUES (%s, %s, %s, %s, %s, %s)"
    # execute the SQL request"""
    curs.executemany(sql, req)
    # validate the transaction
    connection.commit()
    print(curs.rowcount, "ligne insérée.")
    connection.close()


# values = [("Tutuuureguuavfdvdazdeza", "a", "azaefdgrt", "123541556", "auchan"),
#             ("azfrgbrzefbdfree", "b", "zerbdfgbgrtegr", "1213485667", "auchan")]

# ImportBdd(values)

connection.close()
