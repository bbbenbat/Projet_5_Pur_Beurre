# PUR BEURRE  APPLICATION

Application created to find the products with the best nutriscore.

## Getting Started

These instructions will get you to use the application on your local machine

### Prerequisites

Your local machine must have a MySQL server installed. 
A user account must be created with all privileges.
- user : ocr
- password : As you want(ask when starting the application)
rules user : all privileges on this database

```
CREATE DATABASE IF NOT EXISTS PUR_BEURRE
CHARACTER SET 'utf8mb4';
CREATE USER 'ocr'@'localhost' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON pur_beurre. * TO 'ocr'@'localhost';
```
The database 'pur_beurre' will be created automatically by starting the application.
Install Python version 3.7, with the modules in the requirements.txt file.

### Installing

Save the Pur_Beurre folder on your local machine (containing the mysql server).
Check that the folder contains 5 folders:
- admin : 
    __init__.py,
    append.py,
    create.py,
- controllers : 
    __init__.py,
    orm.py
- misc :
    __init__.py,
    tools.py
- models :
    __init__.py,
    orm_data.py,
    product.py,
    product_store.py,
    research.py,
    store.py,
    subcategory.py
- views :
    __init__.py,
    console.py,
    append_feedback.py
- main.py
- readme.md
- requirements.txt
- settings.json

Launch the 'create.py' file from admin folder to create the tables into the Pur_Beurre database.

```
> python create.py
```
Enter the password for the user 'ocr'.
```
> python create.py
Veuillez saisir le mot de passe de connexion:
```

Launch the 'main.py' , enter the database password and select 1 at the first question 
("Souhaitez-vous mettre à jour les articles?") to update the subcategories and the products into the Database. 
You can add benchmark products (the subcategories) by editing the 'settings.json' file and then relaunching the script.

```
"categories": [
    "pizza au thon",
    "pizza au fromage",
    "pizza au jambon",
    "yaourt a la fraise",
    "yaourt a l abricot",
    "yaourt a l ananas",
    "confiture a la fraise",
    "confiture a la framboise",
    "confiture d abricot",
    "jus de fraise",
    "jus d orange",
    "jus de raisin"
  ]
```

You can change the page number and the number of products you want to download from the OpenFoodFacts API,
 on the same one.

```
  "page": 1,
  "product_per_page": 100
```

Let the program download the data and save it to the local database.
You can see the errors if exist.
```
Existe déjà, Produit: Yaourt gourmand Pomme Cannelle au Lait entier | Code-barre: 3339526272002
Existe déjà, Produit: Yaourt lit de pomme | Code-barre: 3463340005017
Existe déjà, Produit: Crémeux sur lit de Pomme Cannelle | Code-barre: 4056489189473
>
```
You can add new products by the same way (change the page's number on 
'settings.json' file).

## How to use

Launch the 'main.py' file to start the program.

```
> python main.py
```
Enter the password for the user 'ocr'.
```
> python main.py
Veuillez saisir le mot de passe de connexion:
```
As explained, you can add new products or not.
```
Souhaitez-vous mettre à jour les articles?
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

Version 0.3

## Authors

* **Ben Bessayah** - *PurBeurre* - [bbbenbat](https://github.com/bbbenbat)




