# Algorithme de Tri

### Trie à Bulle

```bash
Compare l'élément du tableau choisi avec l'élément du tableau au position supérieur à lui!
On répéte cette comparaison jusqu'à ce que notre tableau soit trier.
Complexité : O(n*n)
```

#### Démo
![bubble sort](https://upload.wikimedia.org/wikipedia/commons/c/c8/Bubble-sort-example-300px.gif)

### Trie par insertion

```bash
Compare l'élément du tableau choisi avec l'élément du tableau au position supérieur à lui!
Puis lorsque l'élément du tableau au position supérieur est inférieur au position du tableau choisi, 
alors on va placer cette élément inférieur à son position exacte (cela on comparant 
cette élément ci à tous les éléments qui est au position inférieur à lui).
```

#### Démo
![insertion sort](https://upload.wikimedia.org/wikipedia/commons/0/0f/Insertion-sort-example-300px.gif)

### Trie par selection

```bash
On choisi un élément du tableau "( comme l'indice 0 )" que l'on va definir comme la valeur minimale puis 
on va tester que cette choix est correct. On va comparer alors la valeur minimale avec l'élément 
du tableau si aucun des éléments present n'est inférieur que celle ci alors on ne change rien mais 
dans le cas contraire on va remplacer le minimal par l'élément plus petit que lui puis on va la placer 
dans l'index 0 si c'est la plus petite élément du tableau apres on va chercher le deuxième 
élément plus petite et on va la place à l'index 1 et ainsi de suite jusqu'à ce que le tableau soit trier 
entièrement.
```

#### Démo
![Trie par selection](https://miro.medium.com/v2/1*2H2kYDgD0u2kAM8xXrvC5w.gif)

### Trie par fusion

```bash
On divise en 2 part égal le tableau jusqu'à ce qu'on arrive a un élément par tableau seulement, puis là
on va fusionner les portions de tableau un à un. Alors pour fusionner on doit comparer le 1er élément du 
premier tableau avec le 1er élément du 2eme tableau et celle qui est le plus petite doit être place en premier 
position. Et donc on repète ce processus pour chaque portion de tableau puis à la fin on a un tableau trier
```

#### Démo
![Trie par fusion](https://upload.wikimedia.org/wikipedia/commons/c/cc/Merge-sort-example-300px.gif)

### Trie rapide ou Quick Sort

```bash
Il est aussi base sur le principe de diviser pour rêgner, on divise comme avec le trie par fusion
mais la difference est qu'on choisi un pivot dans notre code on va d'abord choisir le dernier élément du 
tableau comme pivot. Puis on va comparer avec l'élément du tableau ce pivot si l'élément est inférieur alors
on la place à gauche de pivot et à droite si elle est supérieur ou égale au pivot. 
puis apres avoir obtenu c'est deux nouveau sous tableau on va rechoisir un pivot pour chaque sous tableau
et on repète ce processus jusqu'à ce que notre sous tableau ne contient qu'une élément car on sait déjà 
qu'un tableau à une élément est trier.
Et le trie rapide est comme son nom qui le dit elle fait partie des algorithmes de trie
le plus rapide mais pour les tableaux à moitier trier c'est le trie fusion qui est le
plus conseiller.
```

#### Démo
![Trie rapide](https://i.imgur.com/hR69aNY.png)