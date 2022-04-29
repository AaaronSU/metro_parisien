# metro_parisien

Le projet consiste à trouver le plus court chemin entre 2 stations des lignes de métro.

Pour lancer le programme, vous avez besoin des outils suivants :
- python 3.8 ou ultérieurement
- pyvis (pour la partie graphique qui va implementer dans le futur)

Pour installer pyvis, il faut que vous ayez l'outil de la gestion des packages python *pip*.
- https://pip.pypa.io/en/stable/installation/
- https://pyvis.readthedocs.io/en/latest/install.html

Le fichier que nous avons à disposition:
- metro.txt

Nous avons décidé de séparer notre projet en 2 partis, les structures de données et les fonctions.

La première partie est écrite en orienté objet et la partie fonctionnelle comme il indique, est constitué des fonctions.

Python utilise la programmation orientée objet et la programmation fonctionnelle, ce découpage exploite la diversité du language Python.

Dans la documentation nous allons voir d'abord les structures des données que nous avons choisies. Ensuite les fonctions que nous avons implémenté avec notre structure des données ainsi les améliorations que nous pouvons apporter en plus sur le projet.

## Structure de données
Notre structure de données est constitué de 4 classes : graph, node, line, edge.

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
Pour vérifier la connexité du graphe, nous avons fait un parcours en largeur. 
D'abord nous mettons la couleur de tous les sommets en blanche.
Puis nous sélectionnons un sommet, mettre dans la liste à traiter. Tant que la liste à traiter n'est pas vide, sélectionner le premier élément dans la liste. Pour tous les successeurs de cet élément, nous le mettons dans la liste à traiter si le successeur n'est pas colorié en noir. Quand on aura fini de parcourir tous les successeurs de ce sommet, on le colorie en noir.

Affins pour tous les sommets du graphe, nous vérifions si le sommet est colorié en noir. Si tous les sommets sont coloriés en noir, le graphe est connexe sinon il en est pas.


### Trouver les lignes avec les stations de métro associées
Pour trouver les stations dans la ligne de métro, nous avons décidé de faire un parcours en profondeur. Nous traitons pour tous les successeurs de la station de départ. Si le successeur n'a pas le même nom que la station qu'on est en train de traiter, nous ajoutons dans une liste qui représente la ligne et nous faisons un appel récursif au successeur.

### Trouver les terminus des lignes
Pour trouver les terminus des lignes, nous avons fait le traitement suivant pour toutes les lignes. Pour toutes les stations de la ligne, si la station a un seul et seulement un seul successeur qui a le nom différent alors c'est un terminus de la ligne.

### Trouver le plus court chemin
Pour trouver le plus court chemin, nous avons utilisé l'algorithme de Dijkstra.

## Améliorations possibles
### Stockage dans une base de données
La structure des données de notre programme permet de stocker de manière intuitive les informations dans une base de données grâce à une technique appelée ORM.
### Compléter les stations manquantes du métro parisien
Il y a des informations manquantes dans le projet. Comme la date de création du métro.txt date, il y a des stations de métro qui ont apparu entre temps.
### Affichage graphique des sommets avec la librairie externe *pyvis*