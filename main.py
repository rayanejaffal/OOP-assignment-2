#!/bin/env python3
"""
Python Object
Rayane JAFFAL
Probleme 1
"""

# Main
# Question 1

from TicTacToe import TicTacToe

jeu = TicTacToe()
print(jeu)

jeu.place(1,1,'O')
print(jeu)

jeu.place(2,3,'X')
print(jeu)


# Question 2

from Joueur import Joueur

jeu = TicTacToe()
bob = Joueur(jeu,nom='Bob',pion='X')
alice = Joueur(jeu,nom='Alice',pion='O')
print(jeu)

bob.joue(1,1)
print(jeu)

alice.joue(1,3)
print(jeu)

bob.joue(3,3)
alice.joue(2,2)
bob.joue(3,1)
alice.joue(3,2)
bob.joue(2,1)
print(jeu)

# Question 3 

jeu = TicTacToe()
bob = Joueur(jeu,'Bob','X')
alice = Joueur(jeu,'Alice','O')
bob.joue(1,1)
alice.joue(1,3)
print(jeu)

print(jeu.vainqueur())

bob.joue(3,3)
alice.joue(2,2)
bob.joue(3,1)
alice.joue(3,2)
bob.joue(2,1)
print(jeu)

print(jeu.vainqueur())

# Question 4

jeu = TicTacToe(bob, alice)
bob = Joueur(jeu,'Bob','X')
alice = Joueur(jeu,'Alice','O')
bob.joue(1,1)
alice.joue(1,3)
print(jeu)

print(jeu.vainqueur())

bob.joue(3,3)
alice.joue(2,2)
bob.joue(3,1)
alice.joue(3,2)
bob.joue(2,1)
print(jeu)

print(jeu.vainqueur())