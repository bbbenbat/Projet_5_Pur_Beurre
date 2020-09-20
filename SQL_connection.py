# !/usr/bin/env python
# -*- coding: utf-8 -*-
import mysql.connector


class Connection:

    def __init__(self):
        """" """
        self.connection = mysql.connector.connect(
            host="127.0.0.1",
            user="ocr",
            password="Python2020",
            database="PUR_BEURRE"
        )
        self.curs = self.connection.cursor()
        self.list_store = []
        self.listSQL = []

    # change the order of values and save in a list for the SQL upload
    def ReqSql(self, x):
        for line in x:
            tupleSql = (
                line["product_name"], line["nutriscore_grade"], line["url"], line["code"], line["stores"],
                line["categories"],
                line["id_category"])
            self.listSQL.append(tupleSql)
        # print(listSQl)
        return self.listSQL


    def IdCategory(self, cat):
        """ IdCategory gives the ID number of Cat.
        Cat is the name in Subcategory table"""
        # curs.execute("SELECT id FROM Subcategory WHERE name = '"+ cat +"'")
        self.curs.execute("SELECT id FROM Subcategory WHERE name = %s", (cat,))
        # add the result to a list
        id_cat = self.curs.fetchone()
        # select the first value
        numCat = id_cat[0]
        return numCat
        # validate the transaction
        self.connection.commit()
        self.connection.close()

    def ImportBdd(self, req):
        """ This class sends the data to the Product Table """
        # check if error
        # Clean Product table before integration
        print(">>>***>>>", req)
        self.curs.execute("DELETE FROM Product")
        self.curs.execute("ALTER TABLE Product AUTO_INCREMENT = 0")
        # SQL request with all columns from Product table
        sql = "INSERT INTO Product (name, nutriscore, url, barcode, id_category) VALUES (%s, %s, %s, %s, %s)"
        # execute the SQL request
        self.curs.executemany(sql, req)
        # validate the transaction
        self.connection.commit()
        print("Les articles ont bien été enregistrés!")
        self.connection.close()

    def ImportBdd_old(self, req):
        """ This class sends the data to the Product Table """
        # check if error
        # Clean Product table before integration
        print(">>>***>>>", req)
        self.curs.execute("DELETE FROM Product")
        self.curs.execute("ALTER TABLE Product AUTO_INCREMENT = 0")
        # SQL request with all columns from Product table
        sql = "INSERT INTO Product (name, nutriscore, url, barcode, store, description, id_category) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        # execute the SQL request
        self.curs.executemany(sql, req)
        # validate the transaction
        self.connection.commit()
        print("Les articles ont bien été enregistrés!")
        self.connection.close()

    def ListProd(self, x):
        """List of products regarding user selection"""
        self.curs.execute("SELECT id, name FROM Product WHERE id_category = %s", (x,))
        sel_prod = self.curs.fetchall()
        # sel_prod = sorted(sel_prod, key=lambda t: t[0])
        for row in sel_prod:
            print(row[0], "|", row[1])

    def ImportStore(self, req):
        print(">>> >>>", req)
        """ This class creates stores in Store Table """
        for all_store in req:
            for stor in all_store:
                # clean the data before integration
                sto = str.lower(str.strip(stor))
                self.curs.execute("SELECT name FROM Store WHERE name = %s", (sto,))
                name = self.curs.fetchone()
                if not (name) and sto not in self.list_store and sto != "":
                    self.list_store.append(sto)
        for good_store in self.list_store:
            self.curs.execute("INSERT INTO Store (name) VALUES (%s)", (good_store,))
        self.connection.commit()

    #
    def dic_store(self, req):
        x = 1
        stores_all = []
        """self.curs.execute("SELECT id, name FROM Store")
        store_table = self.curs.fetchall()
        for row in req:
            # row est la liste contenant les magasinse numero du produit
            print(row)"""
        print("req : ", req)
        self.curs.execute("SELECT name, store FROM Product")
        aze = self.curs.fetchall()
        # je parcours la table Product
        """for row in aze:
            # je cloisonne les magasins
            azer = row[1].split(',')
            for rows in azer:
                # on recupere chaque magasin de la table
                store = str.lower(str.strip(rows))
                # req[x] correspond aux stores de la liste
                # store correspond aux stores de la table Store
                # x correspond correspond à la position dans la liste
                sto = str.lower(str.strip(str(req[x])))
                print("num list:",x," | magasin:", store, " | liste :", sto)
                print(self)
                print(store in sto)
            x += 1"""
            #print("azer : ",azer)
        # print(row[0], "|", row[1])
        # self.connection.commit()

    #

    def ListCat(self):
        """List of categories. Gives the id and names of Subcategory table. """
        # execute Sql request to list the id and names
        self.curs.execute("SELECT id, name FROM Subcategory")
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

# Connection.ImportBdd()

# ProProd(1,1)
# a = Connection()
# a.ImportStore('carr')
