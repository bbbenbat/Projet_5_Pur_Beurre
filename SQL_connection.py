# !/usr/bin/env python
# -*- coding: utf-8 -*-
import mysql.connector
import sys


# class SQL:
# """ This class sends the data to the Product Table """


def ImportBdd(req):
    # check internet connection
    try:
        connection = mysql.connector.connect(
            host="127.0.0.1",
            user="ocr",
            password="Python2020",
            database="PUR_BEURRE"
        )
        curs = connection.cursor()
        # check if error
        try:
            # SQL request with all columns from Product table
            sql = "INSERT INTO Product (name, nutriscore, url, barcode, store, description, id_category) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            # execute the SQL request
            curs.executemany(sql, req)
            # validate the transaction
            connection.commit()
            print("Les articles ont bien été enregistrés!")
        except Exception as exc:
            if isinstance(exc, mysql.connector.errors.IntegrityError):
                print("Attention : articles déjà enregistrés. \nVeuillez sélectionner une autre page!")
            else:
                print("Erreur lors du traitement, veuillez recommencer.")
        connection.close()
    except:
        print("Attention : Veuillez vérifier que vous avez bien une connexion internet!")
    # Check they are not already saved in database



def IdCategory(cat):
    # check internet connection
    try:
        connection = mysql.connector.connect(
            host="127.0.0.1",
            user="ocr",
            password="Python2020",
            database="PUR_BEURRE"
        )
        """ """
        curs = connection.cursor()
        # execute the SQL request
        curs.execute("SELECT id FROM Category WHERE name = '" + cat + "'")
        #
        # add the result to a list
        id_cat = curs.fetchone()
        # select the first value
        return id_cat[0]
        # validate the transaction
        connection.commit()
        connection.close()
    except:
        print("Attention : Veuillez vérifier que vous avez bien une connexion internet!")


