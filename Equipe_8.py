# -*- coding: utf-8 -*-

from MEC1315_STL import *
from  Fonction_transformation import *
from Objets import objets
from Lettres import lettres
from Mur import mur

#Création des lettres
f_let,v_let,n_let = lettres()
#Création des objets
f_o,n_o,v_o = objets()
#Création du sol  et des murs 
f_mur,v_mur,n_mur = mur()

#Fusion des éléments
f,v,n=fusion((f_let,v_let,n_let),(f_o,n_o,v_o),(f_mur,v_mur,n_mur))

EcrireSTLASCII('Scene_8.stl',f,v,n)
