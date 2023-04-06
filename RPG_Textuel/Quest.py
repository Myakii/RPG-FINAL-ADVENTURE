import sys
import time
import json
from Mapped import *


def json_quest(pnj_name):
    with open('resources\\json_datas\\quest.json', "r", encoding='utf-8') as f:
        data = json.load(f)
    get_quest = data['QuestNPC']
    get_pnj = get_quest[0]
    return get_pnj[pnj_name]


class Quest:
    def __init__(self, info_pnj):
        self.name = info_pnj['name']
        self.choice1 = info_pnj["choice"]["option1"]
        self.choice2 = info_pnj["choice"]["option2"]
        self.description = info_pnj['description']
        self.quest = info_pnj['quest']
        self.reward = info_pnj['reward']
        self.quest_item = info_pnj['quest_item']
        self.answer = info_pnj['answer']
        self.quest_item_get = False
        self.is_done = False

        # ↓ Tout ce qui est en rapport avec le côté dialogue, écriture...

    def print_slow(self, string):
        for letter in string:
            #        Lecture lente
            sys.stdout.write(letter)
    #        Nettoyer
            sys.stdout.flush()
    # Plus rapide ou plus lent (on le mettra à 0.04)
            time.sleep(0.01)

    def print_very_slow(self, string):
        for letter in string:
            #        Lecture lente
            sys.stdout.write(letter)
    #        Nettoyer
            sys.stdout.flush()
    # Plus rapide ou plus lent (on le mettra à 0.04)
            time.sleep(0.1)

    def print_dialog(self, sujet, text, *person):
        a = ""
        for s in sujet:
            a += s + ""
        if len(person) == 0:
            self.print_slow(f"\n\t{a}: {text}")
        else:
            for p in person:
                self.print_slow(f"\n\t{a}: {p} {text}")

    def get_name(self):
        return self.name

    def quest_status(self):
        return self.is_done

    def get_quest(self):
        return self.quest

    def get_yes(self):
        return self.choice1

    def get_description(self):
        return self.description

    def get_no(self):
        return self.choice2

    def get_quest_item(self):
        return self.quest_item

    def get_reward(self):
        return self.reward

    def get_answer(self):
        return self.answer


# quest1 = Quest(json_quest("Jiek"))
# #lancement de la quête tile (3.2)
# quest1.get_quest()
# #choix 1 oui
# quest1.get_yes()
# #choix 2 NAN
# quest1.get_no()
# #objet de quête tile (2.4)
# quest1.get_quest_item()
# #Fin de quête en tile (3.2)⫰
# quest1.get_answer()
# quest1.get_reward()
# #quest1.is_done = True

# print(quest1.get_quest())
# print(quest1.get_quest_item())
