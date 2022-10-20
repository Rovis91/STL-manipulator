# -*- coding: utf-8 -*-

import numpy as np
from MEC1315_STL import *
from  Fonction_transformation import *
"""
Programme de création des lettres et leur positionnement 
"""
def lettres():
    f_y,v_y,n_y = LireSTL("Cylindre.stl")
    f_c,v_c,n_c = LireSTL("Cube.stl")
    
    
    
    #Lettre A
    f1,v1,n1=f_c,v_c,n_c
    f2,v2,n2=f_c,v_c,n_c
    f3,v3,n3=f_c,v_c,n_c
    
    #Modification des dimmensions des barres du A
    v1=2*v1
    v2=2*v2
    v3=1.1*v3
    affinite(f1,v1,n1,0.5,1,5)
    affinite(f2,v2,n2,0.5,1,5)
    affinite(f3,v3,n3,0.5,1,4)
    
    #Translation des differentes barres du A
    f1,v1,n1=translation(f1,v1,n1,-50,50,20)
    f2,v2,n2=translation(f2,v2,n2,-14,50,46)
    f3,v3,n3=translation(f3,v3,n3,-42,50,-36)
    
    #Rotation des barres du A
    f1,v1,n1 = rotation(f1, v1, n1,1, np.pi/8)
    f2,v2,n2 = rotation(f2,v2,n2,1, -np.pi/8)
    f3,v3,n3 = rotation(f3,v3,n3,1, np.pi/2)
    
    #Création de la lettre
    fa,va,na=fusion((f1,v1,n1),(f2,v2,n2),(f3,v3,n3))
    
    
    
    #Lettre G
    f1,v1,n1=f_c,v_c,n_c
    f2,v2,n2=f_c,v_c,n_c
    f3,v3,n3=f_c,v_c,n_c
    f4,v4,n4=f_c,v_c,n_c
    f5,v5,n5=f_c,v_c,n_c
    
    #Modification des dimmensions des barres du G
    v1=2*v1
    v2=2*v2
    v3=2*v3
    v4=2*v4
    v5=2*v5
    affinite(f1,v1,n1,0.5,1,5)
    affinite(f2,v2,n2,0.5,1,3)
    affinite(f3,v3,n3,0.5,1,3)
    affinite(f4,v4,n4,0.5,1,2)
    affinite(f5,v5,n5,0.5,1,1)
    
    #Translation des barres du G
    translation(f1,v1,n1,-4,50,37)
    translation(f2,v2,n2,-47,50,-3)
    translation(f3,v3,n3,-38,50,-3)
    translation(f4,v4,n4,2,50,37)
    translation(f5,v5,n5,-42,50,1)
    
    # Rotation des barres du G
    f2,v2,n2 = rotation(f2,v2,n2,1, np.pi/2)
    f3,v3,n3 = rotation(f3,v3,n3,1, np.pi/2)
    f5,v5,n5 = rotation(f5,v5,n5,1, np.pi/2)
    
    #Création de la lettre
    fg,vg,ng=fusion((f1,v1,n1),(f2,v2,n2),(f3,v3,n3),(f4,v4,n4),(f5,v5,n5))
    
    
    
    #Lettre M
    f1,v1,n1=f_c,v_c,n_c
    f2,v2,n2=f_c,v_c,n_c
    f3,v3,n3=f_c,v_c,n_c
    f4,v4,n4=f_c,v_c,n_c
    
    #Modification des dimmensions des barres du M
    v1=2*v1
    v2=1.5*v2
    v3=1.5*v3
    v4=2*v4
    affinite(f1,v1,n1,0.5,1,5)
    affinite(f2,v2,n2,0.5,1,5)
    affinite(f3,v3,n3,0.5,1,5)
    affinite(f4,v4,n4,0.5,1,5)
    
    #Translation des barres du M
    translation(f1,v1,n1,-25,50,37)
    translation(f2,v2,n2,-5,50,45)
    translation(f3,v3,n3,-35.5,50,28.5)
    translation(f4,v4,n4,-19,50,37)
    
    # Rotation des barres du M
    f2,v2,n2 = rotation(f2,v2,n2,1, -np.pi/8)
    f3,v3,n3 = rotation(f3,v3,n3,1, np.pi/8)
    
    #Création de la lettre
    fm,vm,nm=fusion((f1,v1,n1),(f2,v2,n2),(f3,v3,n3),(f4,v4,n4))
    
    
    
    #Lettre S
    f1,v1,n1=f_c,v_c,n_c
    f2,v2,n2=f_c,v_c,n_c
    f3,v3,n3=f_c,v_c,n_c
    f4,v4,n4=f_c,v_c,n_c
    f5,v5,n5=f_c,v_c,n_c
    
    #Modification des dimmensions des barres du S
    v1=2*v1
    v2=2*v2
    v3=2*v3
    v4=2*v4
    v5=2*v5
    affinite(f1,v1,n1,0.5,1,2)
    affinite(f2,v2,n2,0.5,1,2.25)
    affinite(f3,v3,n3,0.5,1,2)
    affinite(f4,v4,n4,0.5,1,2)
    affinite(f5,v5,n5,0.5,1,2)
    
    #Translation du de la premiere lettre
    translation(f1,v1,n1,-47,50,13)
    translation(f2,v2,n2,13,50,42)
    translation(f3,v3,n3,-42,50,13)
    translation(f4,v4,n4,16,50,37)
    translation(f5,v5,n5,-38,50,13)
    
    # Rotation des barres du S
    f1,v1,n1 = rotation(f1,v1,n1,1, np.pi/2)
    f3,v3,n3 = rotation(f3,v3,n3,1, np.pi/2)
    f5,v5,n5 = rotation(f5,v5,n5,1, np.pi/2)
    
    #Création de la lettre
    fs,vs,ns=fusion((f1,v1,n1),(f2,v2,n2),(f3,v3,n3),(f4,v4,n4),(f5,v5,n5))
    
    
    
    #Lettre U
    f1,v1,n1=f_c,v_c,n_c
    f2,v2,n2=f_c,v_c,n_c
    f3,v3,n3=f_c,v_c,n_c
    f4,v4,n4=f_c,v_c,n_c
    f5,v5,n5=f_c,v_c,n_c
    
    #Modification des dimmensions des barres du U
    v1=2*v1
    v2=2*v2
    v3=2*v3
    affinite(f1,v1,n1,0.5,1,5)
    affinite(f2,v2,n2,0.5,1,2.5)
    affinite(f3,v3,n3,0.5,1,5)
    
    #Translation des barres de la lettre U
    translation(f1,v1,n1,5,50,37)
    translation(f2,v2,n2,-38,50,5)
    translation(f3,v3,n3,10,50,37)
    
    # Rotation des barres du U
    f2,v2,n2 = rotation(f2,v2,n2,1, np.pi/2)
    
    #Création de la lettre
    fu,vu,nu=fusion((f1,v1,n1),(f2,v2,n2),(f3,v3,n3))
    
    
    
    #Lettre O
    f1,v1,n1=f_y,v_y,n_y
    
    #Modification des dimmensions de la lettre O
    v1=9*v1
    affinite(f1,v1,n1,1,1,0.2)
    
    #Rotation du O
    f1,v1,n1 = rotation(f1,v1,n1,0, np.pi/2)

    #Translation du de la lettre O
    translation(f1,v1,n1,-11,52,42)
    
    #Création de la lettre
    fo,vo,no=f1,v1,n1
    
    #Formation du mot
    f,v,n=fusion((fa,va,na),(fg,vg,ng),(fm,vm,nm),(fs,vs,ns),(fu,vu,nu),(fo,vo,no))

    return f,v,n

