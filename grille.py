import random
import bateau as bt
import numpy as np
class grille ():
    
    # initialisation de la matrice a zero---------------------------------------------------------- 
    def __init__(self,grille=None):
        if(grille is None) :
            matrice = []
            for i in range(10):
                matrice.append([0] * 10)
            self.matrice = matrice
        else :
            self.matrice = grille
            
            
    # fonction pour afficher la grille-----------------------------------------------------------------
    def affiche(self,grille=None) :
        if(grille is None):
            grille=self.matrice
        for i in range(len(self.matrice)):
            for j in range(len(self.matrice)):
                print(grille[i][j]," ",end='')
            print("\n")
        #plt.figure(figsize=(5,5))
        #plt.imshow(grille)
        
        
    #fonction pour verifier qu'on depasse pas les bornnes-----------------------------------------------    
    def bounds(self,position,direction,nbr,grille=None):
        if(grille is None):
            grille=self.matrice
        return position[direction]+nbr-1 <len(grille)
    
    
    #fonction pour verifier si une case est vide--------------------------------------------------------- 
    def is_vide(self,position,grille=None):
        if(grille is None):
            grille=self.matrice
        return grille[position[0]][position[1]]==0
    
    def shooted(self,position,grille=None):
        if(grille is None):
            grille=self.matrice
        return grille[position[0]][position[1]]==-1
    
    # fonction pour verifier si on l'mplacement est vide-------------------------------------------------- 
    def emplacement_vide(self,position,nbr,direction,grille=None):
        if(grille is None):
            grille=self.matrice
        if direction==1:
            for i in range (nbr):
                if not(self.is_vide([position[0],position[1]+i],grille)):
                    return False
            return True
        else:
            for i in range (nbr):
                if not(self.is_vide([position[0]+i,position[1]],grille)):
                    return False
            return True
        
        
    # fonction pour verifier si on peut placer------------------------------------------------------------- 
    def peut_placer(self,bateau,position,direction,grille=None):
        if(grille is None):
            grille=self.matrice
        if self.bounds(position,direction,bateau.getSize(),grille) : 
            if self.emplacement_vide(position,bateau.getSize(),direction,grille):
                return True
        return False
    
    
    # une fonction qui permet de copier une matrice--------------------------------------------------------
    def copie_grille(self,grille):
        return np.array(grille)
    
    
    # fonction pour placer un bateau dans la grille---------------------------------------------------------
    def place(self,bateau,position,direction,grille=None):
        if(grille is None):
            grille=self.matrice
        
        if direction==1:
            if self.peut_placer(bateau,position,direction,grille):
                for i in range(bateau.getSize()):
                    grille[position[0]][position[1]+i]=bateau.getId()
        else:
            if self.peut_placer(bateau,position,direction,grille):
                for i in range(bateau.getSize()):
                    grille[position[0]+i][position[1]]=bateau.getId()            
        return  grille
    
    
    #fonction qui verifier si deux grilles sont egeaux--------------------------------------------------------- 
    def eq(self, grilleA,grilleB=None):
        if(grilleB is None):
            grilleB=self.matrice
        return np.array_equal(grilleA,grilleB)  
    
    
    # une fonction qui place aleatoirement un bateau dans la grille--------------------------------------------
    def place_alea(self, bateau,grille=None):
        if grille is None :
            grille=self.matrice      
            
        position = []
        for i in range(2):
            position.append(0)
        direction = random.randint(0,1)            
        position[0] = random.randint(0,9)         
        position[1] = random.randint(0,9)
        while(not(self.peut_placer(bateau,position,direction))):
            direction = random.randint(0,1)
            position[0] = random.randint(0,9)         
            position[1] = random.randint(0,9)
        return self.place(bateau,position,direction,grille)
        
    # une fonction qui permet de generer une grille---------------------------------------------------------   
    def genere_grille(self,grille=None):
        if grille is None :
            grille = self.copie_grille( self.matrice)
            
        cpt = 5
        while(cpt > 2):
            self.place_alea(bt.bateau(cpt),grille)
            cpt = cpt -1
        return grille
    
    
    # une fonction qui calcule le nombre de configuration pour un bateau ------------------------------------
    def nb_config_bateau(self,bateau):
        return ((10-bateau.getSize())+1)*10*2
    
    
    # une fonction qui calcule le nombre de config possible pour une liste de bateau--------------------------
    def nb_config(self,liste_bateau,grille):
        nb_config=0
        if(len(liste_bateau)==1):
            for i in range(len(self.matrice)):
                for j in range(len(self.matrice)):
                    if(self.peut_placer(liste_bateau[0],[i,j],0,grille)):
                        nb_config+=1
                    if(self.peut_placer(liste_bateau[0],[i,j],1,grille)):
                        nb_config+=1 
            return nb_config
        for i in range(len(self.matrice)):
            for j in range(len(self.matrice)):
                if(self.peut_placer(liste_bateau[0],[i,j],0,grille)):
                    nb_config =  nb_config + self.nb_config( [i for i in liste_bateau[1:]],self.place(liste_bateau[0],[i,j],0,self.copie_grille( grille)))
                if(self.peut_placer(liste_bateau[0],[i,j],1,grille)):
                    nb_config = nb_config + self.nb_config([i for i in liste_bateau[1:]],self.place(liste_bateau[0],[i,j],1,self.copie_grille( grille)))
        return nb_config
    
    
    # fonction qui calcule le nombre de grilles generée pour arrive a la grille donnée-----------------------------
    def proba_grille(self,grilleA):
        nb_config=0
        while(not self.eq(grilleA,self.genere_grille(self.copie_grille( self.matrice)))):
            nb_config = nb_config+1
        return nb_config
        
    # une fonction qui permet d’approximer le nombre total de grilles pour une liste de bateaux ------------------- 
    def nb_config_approximer(self):
        result = 0
        compteur=0
        while(compteur <100):
            grilleA = self.genere_grille()
            result= result + self.proba_grille(grilleA)
            compteur = compteur+1
        return result/100
    
    def shoot (self,x,y,nb_shoots):
        res = self.matrice[x][y]
        self.matrice[x][y]=-1
        nb_shoots[0] +=1
        return res
    def elemenate(self,x,y):
        res = self.matrice[x][y]
        self.matrice[x][y]=-1

    
    def probaJointe(self,grille,model):
        jointe = []
        for i in range(10):
            jointe.append([0] * 10)
        for i in range(len(self.matrice)):
            for j in range(len(self.matrice)):
                if(self.peut_placer(bt.bateau(model),[i,j],0,grille)):
                    jointe[i][j] +=1
                    for k in range(bt.bateau(model).getSize()):
                        jointe[i+k-1][j] +=1
                if(self.peut_placer(bt.bateau(model),[i,j],1,grille)):
                    jointe[i][j] +=1 
                    for k in range(bt.bateau(model).getSize()):
                        jointe[i][j+k-1] +=1
        return jointe
    
    def containShip(self,model):
        for i in range(len(self.matrice)):
            for j in range(len(self.matrice)):
                if(self.matrice[i][j]==model):
                    return True
        return False
                    