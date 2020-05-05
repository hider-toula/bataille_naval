import bataille as bt
import random
class JoueurRandom :
    def __init__(self):
        bataille = bt.Bataille()
        self.bataille = bataille
    def play(self,bataille=None):
        if(bataille is None):
            bataille = self.bataille
        nb_shoots = []
        nb_shoots.append(0)
        while (not bataille.win()):
            x = random.randint(0,9)
            y = random.randint(0,9)
            if (not bataille.shooted([x,y])):
                bataille.shoot(x,y,nb_shoots)
        return nb_shoots[0]

"""_____________________________________________________________"""

class JoueurHeuristique :
    def __init__(self):
        bataille = bt.Bataille()
        self.bataille = bataille
    
    # fonction pour jouer ---------------------------------
    def play(self,bataille=None):
        if(bataille is None):
            bataille = self.bataille
        nb_shoots = []
        nb_shoots.append(0)
        while (not bataille.win()) :
            x = random.randint(0,9)
            y = random.randint(0,9)
            if (not bataille.shooted([x,y])) :
                if ( bataille.shoot(x,y,nb_shoots) > 0) :
                    self.relatedBoxes(x,y,nb_shoots)
        
        return nb_shoots[0]
    
    # fonction pour examiner les voisin ----------------------------
    def relatedBoxes(self,x,y,nb_shoots,bataille=None):
        if(bataille is None):
            bataille = self.bataille
        if (y+1 <10 and (not bataille.win()) and (not bataille.shooted([x,y+1])) and bataille.shoot(x,y+1,nb_shoots) >0 ):
            y +=1
            while( y+1 <10 and (not bataille.win())  and (not bataille.shooted([x,y+1]))  and bataille.shoot(x,y+1,nb_shoots)> 0):
                y +=1
        elif (y-1 > 0 and (not bataille.win()) and (not bataille.shooted([x,y-1]))   and bataille.shoot(x,y-1,nb_shoots) >0 ):
            y -=1
            while( y-1 >0 and (not bataille.win()) and (not bataille.shooted([x,y-1]))  and bataille.shoot(x,y-1,nb_shoots)> 0):
                y -=1
        elif (x-1 > 0 and (not bataille.win()) and (not bataille.shooted([x-1,y]))   and bataille.shoot(x-1,y,nb_shoots) >0 ):
            x -=1
            while( x-1 >0 and (not bataille.win()) and (not bataille.shooted([x-1,y]))  and bataille.shoot(x-1,y,nb_shoots)> 0):
                x -=1
        elif (x+1 <10 and (not bataille.win()) and (not bataille.shooted([x+1,y]))   and bataille.shoot(x+1,y,nb_shoots) >0 ):
            x +=1
            while( x+1 <10 and (not bataille.win()) and (not bataille.shooted([x+1,y]))  and bataille.shoot(x+1,y,nb_shoots)> 0):
                x +=1

"""______________________________________________________________"""
class JoueurprobaSimple :
    def __init__(self):
        bataille = bt.Bataille()
        self.bataille = bataille
        matrice = []
        for i in range(10):
            matrice.append([0] * 10)
        self.matrice = matrice

    # fonction pour jouer ---------------------------------
    def play(self,bataille=None):
        if(bataille is None):
            bataille = self.bataille
        
        model =5
        nb_shoots = []
        nb_shoots.append(0)
        x = random.randint(0,9)
        y = random.randint(0,9)
        while (not bataille.win()) :
            if (not bataille.shooted([x,y])) :
                self.matrice[x][y]=-1
                if ( bataille.shoot(x,y,nb_shoots) > 0) :
                    self.relatedBoxes(x,y,nb_shoots)
                    #print("c'est pas logique du tout ")
            if bataille.containShip(model):
                jointe = bataille.probaJointe(self.matrice,model)
            else :
                if model ==5:
                    model=3
                else :
                    model -=1
                jointe = bataille.probaJointe(self.matrice,model)
            #print(jointe)
            for i in range(10):
                for j in range(10):
                    if jointe[i][j] == 0:
                        self.matrice[i][j]=-1
                        bataille.elemenate(i,j)
                    x = random.randint(0,9)
                    y = random.randint(0,9)
        return nb_shoots[0]
    
    # fonction pour examiner les voisin ----------------------------
    def relatedBoxes(self,x,y,nb_shoots,bataille=None):
        if(bataille is None):
            bataille = self.bataille
        if (y+1 <10 and (not bataille.win()) and (not bataille.shooted([x,y+1])) and bataille.shoot(x,y+1,nb_shoots) >0 ):
            y +=1
            self.matrice[x][y]=-1
            while( y+1 <10 and (not bataille.win())  and (not bataille.shooted([x,y+1]))  and bataille.shoot(x,y+1,nb_shoots)> 0):
                y +=1
                self.matrice[x][y]=-1
        elif (y-1 > 0 and (not bataille.win()) and (not bataille.shooted([x,y-1]))   and bataille.shoot(x,y-1,nb_shoots) >0 ):
            y -=1
            self.matrice[x][y]=-1
            while( y-1 >0 and (not bataille.win()) and (not bataille.shooted([x,y-1]))  and bataille.shoot(x,y-1,nb_shoots)> 0):
                y -=1
                self.matrice[x][y]=-1
        elif (x-1 > 0 and (not bataille.win()) and (not bataille.shooted([x-1,y]))   and bataille.shoot(x-1,y,nb_shoots) >0 ):
            x -=1
            self.matrice[x][y]=-1
            while( x-1 >0 and (not bataille.win()) and (not bataille.shooted([x-1,y]))  and bataille.shoot(x-1,y,nb_shoots)> 0):
                self.matrice[x][y]=-1
        elif (x+1 <10 and (not bataille.win()) and (not bataille.shooted([x+1,y]))   and bataille.shoot(x+1,y,nb_shoots) >0 ):
            x +=1
            self.matrice[x][y]=-1
            while( x+1 <10 and (not bataille.win()) and (not bataille.shooted([x+1,y]))  and bataille.shoot(x+1,y,nb_shoots)> 0):
                x +=1
                self.matrice[x][y]=-1