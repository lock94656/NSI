# coding: utf-8
# Encodage et décodage en utf-8.


# ---------------------------------------------------------------------------- #
# Exercices sur les fonctions
# ---------------------------------------------------------------------------- #
# Auteur:                   Hugo Gibert
# Création :                21/09/2026
# Dernière modification :   25/09/2026
# ---------------------------------------------------------------------------- #
# Consignes :
#
# Traiter les neuf exercices ci-dessous en pensant à documenter les fonctions.
# À la fin de la séance, envoyer le fichier à M. Thomas, via École Directe.
# ---------------------------------------------------------------------------- #


# ---------------------------------------------------------------------------- #
# Exercice 1
# Définir une fonction test_Pythagore qui prend trois entiers a, b et c en
# arguments et renvoie un booléen indiquant si a² + b² = c².
import math

def test_Pythagore(a,b,c):
    if(c>b and c>a):
        return c**2==b**2+a**2
    else:
        return "Error"
'''
a = int(input("entrer a : "))
b = int(input("entrer b : "))
c = int(input("entrer c : "))

if(test_Pythagore(a,b,c)==False):
    print("a^2+b^2 n'est pas égal à c^2 : Le triangle n'est pas rectangle")
elif(test_Pythagore(a,b,c)==True):
    print("a^2+b^2 = c^2 : Le triangle est rectangle")
else:
    print("Tu sais pas ecrire...")
'''


# ---------------------------------------------------------------------------- #
# Exercice 2
# Définir une fonction valeur_absolue qui prend un entier en argument
# et renvoie sa valeur absolue.


def valeur_absolue(a):
    a = math.sqrt(a**2)
    return a
'''
a = int(input("Entrer a : "))
print(valeur_absolue(a))
'''

# ---------------------------------------------------------------------------- #
# Exercice 3
# Écrire une fonction max2(a, b) qui renvoie le plus grand des deux entiers a
# et b.


def max2(a,b):
    if(a>b):
        return a
    elif(a<b):
        return b
    else:
        return "Error"
'''
a = int(input("entrer a : "))
b = int(input("entrer b : "))

print(max2(a,b))
'''

# ---------------------------------------------------------------------------- #
# Exercice 4
# En se servant de la fonction max2 de l'exercice précédent,
# écrire une fonction max3(a, b, c) qui renvoie le plus grand des trois
# entiers a, b et c.

def max3(a,b,c):
    if(a>b and a>c):
        return "a = ", a
    elif(b>a and b>c):
        return "b = ", b
    elif(c>a and c>b):
        return "c = ", c
    else:
        return "Error"
'''
a = int(input("entrer a : "))
b = int(input("entrer b : "))
c = int(input("entrer c : "))

print(max3(a,b,c))
'''

# ---------------------------------------------------------------------------- #
# Exercice 5
# Écrire une fonction puissance(x, k), qui renvoie x à la puissance k.
# On utilisera une boucle for pour faire le calcul. On suppose k ⩾ 0
# et on rappelle que x^0 = 1.

def puissance(x, k):
    p = x
    for i in range(k-1):
        p=p*x
    return p

'''
a = int(input("entrer a : "))
b = int(input("entrer b : "))

print(puissance(a,b))
'''

# ---------------------------------------------------------------------------- #
# Exercice 6
# Écrire une fonction bissextile(a) qui renvoie un booléen indiquant
# si l’année a est une année bissextile.
# On rappelle qu'une année bissextile est une année multiple de 4 mais pas
# de 100, ou multiple de 400.

def bissextile(a):
    b = a%400 == 0 or a%4==0 and a%100!=0
    return b

'''
a=int(input("Entrer une année : "))

if(bissextile(a)==True):
    print("L'année ",a, "est bissextile.")
else:
    print("L'année ",a, "n'est pas bissextile.")
'''


# ---------------------------------------------------------------------------- #
# Exercice 7
# Écrire une fonction nb_jour_sannee(a) qui renvoie le nombre de jours de
# l'année a, en utilisant la fonction de l'exercice précédent pour savoir
# si l'année a est bissextile.

def nb_jours_annee(a):
    if(bissextile(a)):
        return 366
    else:
        return 365
'''
a=int(input("Entrer une année : "))
print("Le nombre de jour dans l'année",a,"est de",nb_jours_annee(a))

'''
# ---------------------------------------------------------------------------- #
# Exercice 8
# Écrire une fonction nb_jours_mois(a, m) qui renvoie le nombre de jours dans le
# mois m de l'année a, en utilisant la fonction de l'exercice 6 pour savoir
# si l'année a est bissextile.
# On suppose que le mois m est un entier compris entre 1 (pour janvier)
# et 12 (pour décembre).

def nb_jours_mois(a, m):
    if(m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12):
        return 31
    elif(bissextile(a)==True and m==2):
        return 29
    elif(bissextile(a)==False and m==2):
        return 28
    else:
        return 30
'''
a=int(input("Entrer une année : "))
m=int(input("Entrer un mois : "))
print("Le nombre de jour dans le mois",m,"de l'année",a, "est de : ",nb_jours_mois(a,m))
'''
# ---------------------------------------------------------------------------- #
# Exercice 9
# En utilisant les fonctions des exercices précédents, écrire une fonction
# nb_jours(ji, mi, ai, jf, mf, af) qui renvoie le nombre de jours compris
# entre deux dates données
# (par exemple votre date de naissance et la date d'aujourd'hui).

def nb_jours(ji, mi, ai, jf, mf, af):
    mois = 0
    annee = 0
    for i in range(1,mi):
        mois+= nb_jours_mois(ai,mi-i)
    for i in range(1582,ai):
        annee+= nb_jours_annee(ai-i)
    annee-=10
    tot1=mois+annee+ji
    return tot1


print(nb_jours(20, 5, 2028, 1, 5, 2028))









