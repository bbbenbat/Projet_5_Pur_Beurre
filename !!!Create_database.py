# !/usr/bin/env python
# -*- coding: utf-8 -*-
import mysql.connector
import SQL_connection

SQL = SQL_connection.Connection()


a = SQL.curs._execute_iter("""

DROP TABLE IF EXISTS Product_store;
DROP TABLE IF EXISTS Product_description;
DROP TABLE IF EXISTS Store;
DROP TABLE IF EXISTS Description;
DROP TABLE IF EXISTS Consultation;
DROP TABLE IF EXISTS Product;
DROP TABLE IF EXISTS Subcategory;

# Local database creation
CREATE DATABASE IF NOT EXISTS PUR_BEURRE
CHARACTER SET 'utf8mb4';

USE PUR_BEURRE;

# Subcategory table creation
# description saves Open Food Facts category of the products
CREATE TABLE  IF NOT EXISTS Subcategory (
		id SMALLINT UNSIGNED AUTO_INCREMENT NOT NULL,
    	name VARCHAR(20) UNIQUE,
    	PRIMARY KEY (id)
)
ENGINE=InnoDB;


# Product table creation
CREATE TABLE IF NOT EXISTS Product (
	id SMALLINT UNSIGNED AUTO_INCREMENT NOT NULL,
    	name VARCHAR(100),
    	nutriscore VARCHAR(1),
    	url VARCHAR(300),
    	barcode VARCHAR(20) UNIQUE,
    	id_category SMALLINT UNSIGNED,
    	PRIMARY KEY (id),
        CONSTRAINT fk_category_id
		FOREIGN KEY (id_category)
        	REFERENCES Subcategory(id)
)
ENGINE=InnoDB;  


# Consultation table creation for the user search history
CREATE TABLE IF NOT EXISTS Consultation (
		id SMALLINT UNSIGNED AUTO_INCREMENT NOT NULL,
    	date DATETIME,
    	id_subcategory SMALLINT UNSIGNED,
    	best_product SMALLINT UNSIGNED,
    	PRIMARY KEY(id),
    	CONSTRAINT fk_product_id
		FOREIGN KEY (id_subcategory)
        	REFERENCES Product(id),
		CONSTRAINT fk_best_product
		FOREIGN KEY (id_subcategory)
        	REFERENCES Product(id)
)
ENGINE=InnoDB;

# Table for the OpenFoodFacts category of the product (for the description)
CREATE TABLE IF NOT EXISTS Description (
		id SMALLINT UNSIGNED AUTO_INCREMENT NOT NULL,
    	name VARCHAR(50) UNIQUE,
    	PRIMARY KEY (id)
)
ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS Store (
		id SMALLINT UNSIGNED AUTO_INCREMENT NOT NULL,
    	name VARCHAR(50) UNIQUE,
    	PRIMARY KEY (id)
)
ENGINE=InnoDB;

# Many to many table between Product and Description
CREATE TABLE IF NOT EXISTS Product_description (
		product_id SMALLINT UNSIGNED NOT NULL,
		description_id SMALLINT UNSIGNED NOT NULL,
		PRIMARY KEY (product_id, description_id),
		FOREIGN KEY (product_id) 
			REFERENCES Product(id) 
            ON DELETE RESTRICT ON UPDATE CASCADE,
		FOREIGN KEY (description_id) 
			REFERENCES description(id) 
            ON DELETE RESTRICT ON UPDATE CASCADE
)
ENGINE=InnoDB;

# Many to many table between Product and Store
CREATE TABLE IF NOT EXISTS Product_store (
		product_id SMALLINT UNSIGNED NOT NULL,
		store_id SMALLINT UNSIGNED NOT NULL,
		PRIMARY KEY (product_id, store_id),
		FOREIGN KEY (product_id) 
			REFERENCES Product(id) 
            ON DELETE RESTRICT ON UPDATE CASCADE,
		FOREIGN KEY (store_id) 
			REFERENCES Store(id) 
            ON DELETE RESTRICT ON UPDATE CASCADE
)
ENGINE=InnoDB;

# Name category insertion into table
INSERT INTO Subcategory (name)
VALUES 	('pizza'),
		('pain-de-mie'),
        ('saucisson'),
        ('quiche');""")

SQL.connection.commit()
SQL.connection.close()

