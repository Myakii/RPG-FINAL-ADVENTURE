from Inventory import *
from Item import *


class Item_quest:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name


def sales_item():
    shop_potion_hp = Item_quest('Potion de vie')
    shop_ankh = Item_quest('Ankh')

    while True:
        print("\nQuel type d'item souhaitez-vous acheter ?\n")
        print("[1] Potion[20 gold.]")
        print("[2] Ankh[1500 gold.]")
        print("[3] Quitter")
        item_choice = input()
        if item_choice == "1" and inventory.get_gold() >= 20:
            print("Vous avez acheté une potion.")
            for key, value in inventory.get_inventory().items():
                if key.get_name() == shop_potion_hp.get_name():
                    inventory.update_item(shop_potion_hp, 1)
                    inventory.set_gold(-key.get_price())
        elif item_choice == "2" and inventory.get_gold() >= 1500:
            print("Vous avez acheté un Ankh.")
            for key, value in inventory.get_inventory().items():
                if key.get_name() == shop_ankh.get_name():
                    inventory.update_item(shop_ankh, 1)
                    inventory.set_gold(-key.get_price())
        elif item_choice == "3":
            return

        else:
            print("Vous avez fait une erreur.")
            # une foix que vous avez avez acheter votre item vous avez a nouveau une proposition
        return_choice = input(
            "[1] Acheter un autre item\n[2] Retour\n")
        if return_choice == "1":
            print("\nQuel type d'item souhaitez-vous acheter ?\n")
            print("[1] Potion[20 gold.]")
            print("[2] Ankh[1500 gold.]")
            print("[3] Quitter")
            item_choice = input()
            if item_choice == "1" and inventory.get_gold() >= 20:
                print("Vous avez acheté une potion.")
                for key, value in inventory.get_inventory().items():
                    if key.get_name() == shop_potion_hp.get_name():
                        inventory.update_item(shop_potion_hp, 1)
                        inventory.set_gold(-key.get_price())
            elif item_choice == "2" and inventory.get_gold() >= 1500:
                print("Vous avez acheté un Ankh.")
                for key, value in inventory.get_inventory().items():
                    if key.get_name() == shop_ankh.get_name():
                        inventory.update_item(shop_ankh, 1)
                        inventory.set_gold(-key.get_price())
        elif item_choice == "2":
            return
        else:
            print("Vous avez fait une erreur.")


# fonction de vente du PNJ


def sales():
    print("\tSofia : Bonjour voyageur,\nvoulez-vous acheter quelque chose ?\n")
    # input pour choisir une option (avec information des touches à appuyer)
    choice = input("[1] Acheter\n[2] Quitter ")
    if choice == "1":
        sales_item()
    # ce choix permet de quitter le shop
    elif choice == "2":
        print("Sofia : À bientôt !")
    # vous avez fait un choix indisponible ou inexistant
    else:
        print("Vous avez fait une erreur.")
        sales()
