from random import *
import sys
import time


def print_slow(string):
    for letter in string:
        #        Lecture lente
        sys.stdout.write(letter)
#        Nettoyer
        sys.stdout.flush()
# Plus rapie ou plus lent (on le mettra à 0.04)
        time.sleep(0.01)


def tuto_fight():
    print("━━━━━━━━━━━━")
    print_slow("Loic: Je vais te montrer comment te battre.\n")
    print("━━━━━━━━━━━━")
    choice = int(input("Pour attaquer appuyer sur votre touche [1] :\n "))

    while choice != 1:
        choice = int(input("Pour attaquer appuyez sur votre touche [1] :\n "))
    print("━━━━━━━━━━━━")
    print_slow("Slime subit 5 de dégats.\n")
    print_slow("Slime a 45 HP.\n")
    print("━━━━━━━━━━━━")
    choice_menu = int(
        input("Loic: Maintenant  appuyez sur [2] pour accéder aux Compétences :\n "))

    while choice_menu != 2:
        print("━━━━━━━━━━━━")
        choice_menu = int(
            input("Loic: Maintenant  appuyez sur [2] pour accéder aux Compétences :\n "))
    choice_comp = int(
        input("et appuyez sur [1] pour utiliser un coup percant :\n "))
    print("━━━━━━━━━━━━")

    while choice_comp != 1:
        choice_comp = int(input("et appuyez sur [1] pour coup percant :\n "))
    print_slow("Slime subit 30 de dégats.\n")
    print_slow("Slime a 15 HP.\n")
    print_slow("Slime attaque Cochon Mystérieux !\n")
    print_slow("Cochon mystérieux a subit 15 de dégats.\n")
    print_slow("Cochon mystérieux a 85 HP.\n")
    print("━━━━━━━━━━━━")
    print_slow(
        "Vous avez perdu de la vie. \nUtilisez une potion de vie pour regagner vos HP.\n")
    choice_menu = int(
        input("Loic : Appuyez sur [3] pour accéder as votre Inventaire :\n "))
    print("━━━━━━━━━━━━")

    while choice_menu != 3:
        choice_menu = int(
            input("Loic : Maintenant appuyez sur [3] pour accéder à votre Inventaire :\n "))
    choice_sac = int(input(
        "Loic : Appuyez sur [1] pour utiliser la Potion de Vie :\n "))

    while choice_sac != 1:
        choice_sac = int(input(
            "Loic :Maintenant appuyez sur [1] pour utiliser la Potion de Vie :\n "))
    print_slow("Cochon mystérieux récupère 15 HP.\n")
    print_slow("Cochon mystérieux a 100 HP.\n")
    print_slow("Loic : Bien joué.\n")
