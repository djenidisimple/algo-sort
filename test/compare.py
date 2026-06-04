import random
import time

import os
import sys

# Récupère le dossier parent ('Algo') et l'ajoute au PATH de Python
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Maintenant tu peux l'importer directement, sans les deux points !
from insertion_sort import insertion_sort
from merge_sort import merge_sort
# Génère un grand tableau de 5 000 nombres aléatoires
grand_tableau = [random.randint(0, 10000) for _ in range(5000)]

# Test de l'insertion sort
debut = time.time()
insertion_sort(grand_tableau.copy())
fin = time.time()
print(f"Insertion sort: {fin - debut:.4f}s")

# Test du merge sort
debut = time.time()
merge_sort(grand_tableau.copy())
fin = time.time()
print(f"Merge sort: {fin - debut:.4f}s")