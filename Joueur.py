#!/bin/env python3
"""
Python Object
Rayane JAFFAL
Probleme 1
"""
# Question 2

class Joueur: 
    
    def __init__(self, jeu, nom, pion): 
        self.jeu = jeu
        self.nom = nom
        self.pion = pion #'X' ou 'O'
        
    def joue(self, row, column): #placer un pion dans le jeu
        self.jeu.place(row, column, self.pion)
        
