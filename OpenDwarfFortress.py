#!/usr/bin/python3
# -*- coding: Utf-8 -*-

import os, sys
import pygame
from pygame.locals import *
import random
from modules.variables import *
from modules.generation import *
from modules.base import *
from modules.personnage import *
from modules.affichage import *
import numpy as np

#------------------------Initialisations
print("Bienvenue dans Open Dwarf Fortress !")
pygame.init()
if not pygame.font: print('Warning, fonts disabled')
if not pygame.mixer: print('Warning, sound disabled')

icone = pygame.image.load(image_icone)
pygame.display.set_icon(icone)
pygame.display.set_caption("ODF v0.1")
fenetre.fill((255, 255, 255))

fond = pygame.image.load("images/desert.png").convert()

fenetre.blit(fond, (0,0))

#-------------------------Menu
print("### MENU ###")
if pygame.font:
	font = pygame.font.Font("SDS.ttf", 36)
	text = font.render("Open Dwarf Fortress v0.1", 1, (10, 10, 10))
	textpos = (100,50)
	fenetre.blit(text, textpos)
	
	font = pygame.font.Font("SDS.ttf", 18)
	texta = font.render("(a)-Nouvelle partie", 1, (10, 10, 10))
	textz = font.render("(z)-Charger ancienne partie", 1, (10, 10, 10))
	texte = font.render("(e)-Quitter", 1, (10, 10, 10))
	textr = font.render("(r)-Tests", 1, (10, 10, 10))
	textposa = (200,200)
	textposz = (200,220)
	textpose = (200,240)
	textposr = (200,260)
	fenetre.blit(texta, textposa)
	fenetre.blit(textz, textposz)
	fenetre.blit(texte, textpose)
	fenetre.blit(textr, textposr)
	
	font = pygame.font.Font("SDS.ttf", 8)
	text = font.render("credits : Sylvain Migaud pour la programmation et DragonDePlatino pour les graphiques", 1, (10, 10, 10))
	textpos = (50,400)
	fenetre.blit(text, textpos)
	pygame.display.flip()

font = pygame.font.Font("SDS.ttf", 18)

while continuer:
	for event in pygame.event.get():   
		if event.type == QUIT:     
			continuer = 0  
		if event.type == KEYDOWN:
			if event.key == K_e:
				texte = font.render("(e)-Quitter", 1, (255, 10, 10))
				textpose = (200,240)
				fenetre.blit(texte, textpose)
				selection=0
			if event.key == K_a:
				texta = font.render("(a)-Nouvelle partie", 1, (10, 255, 10))
				textposa = (200,200)
				fenetre.blit(texta, textposa)
				choix=1
			if event.key == K_z:
				textz = font.render("(z)-Charger ancienne partie", 1, (10, 10, 255))
				textposz = (200,220)
				fenetre.blit(textz, textposz)
				choix=2
			if event.key == K_r:
				textz = font.render("(r)-Tests", 1, (255, 10, 255))
				textposz = (200,260)
				fenetre.blit(textz, textposz)
				choix=3
			if event.key == K_RETURN and choix != 0:
				continuer=0
			pygame.display.flip()
				
#--------------------------Boucle du jeu

font = pygame.font.Font("SDS.ttf", 30)
fenetre.fill((255, 255, 255))
texte = font.render("Chargement . . . .", 1, (10, 10, 10))
textpose = (200,240)
fenetre.blit(texte, textpose)



pygame.display.flip()
dicofloorsheet=creationdicofloorsheet()
if choix !=0:
	continuer=1
	if choix == 1:
		print(">> Nouveau monde")
		creationmonde()
		afficher(zonefenetrex,zonefenetrey,zonefenetrez,dicofloorsheet)
	if choix == 3:
		print(">> Nouveau monde")
		taillemonde=500
		heightmap()
		visibilite()
		sol()
		afficher(zonefenetrex,zonefenetrey,zonefenetrez,dicofloorsheet)
	else:
		print(">> Chargement")
		charge(monde,"sauvegardes/sauvmonde.txt")
		charge(visible,"sauvegardes/sauvvisu.txt")
		charge2D(altitude,"sauvegardes/sauvaltitude.txt")
		afficher(zonefenetrex,zonefenetrey,zonefenetrez,dicofloorsheet)
	pygame.display.flip()
	print(">> Affichage !!!")
	print("### JEU ###")
	pygame.event.wait()
	pygame.key.set_repeat(500,50)
	while continuer:
		for event in pygame.event.get():   
			if event.type == QUIT:     
				continuer = 0  
			if event.type == KEYDOWN:
				if event.key == K_RIGHT:
					if zonefenetrex>0:
						zonefenetrex = zonefenetrex-1
						fenetre.fill((255, 255, 255))
						afficher(zonefenetrex,zonefenetrey,zonefenetrez,dicofloorsheet)
						pygame.display.flip()
				if event.key == K_LEFT:
					if zonefenetrex<taillemonde:
						zonefenetrex = zonefenetrex+1
						fenetre.fill((255, 255, 255))
						afficher(zonefenetrex,zonefenetrey,zonefenetrez,dicofloorsheet)
						pygame.display.flip()
				if event.key == K_UP:
					if zonefenetrey<taillemonde:
						zonefenetrey = zonefenetrey+1
						fenetre.fill((255, 255, 255))
						afficher(zonefenetrex,zonefenetrey,zonefenetrez,dicofloorsheet)
						pygame.display.flip()
				if event.key == K_DOWN:
					if zonefenetrey>0:
						zonefenetrey = zonefenetrey-1
						fenetre.fill((255, 255, 255))
						afficher(zonefenetrex,zonefenetrey,zonefenetrez,dicofloorsheet)
						pygame.display.flip()
				if event.key == K_x:
					if zonefenetrez>0:
						zonefenetrez = zonefenetrez-1
						fenetre.fill((255, 255, 255))
						afficher(zonefenetrex,zonefenetrey,zonefenetrez,dicofloorsheet)
						pygame.display.flip()
				if event.key == K_w:
					if zonefenetrez+1<hauteurmonde:
						zonefenetrez = zonefenetrez+1
						fenetre.fill((255, 255, 255))
						afficher(zonefenetrex,zonefenetrey,zonefenetrez,dicofloorsheet)
						pygame.display.flip()
