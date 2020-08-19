# !/usr/bin/env python
# -*- coding: utf-8 -*-
import mysql.connector
import sys


class SQL:
    """ This class sends the data to database """


    connection = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="Saitam@54",
        database="PUR_BEURRE"
    )

curs = connection.cursor()
# SQL request
sql = "INSERT INTO Category (name, description) VALUES (%s, %s)"
# data for the request
value = ("Tutuuuuuaa", "21")
# execute the SQL request
curs.execute(sql, value)
# validate the transaction
connection.commit()

print(curs.rowcount, "ligne insérée.")

connection.close()
