# PUR BEURRE  APPLICATION

Application created to find the products with the best nutriscore.

## Getting Started

These instructions will get you to use the application on your local machine

### Prerequisites

Your local machine must have a mysql server installed with a database :
name : pur_beurre
user : ocr
password : As you want(asked at start application)
rules user : all privileges on this database

```
CREATE DATABASE IF NOT EXISTS PUR_BEURRE
CHARACTER SET 'utf8mb4';
CREATE USER 'ocr'@'localhost' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON pur_beurre. * TO 'ocr'@'localhost';
```
Install Python version 3.7, with the following modules:

mysql-client 0.0.1 ,
mysql-connector 2.2.9 ,
mysql-connector-async-dd 2.0.2 ,
mysql-connector-python 8.0.21 ,
mysql-connector-python-dd 2.0.2 ,
mysqldbda 1.0.2 ,
peewee 3.13.3 ,
peewee-async 0.7.0 ,
requests 2.24.0 ,
PyMySQL 0.10.0 

### Installing

Save the Pur_Beurre folder on your local machine (containing the mysql server).
Check that the folder contains 7 files:
- orm_data.py
- orm_request.py
- API_connection.py
- console.py
- start_init.py
- tools.py
- subcategories.json

Launch the 'start_init.py' file to install the tables and create the sub-categories in the Pur_Beurre database.

```
> python start_init.py
```
Enter the password for the user 'ocr'.
```
> python start_init.py
Veuillez saisir le mot de passe de connexion:
```

At the first question, type 1 to create the tables.
For the second question, type 1 to save the sub-categories.

Next, enter the page number you want to download from the OpenFoodFacts API.
Then enter the number of products you want for each sub-category.

Let the program download the data and save it to the local database.
You can see the number of products registered on the last execution line.
```
product 552 store : SELECT `t1`.`id`, `t1`.`name` FROM `store` AS `t1` WHERE (`t1`.`name` = 'coop')
product 554 store : SELECT `t1`.`id`, `t1`.`name` FROM `store` AS `t1` WHERE (`t1`.`name` = 'leclerc')
product 555 store : SELECT `t1`.`id`, `t1`.`name` FROM `store` AS `t1` WHERE (`t1`.`name` = 'monoprix')
>
```
You can add new products by launching the script and then entering another page.

You can add benchmark products (the subcategories) by editing the subcategories.json file and then relaunching the script.
Then select 2 for the first question, then type 1 for the second question to update the reference products (in subcategorie table).
>Warning: The first word of each sub-category is used to group them into categories. Please follow this methodology.

## How to use

Launch the 'console.py' file to start the program.

```
> python console.py
```
Enter the password for the user 'ocr'.
```
> python console.py
Veuillez saisir le mot de passe de connexion:
```
Type 1 to search for a substitute product or type 2 to see the selections you have saved.
```
Bienvenue sur l'application PurBeurre!
==============================
= Que souhaitez-vous faire ? =
==============================
Avoir un produit de remplacement plus sain : tapez 1
Voir mon historique de recherche : tape 2
```

Each manipulation being well explained, there is no need to explain in more detail how the program works.

## Built With

* [OpenFoodFacts](https://wiki.openfoodfacts.org/) - The web API used

## Contributing

Please go [CONTRIBUTING.md](https://github.com/bbbenbat/Projet_5_Pur_Beurre/pulls) for submitting pull requests to us.

## Versioning

Version 0.1

## Authors

* **Ben Bessayah** - *Student* - [bbbenbat](https://github.com/bbbenbat)




