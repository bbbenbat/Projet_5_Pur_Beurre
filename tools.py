# !/usr/bin/env python
# -*- coding: utf-8 -*-
import getpass
from peewee import *


def ask_integer(name, max_int, min_int=0):
    assert type(name) == str
    assert type(min_int) == int
    assert type(max_int) == int
    while True:
        numb = input(f"Entrez une valeur de {name.lower()} comprise entre {min_int} et {max_int} : ")
        try:
            check = int(numb)
            if check > max_int or check < min_int:
                raise ValueError
            break
        except ValueError:
            pass
    return numb


def rp2cara(req, x, y, z):
    cara_1 = x
    cara_2 = y
    repl_1 = z
    string = cara_1 + cara_2
    for carac in string:
        req = req.replace(carac, repl_1)
    return req


def splite_tuple_to_liste(x):
    # create a liste with a tuple by store's categories
    list_s = []
    list_s = (x.split(','))
    # print("***-***", descStore)
    return list_s


def check_connection_db(req):
    try:
        database = MySQLDatabase('PUR_BEURRE',
                              **{'charset': 'utf8', 'sql_mode': 'PIPES_AS_CONCAT', 'use_unicode': True,
                                 'user': 'ocr',
                                 'password': req})
        database.connect()
        return database
    except:
        print("Mot de passe incorrect!\n")


def pwd():
    """ To have the password of Pur Beurre database. """
    passwo = 0
    while passwo == 0:
        passwo = input("Veuillez saisir le mot de passe de connexion:\n")
        check = check_connection_db(passwo)
        if check is None:
            passwo = 0
        else:
            return check



#pwd()
