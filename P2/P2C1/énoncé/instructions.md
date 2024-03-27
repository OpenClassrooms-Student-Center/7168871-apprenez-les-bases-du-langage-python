# contexte

Vous allez créer une calculatrice qui permettra d'effectuer une opération simple entre deux nombres. Vous devrez donc créer deux variables pour stocker les deux nombres, et une variable pour stocker le symbole qui représentera l'opération à effectuer. Vous devrez d'abord créer une structure conditionnelle qui vérifiera la validité des variables et du symbole. Ensuite, vous devrez créer une deuxième structure conditionnelle pour effectuer l'opération en fonction du symbole choisi. Ne vous inquiétez pas, l’exercice sera guidé par des questions. C’est parti ! À vous de jouer !

# Instructions  

#### 1. Créez deux variables `nombre_a_gauche` et `nombre_a_droite` , et affectez-leur chacune un nombre entier à l'aide d'un input.
- La valeur pour **chaque variable** doit être assigné à l'aide de la fonction `input()` qui permet de demander à l'utilisateur d'entrer une chaine de caractère.

#### 2. Créez une variable `operation` pour stocker le symbole d'opération **(+, -, * ou /)**. L'opérateur sera aussi demander à l'aide de la fonction `input()`.

#### 3. Créez une dernière variable `resultat` initialisée à 0, qui contiendra ensuite le résultat du calcul.

#### 4. Vérifier les deux nombres entiers

* Vérifiez que les **deux variables** `nombre_a_gauche` et `nombre_a_droite` sont bien des nombres entiers à l'aide de la fonction `isnumeric()`.
* Si l'une ou les deux ne sont pas des entiers, affichez un message d'erreur correspondant et quittez le programme. Affichez le message suivant : `Erreur: les deux nombres doivent être des nombres entiers` *(Faite un copier-coller pour éviter que le test ne passe pas)*
* Sinon convertissez les en entier à l'aide de la fonction `int()`.

#### 5. Vérifier le symbole

* Vérifiez que le symbole stocké dans la variable `operation` correspond bien à une des 4 opérations autorisées (+, -, * ou /) à l’aide d'une structure `match` et effectuez le calcul correspondant dans chaque cas. Stockez le résultat dans la variable `resultat`.
* Si le symbole n'est pas correct, affichez un message d'erreur correspondant, et quittez le programme. (**Indice** : *pensez à la valeur par défaut*) Affichez le message suivant : `Erreur: le symbole d'opération doit être '+', '-', '*' ou '/'.` *(Faite un copier-coller pour éviter que le test ne passe pas)*
* Il est impossible de diviser un nombre par 0, il faut donc prévoir une structure conditionnelle supplémentaire pour vérifier ce cas dans la structure `match` . Utilisez les conditions if-else pour réaliser cette opération ; s’il y a une division par 0, affichez `Erreur: impossible de diviser par zéro.`(Faite un copier-coller pour éviter que le test ne passe pas) , sinon stockez le calcul dans la variable `resultat` .

#### 6. Affichez le résultat contenu dans la variable `resultat` .

**Attention** : Dans cet exercice, écrivez votre code dans la partie située sous la ligne `def main()`. **Assurez-vous donc de tout indenter d'un cran** pour que votre code fonctionne correctement. Nous avons enveloppé votre code dans ce qu'on appelle une fonction, pour tester votre code nous avons dû imbriquer votre code dans cette fonction.