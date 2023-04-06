import time
import sys

i = "???"
v = "Valentin"
l = "Loic"
a=None

# s.print_slow("")
# s.next()

class Story:

    def __init__(self):
        pass

    def print_slow(self, string):
        for letter in string:
    #        Lecture lente
            sys.stdout.write(letter)
    #        Nettoyer  
            sys.stdout.flush()
    #Plus rapide ou plus lent (on le mettra à 0.04)
            time.sleep(0.01)

    def print_very_slow(self, string):
        for letter in string:
    #        Lecture lente
            sys.stdout.write(letter)
    #        Nettoyer  
            sys.stdout.flush()
    #Plus rapide ou plus lent (on le mettra à 0.04)
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


    def name(self):
        s.print_dialog(f"{l}"," Quel est ton nom ?\n")
        s.next()
#        Voir si cette ligne est instructif        
        s.print_slow("Veuillez entrer votre nom : \n")
        p = input()
        while len(p) < 3 :
            print("Il faut un pseudo d'au moins 3 caractères !")
            p = input()
        s.print_dialog(f"{i}", "C'est bien cela ?",f"{p}"",")
        s.choice("1 - Oui.", "2 - Non.")
        c = int(input())
        while c != 1 and c != 2:
            s.print_slow("Vous avez fait une erreur")
        if c == 1:
            return p
        elif c == 2:
            s.name()

    #Nombre variable si le mot-clé n'est pas passé
    def choice(self, *arguments):
        for c in arguments:
            print("\n", c)

    def next(self):
        a = input() 
        while a != "":
            a = input()

    def open_inventory(self, i):
        if i == "i":
    #        Inventory()
            pass

    def map(self, m):
        if m == "m":
            # Map() 
            pass

    def quit(self, echap):
        if echap == "quit":
            # Quit()
            pass

    def save(self, save):
        if save == "save":
    #         Json_write()
            pass       

s = Story()
# # LE RÊVE
# s.print_slow("L'écho d'un combat fait rage. J'entends des cris, mais je n'arrive pas à les discerner.")
# s.next()

# s.print_slow("Je n'ai pas le temps de regarder ailleurs, des ennemis arrivent. Des poulpes se jettent sur moi mais je les esquive avec aisance, ma rapidité me permet d'être à l'aise sur l'eau.")
# s.next()

# s.print_dialog(f"{i}", "Le Médaillon de L**** fonctionne parfaitement !")
# s.next()

# s.print_slow("\nMais en tentant d'esquiver l'un d'eux, je trébuche lamentalement sur un poisson, rendant toutes mes actions précédente inutile.")
# s.next()

# s.print_slow("À cet instant, un poulpe m'attrape la jambe et me tire dans les profondeurs des abysses.")
# s.next()

# s.print_slow("Avant d'être immerger, je vois au loin une immense silhouette ressemblant à un pouple humanoïde géante.")
# s.next()

# s.print_slow("Son cri était tellement puissant que toute la caverne se mit à trembler.")
# s.next()

# s.print_very_slow("\n...\n")
# s.next()
# # DANS L'ECOLE
# s.print_slow("Je sursaute et manque de tomber de ma chaise. La salle était vide et tous les élèves étaient déjà rentrer.")
# s.next()

# s.print_slow("La sonnerie retentit et une voix annonce la fermeture de l'école dans quelques minutes.")
# s.next()

# s.print_dialog(f"{i}","Tiens, tu es encore ? Est-ce que tu pourrais ranger ses livres dans la bibliothèque avant de rentrer, s'il te plait ?")
# s.next()

# s.print_slow("Sans même me laisser le temps de répondre, le professeur s'en alla. \n")
# s.next()

# s.print_slow("Je me lève difficilement après ma sieste cauchemardesque.")
# s.next()

# s.print_slow("Le calme de l'école lui donnait un air abandonnée, cependant les quelques cris de la cour me soulager, je n'étais pas seul.")
# s.next()

# s.print_slow("Je prends mes affaires et les livres que mon professeur m'a demandé d'apporter.\n")
# s.next()
# #   LE COULOIR
# s.print_slow("Les couloirs sont vides, la lumière du soleil qui se couche me donne envie de reprendre ma sieste.")
# s.next()

# s.print_slow("Je pousse lentement la porte de la bibliothèque et l'odeur du bois me chatouille les narines.")
# s.next()

# s.print_slow("Voyant que la fermeture approche à grand pas, je dépose les livres rapidement et manque le livre qui s'était accroché à ma manche.")
# s.next()

# s.print_slow("Le bouquin tombe avec un bruit sourd et s'ouvre, le dessin d'un tétagramme apparaît.\n")
# s.next()

# s.print_slow("Voulez-vous ramasser le bouquin?\n")
# #Essayer de mettre en ralentie(mais fonctionne pas)
# s.choice(("1. Oui."), ("2. Non."))
# c = int(input())

# while c != 1 and c != 2:
#     s.print_slow("Vous avez fait une erreur")
#     c = int(input())

# if c == 1:
#     s.print_slow("Je tends ma main pour ramasser le bouquin et mes doigts frôlent le tétagramme.")
#     s.next()
#     s.print_very_slow("\n...")
#     s.print_slow("\nSoudainement une lumière blanche envahie la pièce et je ferme mes yeux malgré moi.")
#     s.next()

# elif c == 2:
#     s.print_slow("Je dépose mes derniers livres et me précipite vers la sortie, la sortie annonçant la fermeture de l'établissement retentie.")
#     s.next()
#     s.print_very_slow("\n...")
#     s.next()
#     s.print_slow("\nSoudainement une lumière blanche envahie la pièce et je ferme mes yeux malgré moi.")
#     s.next()
#     s.print_slow("Sans même ouvrir les yeux, je sens que je tombe et me cogne les fesses.\n")
#     s.next()
#     #Perte de 10 PV.

# s.print_very_slow("...\n")
# s.next()

# s.print_slow("Mes yeux me piquent encore à cause de la lumière, j'entends des cris, des pleurs et des rires et même le bruit...")
# s.next()
# s.print_dialog(f"{p}"," Du feu...?")
# s.next()
# s.print_dialog(f"{i}", "ATTENTION !\n")
# s.next()
# s.print_slow("Deux bruits de métaux s'entrechoquent juste en face de moi.")
# s.next()
# s.print_slow("J'ouvre les yeux et je vois une silhouette qui fait deux têtes de plus que moi, quand mes yeux s'habitue finalement à la lumière tamisée, je peux discener des...oreilles?")
# s.next()
# s.print_slow("L'homme tourne sa tête vers moi, je vois sur son visage un groin.")
# s.next()
# s.print_dialog(f"{p}"," Un cochon ?!")
# s.next()
# s.print_dialog(f"{i}"," Dépêche-toi de te lèver.\n")
# s.next()
# s.print_slow("J'exécute sans broncher et en reculant, ma main touche quelque chose de doux.")
# s.next()
# s.print_slow("Je sursaute.")
# s.next()
# s.print_dialog(f"{i}", "Tu m'as l'air bien compétent, tu devrais pouvoir aider, Valentin.\n")
# s.next()
# s.print_slow("Je me retourne afin de voir que ce que je viens de toucher était un mélange de ... cheval-lion qui...parle ?")
# s.next()
# s.print_dialog(f"{v}","Tiens, attrape ça.\n")
# s.next()
# s.print_slow("Avant même de pouvoir terminer mon observation de l'incroyable animal, je me retourne pour regarder le dénommé Valentin.")
# s.next()
# s.print_slow("Le cochon me lance une épée usée que j'esquive de justesse. La lame se plante dans la terre.")
# s.next()
# s.print_slow("Je lève mon regard dans sa direction, choquer par ce qui vient de se passer, mais le cochon était déjà prêt au combat.")
# s.next()
# s.print_slow("Il avait raison, un monstre était en train de foncer tout droit sur nous.")

#AJOUT DU TUTO COMBAT
#TUTO COMBAT()

# s.print_very_slow("\n...Quelques heures plus tard...\n")
# s.next()
# s.print_slow("Je suis épuiser, je m'assois au sol après toutes les batailles qu'on vient de mener.")
# s.next()
# s.print_slow("Tout mon corps me fait mal, mais je relève ma tête pour enfin pouvoir visionner l'endroit dans lequel je suis.")
# s.next()
# s.print_slow("C'est un village comme dans les jeux vidéos ou dans les histoires fantastique qu'on trouve dans les bouquins.")
# s.next()
# s.print_slow("Toutes les maisons sont faites de bois et ils avaient tous pris feu. Des corps de monstres et d'humains longaient le sol.")
# s.next()

# s.print_dialog(f"{i}"," Comment vas-tu ?")
# s.next()
# s.choice("1 - Je vais bien, merci.", "2 - Comment peux-tu me demander ça ?!")
# c = int(input())
# while c != 1 and c != 2:
#     s.print_slow("Vous avez fait une erreur")
#     c = int(input())
# s.print_dialog(f"{v}"," Je suis désolé d'interrompre votre discussion, mais Loic, nous avons des gens à sauver.")
# s.next()
# s.print_slow("Je pouvais enfin poser un nom sur cette créature mythique, Loic.")
# s.next()
# s.print_slow("Il relève la tête vers celui qui vient de l'interpeler et soupir.")
# s.next()
# s.print_dialog(f"{l}", " Je sais. Mais tu ne peux pas sauver ce village tout seul.")
# s.next()
# s.print_dialog(f"{v}", " Que veux-tu dire par là?\n")
# s.next()
s.print_slow("Loic ne répond pas, à la place, il se tourne vers moi.")
s.next()
s.print_slow("Je sens les ennuie arriver.")
s.next()

p = s.name()
s.print_dialog(f"{i}"," Ravie de te rencontrer, "f"{p}")
s.next()
s.print_dialog(f"{l}", " Je m'appelle Loic et voici mon compagnon de voyage, Valentin.\n")
s.next()
s.print_slow("Je lance un regard à Valentin, il me met légèrement mal à l'aise, contrairement à Loic qui est beaucoup plus prévenant.")
s.next()
s.print_dialog(f"{l}", " Je ne vais pas passer par quatre chemins, on a besoin de ton aide.")
s.next()
s.print_dialog(f"{l}", " Tu es doué au combat. Aide-nous à sauver le village.\n")
s.next()
s.print_slow("Il avait trop d'informations.")
s.next()
s.print_slow("Beaucoup trop d'informations.\n")
s.next()
s.print_slow("Soudain, un cri retentit. Je n'avais pas le temps de réfléchir, des gens avaient besoin d'aide.")
s.next()
s.print_slow("De mon aide.")
s.next()
s.print_slow("Et moi, j'avais aussi besoin d'eux pour comprendre ma situation.")
s.next()
s.print_dialog(f"{p}", " Je vous accompagne.")
s.next()





