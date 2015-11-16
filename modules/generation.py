import random
from math import *
from modules.base import *
from modules.variables import *
import noise

def creationmonde():
	print("### GENERATION ###")
	heightmap()
	sol()
	visibilite()	
	sauv(monde,"sauvegardes/sauvmonde.txt")
	sauv(visible,"sauvegardes/sauvvisu.txt")
	sauv2D(altitude,"sauvegardes/sauvaltitude.txt")
	sauv2D(relief,"sauvegardes/sauvrelief.txt")

def heightmap():
	i,j=0,0
	while i < taillemonde:
		while j < taillemonde:
			relief[i][j]=(int(noise.snoise2(i / freq, j / freq, octaves)*14.0 + 15.0))
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


