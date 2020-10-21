# !/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import os.path
import time

from peewee import MySQLDatabase


def check_value(name, min_int, max_int):
    """ Check if the values are correct """
    while True:
        numb = input(f"-- {name} : Entrez une valeur comprise "
                     f"entre {min_int} et {max_int} : ")
        try:
            check = int(numb)
            if min_int <= check <= max_int:
                break
        except ValueError:
            pass
    return check


def check_list_value(name, list_int):
    """ Check if the values are correct """
    while True:
        numb = input(f"-- {name} : Entrez une de ces valeurs : {list_int} : ")
        try:
            check = int(numb)
            if check in list_int:
                break
        except ValueError:
            pass
    return check


def rp2cara(req, x, y, z):
    """ Replace 2 values by another one """
    cara_1 = x
    cara_2 = y
    repl_1 = z
    string = cara_1 + cara_2
    for carac in string:
        req = req.replace(carac, repl_1)
    return req


def splite_tuple_to_liste(x):
    """ create a liste with a tuple by split of x value for each ','"""
    list_s = (x.split(','))
    return list_s


def check_connection_db(req):
    """ Check if the database connection is established """
    try:
        database = MySQLDatabase('PUR_BEURRE',
                                 **{'charset': 'utf8', 'sql_mode':
                                     'PIPES_AS_CONCAT', 'use_unicode': True,
                                    'user': 'ocr',
                                    'password': req})
        database.connect()
        return database
    except:
        print("Mot de passe incorrect!\n")


def pwd():
    """ To have the password and use it with check_connection function.
     loop if the password is not good. """
    passwo = 0
    while passwo == 0:
        passwo = input("Veuillez saisir le mot de passe de connexion:\n")
        check = check_connection_db(passwo)
        if check is None:
            passwo = 0
        else:
            return check


def check_list(list_one, list_two):
    """ Check that all values of list_one are as keys of list_two,
    else the key is created in list_two.*
    Return the list_two with all keys."""
    list_one_p = list_one['products']
    new_list = []
    # print("LIST_ONE_p : ", list_one_p)
    # print("LIST_TWO", list_two)
    for row in list_one_p:
        # print("ROW", row)
        for rows in list_two:
            if rows in row:
                # print("Déjà présent!")
                pass
            else:
                # print("Rajouter \n", rows)
                row.update({rows: ''})
        posi = list_one_p.index(row)
        list_one_p[posi] = row
        new_list.append(row)
    return list_one_p


def read_json(req):
    """ Return a list of values from req file """
    data_list = []
    with open(req) as json_data:
        data_dict = json.load(json_data)
    for value in data_dict.values():
        data_list.append(value)
    return data_list


def check_file(req, val1):
    """ Check if the file is accessible. """
    if os.path.isfile(req):
        val1
    else:
        print("Fichier \",req,\" absent."
              "Veuillez le placer dans le dossier.")
        time.sleep(5.0)
