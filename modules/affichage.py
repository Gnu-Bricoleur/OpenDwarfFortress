import random
from modules.variables import *



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



def creationdicofloorsheet():
	dicofloorsheet={}
	dicofloorsheet[floor]=load_tile_table(floor,taille_tile,taille_tile)
	dicofloorsheet[pit0]=load_tile_table(pit0,taille_tile,taille_tile)
	dicofloorsheet[hill0]=load_tile_table(hill0,taille_tile,taille_tile)
	return dicofloorsheet


def afficher(x,y,z,dicofloorsheet):
	i,j,k=0,0,0
#	print(x)
#	print(y)
	while i<nombre_sprite_cote_y:
		while j<nombre_sprite_cote_x:
			intermediaire=visible[i+x][j+y][z]
			dic=dicoloc[intermediaire]
			mx=dic[1]
			my=dic[2]
			floorsheet=dicofloorsheet[dic[0]]
#			print(str(mx)+" "+str(my))
			tile=floorsheet[mx][my]
			if z>altitude[x+i][y+j]:
				tile.set_alpha(transparence[altitude[x+i][y+j]-z])
			fenetre.blit(tile, (i*taille_tile, j*taille_tile))
			j=j+1
		j=0
		i=i+1
		

def captureimage(dicofloorsheet):
	i,j,z=0,0,29
	capture = pygame.Surface((taille_tile*taillemonde,taille_tile*taillemonde))
	while i<taillemonde:
		while j<taillemonde:
			intermediaire=visible[i][j][z]
			dic=dicoloc[intermediaire]
			mx=dic[1]
			my=dic[2]
			floorsheet=dicofloorsheet[dic[0]]
			tile=floorsheet[mx][my]
			capture.blit(tile, (i*taille_tile, j*taille_tile))
			j=j+1
		j=0
		i=i+1
	pygame.image.save(capture,"captures/capture.png")
