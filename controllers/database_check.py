# !/usr/bin/env python
# -*- coding: utf-8 -*-
""" This module contains a class to check if the database, tables exist
 and can create the database. """

import mysql.connector
from peewee import MySQLDatabase


class CheckDatabase:
    """ This class checks if the database is available. """

    def create_db(self, req):
        """ If bdd not created = 0, bdd created = 1,
        bdd already exist = 2. """
        try:
            self.__db_connection = mysql.connector.connect(
                host="localhost", user="ocr", password=req)
            self.__db_cursor = self.__db_connection.cursor()
            try:
                self.__db_cursor.execute("CREATE DATABASE "
                                         " PUR_BEURRE CHARACTER SET 'utf8mb4';")
                db = 1
            except:
                db = 2
            return db
        except:
            db = 0
        return db

    def peew_connection_db(self, req):
        """ Check with peewee module if the database connection is established """
        database = MySQLDatabase('PUR_BEURRE',
                                 **{'charset': 'utf8', 'sql_mode':
                                     'PIPES_AS_CONCAT', 'use_unicode': True,
                                    'user': 'ocr',
                                    'password': req})
        database.connect()
        return database
