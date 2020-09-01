# !/usr/bin/env python
# -*- coding: utf-8 -*-
import mysql.connector
import sys


class Connection:

    def __init__(self):
        """" """
        self.connection = mysql.connector.connect(
            host="127.0.0.1",
            user = "ocr",
            password = "Python2020",
            database = "PUR_BEURRE"
        )
        self.curs = self.connection.cursor()
        self.list_store = []

    def IdCategory(self, cat):
        """ IdCategory gives the ID number of Cat.
        Cat is the name Category"""
        # curs.execute("SELECT id FROM Category WHERE name = '"+ cat +"'")
        self.curs.execute("SELECT id FROM Category WHERE name = %s", (cat,))
        # add the result to a list
        id_cat = self.curs.fetchone()
        # select the first value
        numCat = id_cat[0]
        return numCat
        # validate the transaction
        self.connection.commit()
        self.connection.close()

    # """ This class sends the data to the Product Table """
    def ImportBdd(self, req):
        # check if error
        #try:
        # SQL request with all columns from Product table
        self.curs.execute("DELETE FROM Product")
        self.curs.execute("ALTER TABLE Product AUTO_INCREMENT = 0")
        sql = "INSERT INTO Product (name, nutriscore, url, barcode, store, description, id_category) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        # execute the SQL request
        self.curs.executemany(sql, req)
        # validate the transaction
        self.connection.commit()
        print("Les articles ont bien été enregistrés!")
        #except Exception as exc:
            #if isinstance(exc, mysql.connector.errors.IntegrityError):
                #print("Attention : articles déjà enregistrés. \nVeuillez sélectionner une autre page!")
        self.connection.close()

    def ListProd(self, x):
        """List of products regarding user selection"""
        self.curs.execute("SELECT id, name FROM Product WHERE id_category = %s", (x,))
        sel_prod = self.curs.fetchall()
        # sel_prod = sorted(sel_prod, key=lambda t: t[0])
        for row in sel_prod:
            print(row[0], "|", row[1])

    def ImportStore(self, req):
        """ This class creates stores in Store Table """
        for all_store in req:
            for stor in all_store:
                # clean the data before integration
                sto = str.lower(str.strip(stor))
                self.curs.execute("SELECT name FROM Store WHERE name = %s", (sto,))
                name = self.curs.fetchone()
                if not(name) and sto not in self.list_store and sto != "":
                    print("il faut enregistrer")
                    print("variable = ",sto," | liste",self.list_store, "car :")
                    self.list_store.append(sto)
                else:
                    print("il ne faut pas enregistrer!")
                    print("nom store",name, "variable", sto)
        print(self.list_store)
        for good_store in self.list_store:
            print("//",good_store)
            self.curs.execute("INSERT INTO Store (name) VALUES (%s)", (good_store,))
        self.connection.commit()
        #print(">>> ",self.list_store)

    def ListCat(self):
        """List of categories. Gives the id and names of Category table. """
        # execute Sql request to list the id and names
        self.curs.execute("SELECT id, name FROM Category")
        all_cat = self.curs.fetchall()
        all_cat = sorted(all_cat, key=lambda t: t[0])
        for row in all_cat:
            print(f"ID = {row[0]} | Catégorie = {row[1]}")
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

#Connection.ImportBdd()

# ProProd(1,1)
#a = Connection()
#a.ImportStore('carr')