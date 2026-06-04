import unittest
import os
import sys

# Récupère le dossier parent ('Algo') et l'ajoute au PATH de Python
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Maintenant tu peux l'importer directement, sans les deux points !
from merge_sort import merge_sort

class TestTriFusion(unittest.TestCase):

    def test_tableau_aleatoire(self):
        """Test avec un tableau désordonné classique"""
        tableau = [4, 1, 7, 3, 9, 2, 8, 5, 6]
        attendu = sorted(tableau) # sorted() est la fonction de tri native de Python
        self.assertEqual(merge_sort(tableau), attendu)

    def test_tableau_deja_trie(self):
        """Test avec un tableau déjà trié (ne devrait rien changer)"""
        tableau = [1, 2, 3, 4, 5]
        self.assertEqual(merge_sort(tableau), [1, 2, 3, 4, 5])

    def test_tableau_inverse(self):
        """Test avec un tableau trié dans l'ordre décroissant"""
        tableau = [5, 4, 3, 2, 1]
        self.assertEqual(merge_sort(tableau), [1, 2, 3, 4, 5])

    def test_tableau_vide(self):
        """Test avec un tableau vide (cas aux limites)"""
        tableau = []
        self.assertEqual(merge_sort(tableau), [])

    def test_un_seul_element(self):
        """Test avec un tableau contenant un seul élément"""
        tableau = [42]
        self.assertEqual(merge_sort(tableau), [42])

    def test_avec_doublons(self):
        """Test avec des éléments qui se répètent"""
        tableau = [3, 1, 3, 2, 1, 4]
        self.assertEqual(merge_sort(tableau), [1, 1, 2, 3, 3, 4])

    def test_valeurs_negatives(self):
        """Test avec des nombres négatifs"""
        tableau = [3, -1, 0, -5, 2]
        self.assertEqual(merge_sort(tableau), [-5, -1, 0, 2, 3])

if __name__ == '__main__':
    # Lance tous les tests de la classe
    unittest.main()