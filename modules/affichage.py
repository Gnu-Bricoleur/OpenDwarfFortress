import random
from variables import *



def load_tile_table(filename, width, height):
    image = pygame.image.load(filename).convert()
    image_width, image_height = image.get_size()
    tile_table = []
    for tile_x in range(0, int(image_width/width)):
        line = []
        tile_table.append(line)
        for tile_y in range(0, int(image_height/height)):
            rect = (tile_x*width, tile_y*height, width, height)
            line.append(image.subsurface(rect))
    return tile_table


#def poser(tilex,tiley,r,g,b,ar,ag,ab,x,y):
#	i,j=0,0
#	table = load_tile_table(tilesheet, taille_tile,taille_tile)
#	floorsheet = load_tile_table(floor,taille_tile,taille_tile)
#	t=table[tilex]
#	tile=t[tiley]
#	t=floorseet[tilex]
#	tile=t[tiley]
#	image_width, image_height = tile.get_size()
#	while i<image_width:
#		while j<image_height:
#			
#			if tile.get_at((i,j)) == couleur_dessin_tile:
#				tile.set_at((i,j),(r,g,b))
#				
#			if tile.get_at((i,j)) == couleur_fond_tile:
#				tile.set_at((i,j),(ar,ag,ab))
#				
#			j=j+1
#		i=i+1
#		j=0
#	tilecharge.append(tile)
#	fenetre.blit(tile, (x*taille_tile, y*taille_tile))


def creationdicofloorsheet():
	dicofloorsheet={}
	dicofloorsheet[floor]=load_tile_table(floor,taille_tile,taille_tile)
	dicofloorsheet[pit0]=load_tile_table(pit0,taille_tile,taille_tile)
	dicofloorsheet[hill0]=load_tile_table(hill0,taille_tile,taille_tile)
	return dicofloorsheet


def afficher(x,y,z,dicofloorsheet):
	i,j,k=0,0,0
	print(x)
	print(y)
	while i<nombre_sprite_cote_y:
		while j<nombre_sprite_cote_x:
			intermediaire=visible[i+x][j+y][z]
			dic=dicoloc[intermediaire]
			mx=dic[1]
			my=dic[2]
			floorsheet=dicofloorsheet[dic[0]]
			tile=floorsheet[mx][my]
			if z>altitude[x+i][y+j]:
				tile.set_alpha(transparence[altitude[x+i][y+j]-z])
			fenetre.blit(tile, (i*taille_tile, j*taille_tile))
			j=j+1
		j=0
		i=i+1
