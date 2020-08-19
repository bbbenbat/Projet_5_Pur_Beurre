# !/usr/bin/env python
# -*- coding: utf-8 -*-
import mysql.connector
import sys


#class SQL:
    #""" This class sends the data to the Product Table """


connection = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="Saitam@54",
    database="PUR_BEURRE"
)



curs = connection.cursor()
# SQL request
sql = "INSERT INTO Product (name, nutriscore, url, barcode, store) VALUES (%s, %s, %s, %s, %s)"
# data for the request
value = [("Tutuuuuuaa", "a","aze", "123456", "auchan"),
         ("aze","b","zer", "1234567", "auchan")]
# execute the SQL request
curs.executemany(sql, value)
# validate the transaction
connection.commit()
print(curs.rowcount, "ligne insérée.")
connection.close()
