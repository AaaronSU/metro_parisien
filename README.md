# metro_parisien

Le projet consiste à trouver le plus court chemin entre 2 stations de métro.
Pour lancer le programme, vous avez besoin des outils suivants :
- python 3.8 ou ultérieurement
- pyvis (pour la partie graphique qui va être implementer dans le futur)

Pour installer pyvis, il faut que vous ayez l'outil de la gestion des packages python *pip*.
- https://pip.pypa.io/en/stable/installation/
- https://pyvis.readthedocs.io/en/latest/install.html

Le fichier que nous avons à disposition:
- metro.txt

Nous avons décidés de séparer notre projet en 2 parties : les structures de données et les fonctions.

La première partie est écrite en orienté objet et la partie deuxième partie est fonctionnelle.
Python utilise la programmation orientée objet et la programmation fonctionnelle, ce découpage exploite la diversité du language Python.

Dans la documentation nous allons voir d'abord les structures de données que nous avons choisi. Elles ont était implémenté en classe.Puis,les fonctions que nous avons programmé grace à nos structure de données.  Pour finir,nous allons les améliorations que nous pouvons apporter en plus sur le projet.

## Structure de données
Notre structure de données est constitué de 4 classes : graph, node, line, edge.
Graph va nous servir à créer notre carte de métro parisien. 
Node va nous permettre de répresenter les stations de métro.
Line va nous permettre de répresenter les lignes de métro. 
Edge va nous permettre de créer les liaisons direct entre deux stations de métro. 

### Graph
### Node
### Line
### Edge

## Fonctions principale

### Initialiser le graphe
Pour initialiser le graphe, nous avons fait une fonction pour extraire les données dans metro.txt et les stocker dans notre graphe.

La fonction regarde le premier caractère de chaque ligne afin de déterminer le traitement associé. Il y a 3 cas possibles :

- si la ligne commence par #, on la néglige.
- si la ligne commence par V, on ajoute au graphe un noeud
- si la ligne commence par E, on ajoute au graphe une arête dans un sens et dans l'autre sens pour rendre le graphe non orienté afin de faciliter l'implémentation des algorithmes.

### Vérifier la connexité
Pour vérifier la connexité du graphe, nous avons fait un parcours en largeur. (fonction bfs)

Dans un premier temps, tous les sommets sont mis en blanc.
Un sommet est selectionner et ajouter à une liste. Cette liste répresente les sommets à traiter. Tant que la liste à traiter n'est pas vide, le premier élément de la liste est sélectionner. Tous les successeurs du sommet sont ajouter à la liste à traiter. Lorsque tous les sucesseurs sont traiter, le sommet père est mis en noir et est enlever de la liste à traiter. Et cela s'itere jusqu'à que tous les sommets liée soit traiter. 

Dans un second temps, on applique la fonction au sommet du graphe. Si un sommet n'est pas colorié en noir alors le graphe n'est pas connexe


### Trouver les lignes avec les stations de métro associées
Pour trouver les stations d'une ligne de métro, nous avons décidé de faire un parcours en profondeur. (fonction pp)

On initialise une liste. On choisit une station de départ qu'on rajoute à liste. On itère sur les sucesseur de cette station. Si un sucesseur n'a pas le même nom que la station choisi, nous ajoutons ce sucesseur dans la liste. Si le même nom on le néglige. L'itération quand tous les stations sont dans la liste.

### Trouver les terminus des lignes
Pour trouver les terminus des lignes, nous avons utilisé la fonctions pp. Lorsque une station a un unique  successeur qui a un nom différent alors c'est un terminus de la ligne. 

Nous avons vérifier les lignes et les terminus humainement. Les numéros des lignes ont été ajouté à la main. 

### Trouver le plus court chemin
Pour trouver le plus court chemin, nous avons utilisé l'algorithme de Dijkstra.
Nous l'avons simplement implimenter en utilisé les strutures de donnée crée. 

## Améliorations possibles
### Stockage dans une base de données
La structure des données de notre programme permet de stocker de manière intuitive les informations dans une base de données grâce à une technique appelée ORM.
### Compléter les stations manquantes du métro parisien
Il y a des informations manquantes dans le projet. Comme la date de création du métro.txt date, il y a des stations de métro qui ont apparu entre temps.
### Affichage graphique des sommets avec la librairie externe *pyvis*
