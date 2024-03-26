# Contexte

Supposons que vous soyez un responsable RH et que vous deviez **créer un fichier** contenant les salaires de vos employés. Nous allons lire dans un fichier **CSV** les noms des employés et les heures travaillées, puis **créer** un autre **fichier CSV** avec leurs *salaires calculés*.

# Instructions  

1. **Écrivez** un script pour lire le contenu de notre fichier `input.csv` au format suivant :

| nom  | heures_travaillees |
| ------------- |:-------------:|
| Pierre Durand      | **36**     |
| Paul Dupont      | **41**     |
| Edouard Gentil      | **40**     |

**Conseil** : Créez une fonction `extract()` qui retourne les données du fichier `input.csv`

2. **Créez** un nouveau fichier CSV appelé `output.csv` qui devrait avoir le format suivant :

* Les **salaires** sont calculés à l'aide de la formule `heures_travaillées * 15`. *(Attention : les clés doivent être en minuscule pour que les tests passent)*


| nom  | salaire |
| ------------- |:-------------:|
| Pierre Durand      | **540**     |
| Paul Dupont      | **615**     |
| Edouard Gentil      | **600**     |

**Conseil** : Créez une première fonction `transform()` qui sera responsable de la **transformation** des données et la création d'un nouveau conteneur avec toutes les **nouvelles données**. Et ensuite une fonction `load()` qui va charger les nouvelles données dans le fichier `output.csv`.