
"""
#job 1

def fruits():
    fruits = ["pomme", "cerise", "orange"]
    print(fruits)

fruits()


#job 2

def fruits():
    fruits = ["pomme", "cerise", "orange"]
    return fruits

deuxieme_element = fruits()[1]
print(deuxieme_element)


#job 3

def fruits():
    fruits = ["pomme", "cerise", "orange"]
    return fruits

new_list = fruits()
new_list.append("Melon")
print(new_list)

#job 4

def fruits():
    fruits = ["pomme", "cerise", "orange", "melon"]
    return fruits

new_list = fruits()
new_list.insert(2, "mangue")

print(new_list)

#job 5

# Création de la liste L avec au moins 5 entiers
L = [1, 2, 3, 4, 5]
print(L)
# Afficher la deuxième valeur de la liste
print(L[1])  # Les indices commencent à 0, donc L[1] est la deuxième valeur

# Définir une fonction pour remplacer L[3] par la somme des cases voisines L[2] et L[4]
def remplacer_troisieme(L):
    L[3] = L[2] + L[4]  # Remplace L[3] par L[2] + L[4]

# Appeler la fonction pour modifier L
remplacer_troisieme(L)

# Afficher la liste mise à jour
print(L)

# Afficher la dernière valeur de la liste
print(L[-1])  # L[-1] permet d'accéder à la dernière valeur de la liste

#job 6

# Définir une liste non vide
L = [1, 2, 3, 4, 5]

# Afficher la liste avant l'échange
print("Avant l'échange :", L)

# Échanger les valeurs de la première et de la dernière case
L[0], L[-1] = L[-1], L[0]

# Afficher la liste après l'échange
print("Après l'échange :", L)


#job 7

# Définir la liste
L = [8, 24, 48, 2, 16]

# Initialiser un compteur
compteur = 0

# Parcourir les éléments de la liste
for nombre in L:
    if nombre % 3 == 0:  # Vérifier si le nombre est un multiple de 3
        compteur += 1

# Afficher le résultat
print(f"Nombre de multiples de 3 dans la liste : {compteur}")

#job 8

# Définir la liste
L = [8, 24, 27, 48, 2, 16, 9, 7, 84, 91]

# Initialiser une variable pour stocker la somme des valeurs paires
somme_paires = 0

# Parcourir les éléments de la liste
for nombre in L:
    if nombre % 2 == 0:  # Vérifier si le nombre est pair
        somme_paires += nombre  # Ajouter le nombre pair à la somme

# Afficher le résultat
print(f"La somme des valeurs paires dans la liste est : {somme_paires}")


#job 9

# Définir la liste
L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]

# Récupérer la valeur maximum et minimum de la liste
valeur_max = max(L)  # Fonction max() pour obtenir la valeur maximale
valeur_min = min(L)  # Fonction min() pour obtenir la valeur minimale

# Afficher les résultats
print(f"La valeur max est : {valeur_max}")
print(f"La valeur min est : {valeur_min}")


#job 10

# Définir la liste
L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]

# Initialiser le produit à 1 (car c'est l'élément neutre pour la multiplication)
produit = 1

# Parcourir les éléments de la liste
for nombre in L:
    if 25 <= nombre <= 90:  # Vérifier si le nombre est dans l'intervalle [25, 90]
        produit *= nombre  # Multiplier le produit par le nombre

# Afficher le résultat
print(f"Le produit des valeurs dans l'intervalle [25, 90] est : {produit}")


#job 11

# Créer la liste d'entiers
L = [7, 11, 42, 39, 2]

# Modifier chaque élément de la liste en l'augmentant de 1
for i in range(len(L)):
    L[i] += 1  # Ajouter 1 à chaque élément

# Afficher la liste modifiée
print("Liste après modification :", L)


#job 12

liste = [8, 27, 3, 68, 13]
print(sorted(liste))

#job 13

liste = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]

new_list = []

for i in liste:
    doublon = False
    for j in new_list:
        if i == j:
            doublon = True
            break

    if not doublon:
        new_list.append(i)

print("Liste sans doublons :", new_list)

# Dexième methode)
def supprimer_doublons(liste):
    # Créer une nouvelle liste vide pour stocker les éléments uniques
    liste_sans_doublons = []
    
    # Parcourir tous les éléments de la liste
    for element in liste:
        # Vérifier si l'élément n'est pas déjà dans la liste sans doublons
        existe_deja = False
        for unique_element in liste_sans_doublons:
            if element == unique_element:
                existe_deja = True
                break
        # Si l'élément n'existe pas encore dans la liste, l'ajouter
        if not existe_deja:
            liste_sans_doublons.append(element)
    
    # Retourner la liste sans doublons
    return liste_sans_doublons

# Exemple d'utilisation
L = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]
L_sans_doublons = supprimer_doublons(L)
print("Liste sans doublons :", L_sans_doublons)

"""
#job 14

def my_long_word(nombre, texte):
    # Diviser la chaîne de caractères en mots
    mots = []
    mot = ""
    
    # Parcourir chaque caractère du texte pour séparer les mots
    for char in texte:
        if char == " ":
            if mot != "":
                mots.append(mot)
                mot = ""
        else:
            mot += char

    # Ajouter le dernier mot, s'il y en a un
    if mot != "":
        mots.append(mot)
    
    # Créer une liste des mots qui ont plus de caractères que le nombre spécifié
    resultats = []
    for mot in mots:
        # Comparer la longueur du mot à la valeur donnée
        count = 0
        for char in mot:  # Compter les caractères du mot manuellement
            count += 1
        if count > nombre:
            resultats.append(mot)
    
    # Retourner les mots longs sous forme de chaîne
    return " ".join(resultats)

# Exemple d'utilisation
texte = "La peur est le chemin vers le côté obscur, la peur mène à la colère, la colère mène à la haine, la haine mène à la souffrance"
resultat = my_long_word(3, texte)
print(resultat)
exit()
#job 15

def arrondir_nombre(nombre):
    # Arrondir le nombre manuellement à l'entier le plus proche
    if nombre - int(nombre) >= 0.5:
        return int(nombre) + 1  # Arrondi supérieur
    else:
        return int(nombre)  # Arrondi inférieur

def trier_liste(liste):
    # Tri par sélection (en ordre croissant)
    n = 0
    for element in liste:
        n += 1  # Calculer la longueur de la liste manuellement
        
    for i in range(n):
        for j in range(0, n-i-1):
            if liste[j] > liste[j+1]:
                # Échanger les éléments
                temp = liste[j]
                liste[j] = liste[j+1]
                liste[j+1] = temp

# Liste des nombres
L = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]

# Arrondir les nombres
L_arrondis = [arrondir_nombre(n) for n in L]

# Trier la liste arrondie
trier_liste(L_arrondis)

# Afficher la liste triée après arrondi
print("Liste triée après arrondi :", L_arrondis)
