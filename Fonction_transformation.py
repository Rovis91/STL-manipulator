# -*- coding: utf-8 -*-

import numpy as np
from MEC1315_STL import *

#-----------------------------------------------------------------------------
def translation(f,v,n, deplacement_x, deplacement_y, deplacement_z):

    v[:,0]=v[:,0]+deplacement_x
    v[:,1]=v[:,1]+deplacement_y
    v[:,2]=v[:,2]+deplacement_z
    return f, v, n

#-----------------------------------------------------------------------------
def rotation(f, v, n, axe=2, angle=np.pi/2):
    """

    Parameters
    ----------
    f,n,v : objet d'entré  
    axe : axe de rotation
        x=0,y=1,z=2,z par défault
    angle : angle de rotation
        90° par défault

    Returns
    -------
    f,n,v : objet de sortie
    """
    
    if axe==0:
        R=Rx(angle)
    elif axe==1:
        R=Ry(angle)
    elif axe==2:
        R=Rz(angle)
    else:
        print("Erreur d'axe")
    
    v=np.dot(v,R)
    n=np.dot(n,R)
    return f,v,n

#-----------------------------------------------------------------------------
def homothetie(f,v,n,x):
    
    v=x*v
    
    return f, v, n

#-----------------------------------------------------------------------------
def affinite(f, v, n, x, y, z):

    if x!=0:
        v[ :,0]=v[ :,0]*x  
    if y!=0:
        v[ :,1]=v[ :,1]*y    
    if z!=0:
        v[ :,2]=v[ :,2]*z
    
    n=CalculNormal( f, v )

    return f, v, n

#-----------------------------------------------------------------------------
def centrage(f,v,n):
    
    nv=len(v)
    v[:,0]=v[:,0]-np.ones(nv)*np.mean(v[:,0])
    v[:,1]=v[:,1]-np.ones(nv)*np.mean(v[:,1])
    v[:,2]=v[:,2]-np.ones(nv)*np.mean(v[:,2])
    
    return f,v,n

#-----------------------------------------------------------------------------
def fusion(*tpl):
    """

    Parameters
    ----------
    *tpl : tuple sous la forme (f1,v1,n1),(f2,v2,n2), ...

    Returns
    -------
    f,n,v : objet de sortie
    
    """
    
    f, v, n = tpl[0][0],tpl[0][1],tpl[0][2]
    
    for i in range(1,len(tpl)):
        f1, v1, n1 = f, v, n
        nv1 = len(v1)
        f2, v2, n2 = tpl[i][0],tpl[i][1],tpl[i][2]
        f = np.vstack((f1, f2+nv1))
        v = np.vstack((v1, v2))
        n = np.vstack((n1, n2))
        
    return f, v, n

#-----------------------------------------------------------------------------

def repetition_circulaire(f,v,n,x,y,z, rayon, repetition, axe=0, borne_min=0, borne_max=2*np.pi):
    """
    
    Parameters
    ----------
    f,v,n : objet d'entré  
    x,y,z : position du centre du cercle 
    rayon : rayon du cercle 
    repetition : nombre d'objets
    axe : axe perpendiculaire du cercle 
        0=z
        1=y
        2=x
    borne_min : borne minimal 
    borne_max : borne maximal 
    
    Returns
    -------
    f,v,n : objet de sortie

    """
    
    f,v,n=centrage(f,v,n) # On centre l'objet
    f,v,n=translation(f,v,n,x,y,z) # Positionnement en coordonnes absolue 
    v1,n1=np.array(v),n # On enregistre les valeurs de l'objet initial 
    
    angle=(borne_max-borne_min)/repetition
    nv=len(v1)

    
    for i in range(repetition+1):
        #On copie l'objet
        f2=f+nv
        n2=n
        v2=np.array(v1)
        
        
        #On deplace l'ojet
        if axe == 0:
            v2[:,0]=v2[:,0]+(rayon*np.cos(i*angle))
            v2[:,1]=v2[:,1]+(rayon*np.sin(i*angle)) 
            
            
        elif axe == 1:
            v2[:,1]=v2[:,1]+(rayon*np.cos(i*angle))
            v2[:,2]=v2[:,2]+(rayon*np.sin(i*angle))
        elif axe == 2:
            v2[:,2]=v2[:,2]+(rayon*np.cos(i*angle))
            v2[:,0]=v2[:,0]+(rayon*np.sin(i*angle))
        else:
            print('valeur "axe" non valide')

        if i==0: # Permet de ne pas laisser un bloc au milieu 
            f,v,n=f,np.array(v2),n2
        else:  
            f,v,n=np.vstack((f,f2)),np.vstack((v,v2)),np.vstack((n,n2))
    
    return f,v,n

def repetition_rectiligne(f,v,n,x,y,z, distance_x, distance_y=False, distance_z=False, rep_x=1, rep_y=1, rep_z=1):
    """
    
    Parameters
    ----------
    f,v,n : objet d'entré  
    x,y,z : position d
    distance_x : distance en x entre les objets
    distance_y : distance en y entre les objets
    distance_z : distance en z entre les objets
    rep_x : nombre d'élement en x
    rep_y : nombre d'éléments en y
    rep_z : nombre d'éléments en z

    Returns
    -------
    f,v,n : objet de sortie

    """
    f,v,n=centrage(f,v,n) # On centre l'objet
    f,v,n=translation(f,v,n,x,y,z) # Positionnement en coordonnes absolue 
    v1,n1=np.array(v),n # On enregistre les valeurs de l'objet initial 
    
    # On met distance x par defaut partout si rien n'est rentré
    if distance_y==False:
        distance_y=distance_x
    if distance_z==False:
        distance_z=distance_x
        
    
    nv=len(v1)
    # Clonage en x
    for i in range(1,rep_x):
        f2=f+nv
        n2=n
        v2=np.array(v1)
        v2[:,0]=v2[:,0]+distance_x*i
        f,v,n=np.vstack((f,f2)),np.vstack((v,v2)),np.vstack((n,n2))

    v1=np.array(v)
    nv=len(v1)
    # Clonage en y
    for i in range(1,rep_y):
        f2=f+nv
        n2=n
        v2=np.array(v1)
        v2[:,1]=v2[:,1]+distance_y*i
        f,v,n=np.vstack((f,f2)),np.vstack((v,v2)),np.vstack((n,n2))
        
    v1=np.array(v)
    nv=len(v1)
    # Clonage en z
    for i in range(1,rep_z):
        f2=f+nv
        n2=n
        v2=np.array(v)
        v2[:,2]=v2[:,2]+distance_z*i
        f,v,n=np.vstack((f,f2)),np.vstack((v,v2)),np.vstack((n,n2))
    
    return f,v,n