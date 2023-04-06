from alive_progress import alive_bar
import time


def compute():
    for i in range(1000):
        time.sleep(0.01)
        if i == 250:
            print("Chargement 25%")
        if i == 500:
            print("Chargement 50%")
        if i == 750:
            print("Chargement 75%")
        if i == 999:
            print("Chargement 99,9%(")
        yield


with alive_bar(1000) as bar:
    for i in compute():
        bar()

print("fin de la fonction play()")
print("Fin de la partie")
is_game_run = False
