# OOP-assignment-2
#### Master1 Data Science
#### University of Angers
#### Course: POO et traitement des données en Python
#### Prof: Jacquelin Charbonnel

TicTacToe
=========


Le jeu de [tic-tac-toe](https://fr.wikipedia.org/wiki/Tic-tac-toe) se joue à 2 sur un damier 3x3. Chaque case du damier peut recevoir un pion. Il y a 2 types de pions, 1 type par joueur.

Question 1 🙂
-------------

Modéliser le damier de ce jeu par une classe pouvant s’utiliser comme :

    jeu = TicTacToe()
    print(jeu)
              . . .
              . . .
              . . .
    jeu.place(1,1,'O')
    print(jeu)
              O . .
              . . .
              . . .
    jeu.place(2,3,'X')
    print(jeu)
              O . .
              . . X
              . . .

Question 2 🙂
-------------

Créer une classe `Joueur` permettant d’écrire :

    jeu = TicTacToe()
    bob = Joueur(jeu,nom='Bob',pion='X')
    alice = Joueur(jeu,nom='Alice',pion='O')
    print(jeu)
              . . .
              . . .
              . . .
    bob.joue(1,1)
    print(jeu)
              X . .
              . . .
              . . .
    alice.joue(1,3)
    print(jeu)
              X . O
              . . .
              . . .
    bob.joue(3,3)
    alice.joue(2,2)
    bob.joue(3,1)
    alice.joue(3,2)
    bob.joue(2,1)
    print(jeu)
              X . O
              X O .
              X O X

Question 3 🙂
-------------

Ajouter dans la classe `TicTacToe` une méthode `vainqueur()` qui renvoie quel pion a gagné, si la partie est terminée, ou `None` sinon :

    jeu = TicTacToe()
    bob = Joueur('Bob',jeu,'X')
    alice = Joueur('Alice',jeu,'O')
    bob.joue(1,1)
    alice.joue(1,3)
    print(jeu)
              X . O
              . . .
              . . .
    print(jeu.vainqueur())
            None
    
    bob.joue(3,3)
    alice.joue(2,2)
    bob.joue(3,1)
    alice.joue(3,2)
    bob.joue(2,1)
    print(jeu)
              X . O
              X O .
              X O X
    print(jeu.vainqueur())
            X

Question 4 🤔
-------------

Modifier le code précédent de façon à ce que la méthode `vainqueur()` renvoie le nom du vainqueur, plutôt que son pion.


var myDate = new Date(document.lastModified); myNewDate = new Intl.DateTimeFormat( undefined, {year: "numeric", month: "long", day: "numeric", hour: "2-digit", minute: "2-digit"} ) .format(myDate).replace(/\\./g, '-'); document.getElementById("lastmodify").innerHTML = myNewDate ;
