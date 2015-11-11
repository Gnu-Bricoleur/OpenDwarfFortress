import random
from math import *
from base import *
from variables import *


def creationmonde():
	print("### GENERATION ###")
	heightmap()	
	visibilite()
	sol()
	sauv(monde,"sauvegardes/sauvmonde.txt")
	sauv(visible,"sauvegardes/sauvvisu.txt")
	sauv2D(altitude,"sauvegardes/sauvaltitude.txt")
	
def heightmap():
	i,j,k,a,b,c,d,da,db,dc,dd=0,0,0,0,0,0,0,0,0,0,0
	nbmontagnes,nblacs=3,3
	while k<nbmontagnes:
		relief[random.randint(0,(taillemonde//taillemaille)*taillemaille)][random.randint(0,(taillemonde//taillemaille)*taillemaille)]=29
		k=k+1
	k=0
	while k<nblacs:
		relief[random.randint(0,(taillemonde//taillemaille)*taillemaille)][random.randint(0,(taillemonde//taillemaille)*taillemaille)]=0
		k=k+1
	while i <= taillemonde:
		while j <= taillemonde:
			xa,ya=(i//taillemaille)*taillemaille,(j//taillemaille)*taillemaille
			xb,yb=taillemaille+(i//taillemaille)*taillemaille,(j//taillemaille)*taillemaille
			xc,yc=taillemaille+(i//taillemaille)*taillemaille,taillemaille+(j//taillemaille)*taillemaille
			xd,yd=(i//taillemaille)*taillemaille,taillemaille+(j//taillemaille)*taillemaille
			print(xa)
			print(ya)
			if relief[xa][ya]==29 or relief[xb][yb]==29 or relief[xc][yc]==29 or relief[xd][yd]==29:
				relief[i][j]=random.randint(15,25)
			elif relief[xa][ya]==0 or relief[xb][yb]==0 or relief[xc][yc]==0 or relief[xd][yd]==0:
				relief[i][j]=random.randint(4,8)
			else:
				relief[i][j]=random.randint(9,14)
			j=j+taillemaille
		j=0
		i=i+taillemaille
	i,j=0,0
	
	while i < taillemonde:
		while j < taillemonde:
			if not(i%taillemaille==0 and j%taillemaille==0):
#				on prend la troncature de la valeur de chaque point de la grille de maille "taillemaille" representant un sommet du carre dans lequel est notre pts
#				et on le multiplie par la distance a ce sommet (comprise entre 0 et 1) et on fait la moyenne 
#				xa,ya=(i//10)*10,(j//10)*10
#				xb,yb=10+(i//10)*10,(j//10)*10
#				xc,yc=10+(i//10)*10,10+(j//10)*10
#				xd,yd=(i//10)*10,10+(j//10)*10
#				da=sqrt(carre(i-xa)+carre(j-ya))
#				db=sqrt(carre(xb-i)+carre(j-yb))
#				dc=sqrt(carre(xc-i)+carre(yc-j))
#				dd=sqrt(carre(i-xd)+carre(yd-j))
#				a=relief[xa][ya]
#				b=relief[xb][yb]
#				c=relief[xc][yc]
#				d=relief[xd][yd]
#				relief[i][j]=((a*da+b*db+c*dc+d*dd)/7)//4
#				relief[i][j]=relief[i][j]//4
#				autre technique : interpollation billineaire (wikipedia)
				xa,ya=(i//taillemaille)*taillemaille,(j//taillemaille)*taillemaille
				xb,yb=taillemaille+(i//taillemaille)*taillemaille,(j//taillemaille)*taillemaille
				xc,yc=taillemaille+(i//taillemaille)*taillemaille,taillemaille+(j//taillemaille)*taillemaille
				xd,yd=(i//taillemaille)*taillemaille,taillemaille+(j//taillemaille)*taillemaille
				fxy1,fxy2,fxy=12.223,12.3467,12.4567
				fxy1=((xc-i)/(float(xc-xd)))*relief[xd][yd]+((i-xd)/(float(xc-xd)))*relief[xc][yc]
				fxy2=((xc-i)/(float(xc-xd)))*relief[xa][ya]+((i-xd)/(float(xc-xd)))*relief[xb][yb]
				fxy=((j-yd)/(float(ya-yd)))*fxy1+((ya-j)/(float(ya-yd)))*fxy2
				relief[i][j]=int(fxy)
			j=j+1
		j=0
		i=i+1
	
def carre(a):
	return a*a

def sol():
	i,j=0,0
	alpha,rab=0,0
	while i < taillemonde:
		while j < taillemonde:
			if relief[i][j]<=5:
				monde[i][j][relief[i][j]]=1111119
			elif 5<relief[i][j]<9:
				monde[i][j][relief[i][j]]=1111114
			elif relief[i][j]==9:
				monde[i][j][relief[i][j]]=1111117
			elif 9<relief[i][j]<=14:
				monde[i][j][relief[i][j]]=1111115
			elif 14<relief[i][j]<=25:
				monde[i][j][relief[i][j]]=1111116
			else:
				monde[i][j][relief[i][j]]=1111118
			j=j+1
		j=0
		i=i+1

#def vegetationplaine():
#	i,j=0,0
#	alpha,rab=0,0
#	while i < taillemonde:
#		while j < taillemonde:
#			if monde[i][j][10]==1111111:
#				alea = random.randint(1,5)
#				if alea == 1:
#					monde[i][j][10]=1111112
#			j=j+1
#		j=0
#		i=i+1
#	
#	i,j=0,0
#	alpha,rab=0,0
#	while i < taillemonde:
#		while j < taillemonde:
#			if monde[i][j][10]==1111111:
#				alea = random.randint(1,10)
#				if alea == 1:
#					monde[i][j][10]=1111113
#			j=j+1
#		j=0
#		i=i+1


def visibilite():
	i,j,k,limite=0,0,0,0
	while i<taillemonde:
		while j<taillemonde:
			while k<hauteurmonde:
				if monde[i][j][k] != 0:
					limite=k
				k=k+1
			k=0
			altitude[i][j]=limite
			while k<hauteurmonde:
				if k<limite:
					visible[i][j][k]=1
				if k>=limite:
					visible[i][j][k]=monde[i][j][limite]
				k=k+1
			k=0
			j=j+1
		j=0
		i=i+1


