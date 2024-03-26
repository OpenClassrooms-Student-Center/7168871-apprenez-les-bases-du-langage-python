# Instructions  

  1. Utilisez le module `beautifulsoup4` pour **extraire** les informations suivantes et les **stocker** dans des variables :

* Pour lire le contenu du fichier `index.html`, vous devez impérativement **copier-coller** le code suivant :
    
```
with open("index.html", 'r') as file:
    soup = BeautifulSoup(file, 'html.parser')
```

* Récuperez les éléments suivants dans le code html et stockez les dans des variables.
```
- le titre de la page (<title>)
- le texte de la balise <h1>
- les noms et les prix des produits dans la liste (<ul>) (les stocker dans une liste)
- les descriptions des produits dans la liste (<ul>) (les stocker dans une liste).
```

2. **Affichez** les informations **extraites** dans la console.
3. **Convertissez** les prix en euro vers le dollars (considérez que le prix `dollar = euro * 1.2` ).

#### Conseils : 
* N'oubliez pas de retirer toutes les informations inutile (Le mot `prix`, `:`, et le `€`) et de convertir le prix en entier avec la fonction `int()`
* N'oubliez pas d'ajouter le symbole `$` à la suite du prix converti, par exemple : `20$`.

4. **Affichez** la nouvelle liste avec le `nom` et le `nouveau prix en dollars`.