import pygame
import os
import json
from pygame.locals import *
from Character import *
from Monster import *


pygame.init()
clock = pygame.time.Clock()
fps = 60


#
bottom_panel = 150
panel_jutsu = 150
screen_width = 1280
screen_height = 720

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("FINAL ADVENTURE")


# Chargement du jeu
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "ressources/images")
# self.image = pygame.image.load(os.path.join(img_folder, "Chrisline_Behind_0.png")).convert()
# Background image
background_img = pygame.image.load(os.path.join(
    img_folder, 'Fire_Village.jpg')).convert_alpha()
# Panel image
panel_img = pygame.image.load(os.path.join(
    img_folder, 'panel.png')).convert_alpha()
panel_2 = pygame.image.load(os.path.join(
    img_folder, 'panel_jutsu.png')).convert_alpha()
# game_folder = os.path.dirname(__file__)
# img_folder = os.path.join(game_folder, "../Images")
# #background image
# background_img = pygame.image.load(img_folder,'Fire_Village.jpg').convert_alpha()
# panel image
# panel_img = pygame.image.load(img_folder,'panel_hp.jpg').convert_alpha()
# #button images
# potion_img = pygame.image.load(img_folder,'Potion_de_soin.png').convert_alpha()
# restart_img = pygame.image.load(img_folder,'restart.png').convert_alpha()
# #load victory and defeat images
# victory_img = pygame.image.load(img_folder,'chest.png').convert_alpha()
# defeat_img = pygame.image.load(img_folder,'58ee7c023545163ec1942ca9.png').convert_alpha()
# #sword image
# sword_img = pygame.image.load(img_folder,'Chram_taillenormal.gif').convert_alpha()


def draw_bg():
    screen.blit(background_img, (0, 0))

# Fonction pour le panel


def draw_panel():
    screen.blit(panel_img, (0, screen_height - bottom_panel))


def draw_panel_2():
    #   screen.blit(panel_2,(Horizontal,Vertical))
    screen.blit(panel_2, (900, 570))

# Classe Fighter


class Fighter(Character):
    def __init__(self, x, y, info_perso, potions):
        super().__init__(info_perso)
        img_folder = os.path.join(game_folder, "ressources\images\characters")
        self.alive = True
        self.animation_list = [
            pygame.image.load(os.path.join(
                img_folder, "Heros\\hero_behind\\Hero_Behind_0.png")).convert_alpha(),
            pygame.image.load(os.path.join(
                img_folder, "Heros\\hero_behind\\Hero_Behind_1.png")).convert_alpha(),
            pygame.image.load(os.path.join(
                img_folder, "Heros\\hero_behind\\Hero_Behind_2.png")).convert_alpha(),
            pygame.image.load(os.path.join(
                img_folder, "Heros\\hero_behind\\Hero_Behind_3.png")).convert_alpha(),
            pygame.image.load(os.path.join(
                img_folder, "Heros\\hero_behind\\Hero_Behind_4.png")).convert_alpha(),
            pygame.image.load(os.path.join(
                img_folder, "Heros\\hero_behind\\Hero_Behind_5.png")).convert_alpha(),
            pygame.image.load(os.path.join(
                img_folder, "Heros\\hero_behind\\Hero_Behind_6.png")).convert_alpha(),
            pygame.image.load(os.path.join(
                img_folder, "Heros\\hero_behind\\Hero_Behind_7.png")).convert_alpha(),
        ]
        for i in self.animation_list:
            img = pygame.image.load(os.path.join(
                img_folder, "Heros\\hero_behind\\Hero_Behind_0.png")).convert_alpha(),
            # img = pygame.transform.scale(
            #     img, (img.get_width()*3, img.get_heigth()*3))
            self.animation_list.append(img)

        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()
        for i in range(8):
            img = pygame.image.load(os.path.join(
                img_folder, 'Hero_Behind_0.png')).convert_alpha()
        # img = pygame.transform.scale(
            # img, (img.get_width()*3, img.get_heigth()*3))
        self.animation_list.append(img)
        self.image = self.animation_list[self.frame_index]
        self.start_potions = potions
        self.potions = potions
#        img = pygame.image.load(os.path.join(img_folder,'cochon_0.png')).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self):
        animation_cooldown = 100
        # Vérifier si le temps est passé depuis la dernière mise à jour
        self.image = self.animation_list[self.frame_index]
        if pygame.time.get_ticks() - self.update_time > animation_cooldown:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
        # Si animation est en cours, il sera reset depuis le début
        if self.frame_index >= len(self.animation_list):
            self.frame_index = 0

    def draw(self):
        screen.blit(self.image, self.rect)


class Monster(Monster):
    def __init__(self, x, y, info_monster):
        super().__init__(info_monster)
        self.alive = True
        img = pygame.image.load(os.path.join(
            img_folder, 'cochon_0.png')).convert_alpha()
        img = pygame.image.load(os.path.join(
            img_folder, "slime-rose_00.png")).convert_alpha()
        # img = pygame.transform.scale(
        #     img, (img.get_width()*3, img.get_heigth()*3))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def draw(self):
        screen.blit(self.image, self.rect)


Heros = Fighter(500, 600, json_class("Heros"), 3)
# print(Heros.get_name())
# pig = Monster(Horizontal(+ = >,- = <),Vertical(+ = Bas, - = Haut))
pig = Monster(350, 200, json_monster("4"))
# pink_slime = Monster(450, 200,json_monster("2"))
pig2 = Monster(950, 200, json_monster("4"))

monster_list = []
monster_list.append(pig)
monster_list.append(pig2)
# monster_list.append(pink_slime)


run = True

while run:

    clock.tick(fps)
    # draw background
    draw_bg()

# draw panel
    draw_panel()

    draw_panel_2()

# drawn fighter
    Heros.update()
    Heros.draw()
    for pig in monster_list:
        pig.draw()
        # for pink_slime in monster_list:
        #     pink_slime.draw()

    continuer = 1

    while continuer:
        for event in pygame.event.get():
            if event.type == QUIT:
                continuer = 0

pygame.display.update()
pygame.quit()
