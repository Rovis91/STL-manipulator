# -*- coding: utf-8 -*-

import numpy as np
from MEC1315_STL import *
from  Fonction_transformation import *

def objets():
    f_y,v_y,n_y = LireSTL("Cylindre.stl")
    f_c,v_c,n_c = LireSTL("Cube.stl")
    f_a,v_a,n_a = LireSTL("Amogus.stl")
    f_da,v_da,n_da = LireSTL("Dead_Amogus.stl")
    f_t,v_t,n_t = LireSTL("Triangle.stl")
    f_l,v_l,n_l = LireSTL("Lego.stl")
    
    def panneau(f_t,v_t,n_t,f_c,v_c,n_c):
        
        # Création du panneau
        f_p1,v_p1,n_p1= affinite(f_c,v_c,n_c,5,1,10)
        f_p1,v_p1,n_p1 = rotation(f_p1,v_p1,n_p1 ,2, np.pi/2)
        translation(f_p1,v_p1,n_p1,-48,5,5)
        
        # création des boutons en triangle du panneau
        f_t,v_t,n_t = rotation(f_t,v_t,n_t,0,np.pi/2)
        # Les boutons de gauche
        f_p2,v_p2,n_p2= affinite(f_t,v_t,n_t,1,1,0.5)
        f_p2,v_p2,n_p2=rotation(f_p2,v_p2,n_p2 ,1, np.pi/2)
        f_p2,v_p2,n_p2=translation(f_p2,v_p2,n_p2,-47.75,6,14)
        
        f_p3,v_p3,n_p3= affinite(f_t,v_t,n_t,1,1,0.5)
        f_p3,v_p3,n_p3=rotation(f_p3,v_p3,n_p3 ,1, np.pi/2)
        f_p3,v_p3,n_p3=translation(f_p3,v_p3,n_p3,-47.75,6,11)
        
        f_p4,v_p4,n_p4= affinite(f_t,v_t,n_t,1,1,1)
        f_p4,v_p4,n_p4=rotation(f_p4,v_p4,n_p4 ,1, np.pi/2)
        f_p4,v_p4,n_p4=translation(f_p4,v_p4,n_p4,-47.75,6,8)
        
        # Les boutons de droite
        f_p5,v_p5,n_p5= affinite(f_t,v_t,n_t,1,1,2)
        f_p5,v_p5,n_p5=rotation(f_p5,v_p5,n_p5 ,1, np.pi/2)
        f_p5,v_p5,n_p5=translation(f_p5,v_p5,n_p5,-47.75,8,14)
        
        f_p6,v_p6,n_p6= affinite(f_t,v_t,n_t,1,1,0.75)
        f_p6,v_p6,n_p6=rotation(f_p6,v_p6,n_p6 ,1, np.pi/2)
        f_p6,v_p6,n_p6=translation(f_p6,v_p6,n_p6,-47.75,8,11)
        
        f_p7,v_p7,n_p7= affinite(f_t,v_t,n_t,1,1,0.5)
        f_p7,v_p7,n_p7=rotation(f_p7,v_p7,n_p7 ,1, np.pi/2)
        f_p7,v_p7,n_p7=translation(f_p7,v_p7,n_p7,-47.75,8,8)
        
        #Fusion des boutons
        f_p,v_p,n_p=fusion((f_p1,v_p1,n_p1),(f_p2,v_p2,n_p2),(f_p3,v_p3,n_p3),(f_p4,v_p4,n_p4),(f_p5,v_p5,n_p5),(f_p6,v_p6,n_p6),(f_p7,v_p7,n_p7))
        
        f_p,v_p,n_p=repetition_rectiligne(f_p,v_p,n_p, -48,15,10, False, -10,False, 1,4,1)
        return f_p,v_p,n_p
    
    
    def table(f_y,v_y,n_y):
    
        #Création des tabourets 
        f_t,v_t,n_t = affinite(f_y,v_y,n_y, 10*0.25,10*0.25, 20*0.07)
        f_t,v_t,n_t = repetition_circulaire(f_t,v_t,n_t, 0, 0, 0, 20*0.7, 6, axe=0, borne_min=0, borne_max=2*np.pi)
        f_t,v_t,n_t = translation(f_t,v_t,n_t,0,0,-1.5)
        #Création de la table
        f_tb,v_tb,n_tb = affinite(f_y,v_y,n_y, 9, 9, 3)

        
        
        f_tt,v_tt,n_tt=fusion((f_tb,v_tb,n_tb),(f_t,v_t,n_t))    
        
        f_tt,v_tt,n_tt = repetition_circulaire(f_tt,v_tt,n_tt, 0, 0, 0, 25, 3, axe=0, borne_min=0, borne_max=2*np.pi)
        f_tt,v_tt,n_tt = translation(f_tt,v_tt,n_tt,0,0,1)
        return  f_tt,v_tt,n_tt
    
    def amogus(f_a,v_a,n_a):
        
        homothetie(f_a,v_a,n_a, 1.1)
        
        #Position des amogus
        f_a1,v_a1,n_a1 = f_a,v_a,n_a 
        f_a1,v_a1,n_a1 = rotation(f_a1,v_a1,n_a1 ,2, np.pi/2)
        f_a1,v_a1,n_a1 = translation(f_a1,v_a1,n_a1,-3.0, -2.0, -0.5)
        
        f_a2,v_a2,n_a2 =f_a,v_a,n_a 
        f_a2,v_a2,n_a2 = rotation(f_a2,v_a2,n_a2 ,2, 2*np.pi/3)
        f_a2,v_a2,n_a2 = translation(f_a2,v_a2,n_a2,-1.5, -2.2, -0.5)
        
        f_a3,v_a3,n_a3 = f_a,v_a,n_a
        f_a3,v_a3,n_a3 = rotation(f_a3,v_a3,n_a3 ,2, -4*np.pi/6)
        f_a3,v_a3,n_a3 = translation(f_a3,v_a3,n_a3,1.0, -2.0, -0.5)
        
        f_a4,v_a4,n_a4 = f_a,v_a,n_a
        f_a4,v_a4,n_a4 = rotation(f_a4,v_a4,n_a4 ,2, np.pi/4)
        f_a4,v_a4,n_a4 = translation(f_a4,v_a4,n_a4,-4.2, 1, -0.5)
        
        
        f_a5,v_a5,n_a5 = f_a,v_a,n_a
        f_a5,v_a5,n_a5 = rotation(f_a5,v_a5,n_a5 ,2, -np.pi/6)
        f_a5,v_a5,n_a5 = translation(f_a5,v_a5,n_a5,0.5, 3.0, -0.5)
        
        f_a6,v_a6,n_a6 = f_a,v_a,n_a
        f_a6,v_a6,n_a6 = rotation(f_a6,v_a6,n_a6 ,2, np.pi/3)
        f_a6,v_a6,n_a6 = translation(f_a6,v_a6,n_a6,3.0, -1.3, -0.5 )
        
        #Fusion des personnages
        f_am,v_am,n_am = fusion((f_a1,v_a1,n_a1),(f_a2,v_a2,n_a2),(f_a3,v_a3,n_a3),(f_a4,v_a4,n_a4),(f_a5,v_a5,n_a5),(f_a6,v_a6,n_a6 ))
        
        return f_am,v_am,n_am
    
    def amogus_mort(f_da,v_da,n_da):
        
        v_da=6*v_da
        f_da,v_da,n_da=rotation(f_da,v_da,n_da,1)
        f_da,v_da,n_da=translation(f_da,v_da,n_da,-5, -5, 3)
        
        return f_da,v_da,n_da
    
    def aeration(f_c,v_c,n_c,f_l,v_l,n_l):
        
        f1,v1,n1 = affinite(f_c,v_c,n_c,42,0.1,25)
        f1,v1,n1 = centrage(f1,v1,n1)
        
        # Modification des dimensions de la grille d'aération
        v1=v1/15
        affinite(f1,v1,n1,0.25,0.25,0.1)
        
        # translation et répétition de la grille d'aération
        translation(f1, v1, n1, 5, -5, 1)
        f1,v1,n1=repetition_rectiligne(f1, v1, n1, 35,-20 ,0.5, False, 0.8,False, 1,5,1)
        
        f2,v2,n2=f_l,v_l,n_l
        f3,v3,n3=f_l,v_l,n_l
        f4,v4,n4=f_l,v_l,n_l
        f5,v5,n5=f_l,v_l,n_l
        # Modification des dimensions des contours de l'aération
        v2=v2/5
        v3=v3/5
        v4=v4/5
        v5=v5/5
        affinite(f2, v2, n2, 1,0.3, 1)
        affinite(f3, v3, n3, 1,0.3, 1)
        affinite(f4, v4, n4, 1.1,0.3, 1)
        affinite(f5, v5, n5, 1.1,0.3, 1)
        
        # Rotation du premier contour
        f2,v2,n2= rotation(f2,v2,n2 ,0, np.pi)
        f2,v2,n2= rotation(f2,v2,n2 ,2, np.pi/2)
    
        # Rotation du deuxième contour
        f3,v3,n3 = rotation(f3,v3,n3 ,0, np.pi)
        f3,v3,n3 = rotation(f3,v3,n3 ,2, np.pi/2)
        
        # Rotation du troisieme contour
        f4,v4,n4 = rotation(f4,v4,n4 ,0, np.pi)
        
        # Rotation du quatrième contour
        f5,v5,n5= rotation(f5,v5,n5 ,0, np.pi)
        
        # Translation des contours de l'aération
        translation(f2, v2, n2, 32.8, -20.55, 1)
        translation(f3,v3,n3,36.5,-20.55,1)
        translation(f4,v4,n4,32.75,-16,1)
        translation(f5,v5,n5,32.75,-20,1)
        
        #Création de la grille
        f_ar,v_ar,n_ar=fusion((f1,v1,n1),(f2,v2,n2),(f3,v3,n3),(f4,v4,n4),(f5,v5,n5))
        
        #Plcement de la grille
        translation(f_ar,v_ar,n_ar,-25,-25,0)
        return f_ar,v_ar,n_ar
            
    
    f_p,v_p,n_p = panneau(f_t,v_t,n_t,f_c,v_c,n_c)
    f_tt,v_tt,n_tt = table(f_y,v_y,n_y)
    f_am,v_am,n_am = amogus(f_a,v_a,n_a) 
    f_da,v_da,n_da = amogus_mort(f_da,v_da,n_da)
    f_ar,v_ar,n_ar = aeration(f_c,v_c,n_c,f_l,v_l,n_l)
    
    #Fusion des objets
    f,n,v=fusion((f_tt,v_tt,n_tt),(f_am,v_am,n_am),(f_da,v_da,n_da),(f_p,v_p,n_p),(f_ar,v_ar,n_ar))
    
    return f,n,v

    
 