#!/bin/env python3
"""
Python Object
Rayane JAFFAL
Probleme 1
"""

# Question 1

class TicTacToe:
    
    def __init__(self): #définir unn grid 3x3 avec une '.' dans chaque position
        self.grid = []
        for i in range(3):
            ligne = []
            for j in range(3):
                ligne.append('.')
            self.grid.append(ligne)
    
    def place(self,row,column,pion): #placer un pion dans la position
        #ajouter un pion
            self.grid[row -1][column - 1] = pion #le input des lignes et colonnes est entre 1 et 3
            
    def __str__(self): #pour afficher le grid comme demandé comme un string
        grid_str = ""
        for ligne in self.grid:
            for position in ligne:
                grid_str += position + ' '
            grid_str = grid_str.rstrip() + '\n'
        return grid_str
    
# Question 3

    def vainqueur(self): #savoir quel pion est le gagnant
        
        for i in range(3):
            #vérifier si quelqu un a gagné sur les lignes
            if self.grid[i][0] == self.grid[i][1] == self.grid[i][2] != ' ':
                return self.grid[i][0] #une des trois position, ils sont tous les memes
            
            #vérifier si quelqu un a gagné sur les colonnes
            elif self.grid[0][i] == self.grid[1][i] == self.grid[2][i] != ' ':
                return self.grid[0][i]
            
            #vérifier si quelqu un a gagné sur les diagonales, notons qu'il ya deux diagonales
            elif self.grid[0][0] == self.grid[1][1] == self.grid[2][2] != ' ':
                return self.grid[0][0]
            
            elif self.grid[0][2] == self.grid[1][1] == self.grid[2][0] != ' ':
                return self.grid[0][2]
            
            else: return None #si aucun on return None
            
### Dans la suite le code modifié pour retourner le nom du vainqueur
# J'ai mis le code comme commentaire pour ne pas affecter le code pour les premieres trois questions
"""

# Question 4

class TicTacToe:
    
    def __init__(self,joueur1,joueur2): #J'ai ajouté deux arguments pour les nom des joueurs
        self.joueur1 = joueur1
        self.joueur2 = joueur2
        self.grid = []
        for i in range(3):
            ligne = []
            for j in range(3):
                ligne.append('.')
            self.grid.append(ligne)
    
    def place(self,row,column,pion):
        #ajouter un pion
            self.grid[row -1][column - 1] = pion
            
    def __str__(self):
        grid_str = ""
        for ligne in self.grid:
            for position in ligne:
                grid_str += position + ' '
            grid_str = grid_str.rstrip() + '\n'
        return grid_str
    

    def vainqueur(self):  #puis ici dans chaque if, j'ai comparé le contenu de la position avec le pion de chaque joueur pour savoir le vainqueur
        
        for i in range(3):
            #vérifier si quelqu un a gagné sur les lignes
            if self.grid[i][0] == self.grid[i][1] == self.grid[i][2] != ' ':
                if self.grid[i][0] == self.joueur1.pion:
                    return self.joueur1.nom
                else:
                    return self.joueur2.nom
                
            #vérifier si quelqu un a gagné sur les colonnes
            elif self.grid[0][i] == self.grid[1][i] == self.grid[2][i] != ' ':
                if self.grid[0][i] == self.joueur1.pion:
                    return self.joueur1.nom
                else:
                    return self.joueur2.nom
                
            #vérifier si quelqu un a gagné sur les diagonales, notons qu'il ya deux diagonales
            elif self.grid[0][0] == self.grid[1][1] == self.grid[2][2] != ' ':
                if self.grid[0][0] == self.joueur1.pion:
                    return self.joueur1.nom
                else:
                    return self.joueur2.nom
                
            elif self.grid[0][2] == self.grid[1][1] == self.grid[2][0] != ' ':
                if self.grid[0][2] == self.joueur1.pion:
                    return self.joueur1.nom
                else:
                    return self.joueur2.nom
                
            else: return None
            
"""
