import random
from variables import *
import os, sys

def sauv(tableau,cheminfichier):
	sauv=open(cheminfichier,"w")
	i,j,k=0,0,0
	while i<taillemonde:
		while j<taillemonde:
			while k<hauteurmonde:
			#for item in monde[i][j]:
				inter=str(tableau[i][j][k]) + "\n"
				sauv.write(inter)
				k=k+1
			j=j+1
			k=0
		j=0
		i=i+1
	sauv.close()

def charge(tableau,cheminfichier):
	sauv=open(cheminfichier,"r")
	i,j,k=0,0,0
	while i<taillemonde:
		while j<taillemonde:
			while k<hauteurmonde:
				inter = int(sauv.readline().rstrip('\n\r'))
				tableau[i][j][k] = inter
				k=k+1 
			j=j+1
			k=0
		j=0
		i=i+1
	sauv.close()



def sauv2D(tableau,cheminfichier):
	sauv=open(cheminfichier,"w")
	i,j,k=0,0,0
	while i<taillemonde:
		while j<taillemonde:
			#for item in monde[i][j]:
			inter=str(tableau[i][j]) + "\n"
			sauv.write(inter)
			j=j+1
			k=0
		j=0
		i=i+1
	sauv.close()

def charge2D(tableau,cheminfichier):
	sauv=open(cheminfichier,"r")
	i,j,k=0,0,0
	while i<taillemonde:
		while j<taillemonde:
			inter = int(sauv.readline().rstrip('\n\r'))
			tableau[i][j] = inter
			j=j+1
			k=0
		j=0
		i=i+1
	sauv.close()


