# !/usr/bin/env python
# -*- coding: utf-8 -*-
""" This module contains a class to check if the database, tables exist
 and can create the database. """

import mysql.connector

from peewee import MySQLDatabase


class CheckDatabase:
    """  """

    def __init__(self):
        self.__db_connection = mysql.connector.connect(
            host="localhost", user="ocr", password="Python2020")
        self.__db_cursor = self.__db_connection.cursor()

    def create_db(self):
        self.__db_cursor.execute("CREATE DATABASE IF NOT EXISTS"
                                 " PUR_BEURRE CHARACTER SET 'utf8mb4';")

    def check_datab(self):
        try:
            self.connector = mysql.connector.connect(
                user='ocr', password='Python2020',
                host='localhost',
                database='PUR_BEURRE')
        except:
            self.create_db()

    def check_connection_db(self, req):
        """ Check if the database connection is established """
        database = MySQLDatabase('PUR_BEURRE',
                                 **{'charset': 'utf8', 'sql_mode':
                                     'PIPES_AS_CONCAT', 'use_unicode': True,
                                    'user': 'ocr',
                                    'password': req})
        database.connect()
        return database

    def check_table_exists(self):
        self.check_datab()
        table_name = 'product'
        dbcur = self.connector.cursor()
        dbcur.execute(f"""
            SELECT COUNT(*)
            FROM information_schema.tables
            WHERE table_name = '{table_name}'
            """)
        if dbcur.fetchone()[0] == 1:
            dbcur.close()
            return True
        else:
            dbcur.close()
            return False
