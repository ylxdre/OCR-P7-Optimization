# AlgoInvest&Trade

Choix optimal parmi une liste d'actions

## Introduction

Ces instructions vous permettent de :
- récupérer le programme, 
- d'installer l'environnement nécessaire à son exécution, 
- de l'exécuter,
- d'en connaitre le résultat


### Pré-requis

```
paquets : python 3.11, python3.11-venv, git 
modules : python requests, BeautifulSoup, csv, os
```

### Installation

Voici les étapes à suivre pour avoir un environnement d'exécution opérationnel :

créer l'environnement virtuel 

```
python3.11 -m venv env
source env/bin/activate
```
cloner le dépôt, aller dans le bon dossier
```
git clone https://mcstn.fr/gitea/Yann/Projet2.git
cd Projet2/rendu
```
installer les modules
```
pip install -r requirements.txt
```

## Exécution

exécuter la commande :
```
python3 main.py
```

## Résultat

Les fichiers sont placés dans un répertoire "resultat"

Le programme récupère les catégories sur la page d'accueil de l'URL, puis, pour chaque catégorie : 
1. affiche la catégorie traitée, le nombre de catégories restantes, de livres présents, traités au total et restants
2. crée un dossier du nom de la catégorie, y enregistre les images des livres nommées en fonction du titre
3. crée un fichier csv au nom de la catégorie, avec :
   - product_page_url
   - universal_ product_code (upc)
   - title
   - price_including_tax
   - price_excluding_tax
   - number_available
   - product_description
   - category
   - review_rating
   - image_url

```
$ time python3.11 main.py 
1000  à traiter répartis en  50  catégories.

[ ... ]

 Traitement terminé.

real	20m17,783s
user	4m30,695s
sys	0m3,172s
```
## Auteur

Yann  <yann@needsome.coffee>



## License

N/A
