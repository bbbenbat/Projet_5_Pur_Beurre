# !/usr/bin/env python
# -*- coding: utf-8 -*-
import mysql.connector
import sys



def connect():
    """  """
    global connection, curs
    connection = mysql.connector.connect(
        host="127.0.0.1",
        user="ocr",
        password="Python2020",
        database="PUR_BEURRE"
    )
    curs = connection.cursor()
    return connection, curs

    # """ This class sends the data to the Product Table """
def ImportBdd(req):
        """ check internet connection """
        try:
            connect()
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
            print("Attention : Veuillez vérifier que vous avez bien une connexion serveur!")
        # Check they are not already saved in database"""

def IdCategory(cat):
    """ IdCategory gives the ID number of Cat.
    Cat is the name Category"""
    connect()
    # curs.execute("SELECT id FROM Category WHERE name = '"+ cat +"'")
    curs.execute("SELECT id FROM Category WHERE name = %s", (cat,))
    # add the result to a list
    id_cat = curs.fetchone()
    # select the first value
    numCat = id_cat[0]
    return numCat
    # validate the transaction
    connection.commit()
    connection.close()

def ListProd(x):
    """List of products regarding user selection"""
    connect()
    curs = connection.cursor()
    curs.execute("SELECT id, name FROM Product WHERE id_category = %s", (x,))
    sel_prod = curs.fetchall()
    # sel_prod = sorted(sel_prod, key=lambda t: t[0])
    for row in sel_prod:
        print(row[0], "|", row[1])

"""
def ImportTableTempo(req):
#     This class sends the data to the Tempo Table 
    # check internet connection
    try:
        connect()
        curs = connection.cursor()
        # check if error
        # Clean the table for new download
        curs.execute("DELETE FROM Tempo")
        curs.execute("ALTER TABLE Tempo AUTO_INCREMENT = 0")
        # SQL request with all columns from Product table
        sql = "INSERT INTO Tempo (name, nutriscore, url, barcode, store, description, id_category) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        # execute the SQL request
        curs.executemany(sql, req)
        # validate the transaction
        connection.commit()
        print("Les données ont bien été enregistrés!")
        connection.close()
    except:
        print("Attention : Veuillez vérifier que vous avez bien une connexion serveur!")
    # Check they are not already saved in database
"""


def Store():
    """Insert Store name in Store table and completing the data in Product_store table"""


def ImportStore(req):
    """ This class sends the data to the Tempo Table """
    # check internet connection

    connect()
    curs = connection.cursor()
    # check if error
    # Clean the table for new download
    # curs.execute("DELETE FROM Store")
    # curs.execute("ALTER TABLE Store AUTO_INCREMENT = 0")
    # SQL request with all columns from Product table
    print(req, "***")
    for sto in req:
        try:
            # execute the SQL request
            curs.execute("INSERT INTO Store (name) VALUES (%s)", (sto,))
            # validate the transaction
            connection.commit()
            print("Les magasins ont bien été enregistrés!")
        except:
            pass
    connection.close()





def ListCat():
    """List of categories. Gives the id and names of Category table. """
    connect()
    curs = connection.cursor()
    # execute Sql request to list the id and names
    curs.execute("SELECT id, name FROM Category")
    all_cat = curs.fetchall()
    all_cat = sorted(all_cat, key=lambda t: t[0])
    for row in all_cat:
        print(f"ID = {row[0]} | Catégorie = {row[1]}")







# ProProd(1,1)
