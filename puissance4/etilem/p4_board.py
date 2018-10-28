# coding: utf-8
# pylint: disable=c0103
"""
module de classe grille
"""

from p4_config import VOID, SPRITE

class Board:
    """
    Grille
    """
    def __init__(self, width, height):
        """
        Créé une grille vide et initialise le compteur de jetons joués
        """
        self.width, self.height = width, height
        self.grille = [[VOID for y in range(self.height)] for x in range(self.width)]
        self.dropped = 0

    def is_full(self):
        """
        Teste si la grille est pleine
        """
        return self.dropped >= self.width * self.height

    def cases(self):
        """
        Génère les cases de la grille
        """
        for x in range(self.width):
            for y in range(self.height):
                yield x, y

    def is_valid(self, case):
        """
        Teste si une case appartient à la grille
        """
        return case in self.cases()

    def is_playable(self, case):
        """
        Teste si une case est jouable
        """
        if self.is_valid(case):
            x, y = case
            return self.grille[x][y] == VOID
        return False

    def clone(self):
        """
        Renvoit un clone de la grille
        """
        snap = Board(self.width, self.height)
        for x, y in snap.cases():
            snap.grille[x][y] = self.grille[x][y]
        snap.dropped = self.dropped
        return snap

    def __str__(self):
        """
        Affiche la grille
        """
        out = "\n|"
        for i in range(self.width):
            out += f"c{i+1}|"
        out += "\n"
        for y in range(self.height):
            out += "|"
            for x in range(self.width):
                token = self.grille[x][y]
                out += f"{SPRITE[token]} |"
            out += "\n"
        out += "\n"
        return out
