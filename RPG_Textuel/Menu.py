import sys
from alive_progress import alive_bar
import time


class Menu:
    def __init__(self):
        self.is_game_run = True

    def print_slow(self, str):
        for letter in str:
            sys.stdout.write(letter)
            sys.stdout.flush()
            # time.sleep(0.04)
            time.sleep(0.01)

    def print_very_slow(self, string):
        for letter in string:
            #        Lecture lente
            sys.stdout.write(letter)
    #        Nettoyer
            sys.stdout.flush()
    # Plus rapide ou plus lent (on le mettra à 0.04)
            time.sleep(0.1)

    def print_slow_titre(self):

        self.print_slow(
            "\n_________________________________________________________\n")
        self.print_slow(
            "\n█▀▀ █ █▄░█ ▄▀█ █░░  ▄▀█ █▀▄ █░█ █▀▀ █▄░█ ▀█▀ █░█ █▀█ █▀▀\n")
        self.print_slow(
            "█▀░ █ █░▀█ █▀█ █▄▄  █▀█ █▄▀ ▀▄▀ ██▄ █░▀█ ░█░ █▄█ █▀▄ ██▄\n")
        self.print_slow(
            "\n_________________________________________________________\n")

    def menu(self):
        self.print_slow("\n\t\t[1] Jouer\t\t")
        self.print_slow("\n\t\t[2] Charger une sauvegarde\t\t")
        self.print_slow("\n\t\t[3] Crédits")
        self.print_slow("\n\t\t[4] Quitter\t\t\n\n")
        self.print_slow("DEMO")
        self.print_slow("© by RoVaLoThaChri\n")

    def play(self):
        self.print_slow("\t\nBienvenue dans le monde de Final Adventure\n")
        commencer_le_jeu = input(
            "\tAppuyer sur [ ENTRER ] pour commencer le jeu !\n")

        def compute():
            for i in range(1000):
                time.sleep(0.001)
                yield
        with alive_bar(1000) as bar:
            for i in compute():
                bar()

        while commencer_le_jeu != "":
            self.print_slow("Vous avez fait une erreur.")
            commencer_le_jeu = input()
        self.is_game_run = False

    def load_savegame(self):
        self.print_slow("Cette fonction n'est pas encore definit.\n")

    def credits(self):
        self.print_slow("\n\t\t[ Crédits ]\n")
        self.print_slow("\n\tHistoire & Création des personages - Rosine\n\t")
        self.print_slow("Créations des monstres - Chrisline\n\t")
        self.print_slow("Compétences - Valentin & Chrisline \n\t")
        self.print_slow("Combat - Chrisline\n\t")
        self.print_slow("Carte du jeu - Lorys & Valentin\n\t")
        self.print_slow("Menu Principale - Lorys\n\t")
        self.print_slow("Inventaire - Thari\n\t")
        ("Coordonnées de la carte - Valentin & Rosine\n\t")
        self.print_slow("")

    def back(self):
        return self.menu()

    def choice_input(self):

        while self.is_game_run:
            self.menu()
            choice = int(input("Que voulez-vous faire ? "))
            while choice != 1 and choice != 2 and choice != 3 and choice != 4:
                self.print_slow("Vous avez fait une erreur.\n")
                self.menu()
                choice = int(input("Que voulez-vous faire ? "))

            if choice == 1:
                self.play()

            elif choice == 2:
                self.load_savegame()

            elif choice == 3:
                self.credits()

            elif choice == 4:
                self.print_slow("Vous avez quitté Final Adventure.\n")
                exit()
            else:
                self.print_slow("Sélectionnez parmi les choix proposés !")


m = Menu()
m.print_slow_titre()
m.choice_input()
