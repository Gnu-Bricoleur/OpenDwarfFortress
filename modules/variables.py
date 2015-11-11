import pygame
import numpy as np


# Variables pour l'affichage (non modifie pendant le jeu)
tilesheet = "images/zilk.png"
image_icone = "images/dwarf.png"
floor = "images/DawnLike/Objects/Floor32.png"
pit0="images/DawnLike/Objects/Pit032.png"
hill0="images/DawnLike/Objects/Hill032.png"

taillemaille=20
taille_tile = 32
taillemonde=500
hauteurmonde=30
nombre_sprite_cote_x = 21
nombre_sprite_cote_y = 31
couleur_fond_tile = (255,0,255)
couleur_dessin_tile = (255,255,255)


# Variables globales pour passage d'information (modifie mais reinitialise)
continuer =1
selection=0
choix=0
zonefenetrex=50
zonefenetrey=50
zonefenetrez=10
joueurx=50
joueury=50
joueurz=10
#monde = [[0] * taillemonde for _ in range(taillemonde)]
#monde=[[[0 for i in xrange(taillemonde)] for j in xrange(taillemonde)] for k in xrange(hauteurmonde)]
#monde = [[[0]*hauteurmonde for _ in range(taillemonde)] for _ in range(taillemonde)]
#visible=[[[0 for i in xrange(taillemonde)] for j in xrange(taillemonde)] for k in xrange(hauteurmonde)]
#visible = [[[0]*hauteurmonde for _ in range(taillemonde)] for _ in range(taillemonde)]
monde = np.zeros((taillemonde+1, taillemonde+1, hauteurmonde), dtype='i')
visible = np.zeros((taillemonde+1, taillemonde+1, hauteurmonde), dtype='i')
relief=np.zeros((taillemonde+1, taillemonde+1), dtype='i')
altitude=np.zeros((taillemonde+1,taillemonde+1),dtype='i')

fenetre = pygame.display.set_mode((nombre_sprite_cote_y*taille_tile, nombre_sprite_cote_x*taille_tile))

dejacharge=[]
indentifiant=[]
tilecharge=[]
alea=0
# Base de donne tile
transparence=[0,20,40,60,80,100,120,140,160,180,200,220,240,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255]



dicoid={}
dicoloc={}

dicoid[1111113]="solcraquele"
dicoloc[1111113]=(floor,19,6)
dicoid[1111112]="solherbeuxsec"
dicoloc[1111112]=(floor,12,6)
dicoid[1111111]="solsec"
dicoloc[1111111]=(floor,1,19)
dicoid[0]="rien-erreur"
dicoloc[0]=(floor,16,0)
dicoid[1]="noir"
dicoloc[1]=(floor,10,0)
dicoid[1111114]="eau"
dicoloc[1111114]=(pit0,1,9)
dicoid[1111115]="herbe"
dicoloc[1111115]=(floor,8,7)
dicoid[1111116]="montagne"
dicoloc[1111116]=(hill0,5,1)
dicoid[1111117]="sable"
dicoloc[1111117]=(floor,15,4)
dicoid[1111118]="sommets"
dicoloc[1111118]=(hill0,5,1)
dicoid[1111119]="eauprofonde"
dicoloc[1111119]=(pit0,15,1)


