# AlgoInvest&Trade

Déterminer un choix optimal d'actions caractérisées par un coût et un rendement, en fonction d'un coût maximum pour un profit maximal 

## Introduction

Ces instructions vous permettent de :
- récupérer le programme, 
- d'installer l'environnement nécessaire à son exécution, 
- de l'exécuter,
- d'en connaitre le résultat


### Pré-requis

```
paquets : python 3.11, python3.11-venv, git 
modules : csv
```

### Installation

1. créer l'environnement virtuel :
```
python3.11 -m venv env
source env/bin/activate
```
2. cloner le dépôt :
```
git clone https://mcstn.fr/gitea/Yann/Projet7.git
```


## Exécution
 
Pour l'algorithme bruteforce sur le dataset0, 
exécuter la commande :
```
python3 bruteforce.py
```  

Pour l'algorithme de DP, executer la commande : 
```
python3 optimized.py
``` 


## Résultat

Optimized traite par défaut les datasets 1 et 2;
Décommenter la ligne du dataset0 dans le main() si besoin
```
$ time python optimized.py 

DATASET 1
Cost: 499.43 €
Profit: 196.84 €
Shares : ['Share-HITN', 'Share-GRUT']

DATASET 2
Cost: 497.67 €
Profit: 194.90 €
Shares : ['Share-GEBJ', 'Share-LFXB', 'Share-FWBE', 'Share-PLLK', 'Share-ZKSN', 'Share-ZOFA', 'Share-PATS', 'Share-DWSK', 'Share-ALIY', 'Share-ECAQ', 'Share-FAPS', 'Share-JGTW', 'Share-QLWT', 'Share-OPBR', 'Share-ANFX', 'Share-IJFT', 'Share-JWGF']

real	0m0,852s
user	0m0,832s
sys	0m0,018s
```
## Auteur

Yann  <yann@needsome.coffee>



## License

N/A
