# -*- coding: utf-8 -*-

import numpy as np
from MEC1315_STL import *
from  Fonction_transformation import *


def mur():
    f_y,v_y,n_y = LireSTL("Cylindre.stl")
    f_c,v_c,n_c = LireSTL("Cube.stl")
    
    
    #Création du sol
    f_s,v_s,n_s = affinite(f_y,v_y,n_y,100,100,0.5)
    f_s,v_s,n_s = centrage(f_s,v_s,n_s)
    
    #Création des murs
    f_m,v_m,n_m = affinite(f_c,v_c,n_c,42,0.1,25)
    f_m,v_m,n_m = centrage(f_m,v_m,n_m)
    f_m,v_m,n_m = translation(f_m,v_m,n_m,0,0,12)
    
    
    lg=35.1
    lg2=50
    #Arrire gauche
    f_mag,v_mag,n_mag = rotation(f_m,v_m,n_m, 2, np.pi/4)
    f_mag,v_mag,n_mag = translation(f_mag,v_mag,n_mag,-lg,lg,0)
    #Arrire droite
    f_mad,v_mad,n_mad = rotation(f_m,v_m,n_m, 2, -np.pi/4)
    f_mad,v_mad,n_mad = translation(f_mad,v_mad,n_mad,lg,lg,0)
    #Gauche
    f_mg,v_mg,n_mg = translation(f_m,v_m,n_m,0,lg2,0)
    #Droite
    f_md,v_md,n_md = rotation(f_m,v_m,n_m, 2, np.pi/2)
    
    #Fusion des murs et de la base
    f,n,v=fusion((f_s,v_s,n_s),(f_mag,v_mag,n_mag),(f_mad,v_mad,n_mad),(f_mg,v_mg,n_mg),(f_md,v_md,n_md))
    return f,n,v