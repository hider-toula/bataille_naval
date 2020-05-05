import grille as gl

class Bataille :
    def __init__(self):
        GrilleB = gl.grille()
        GrilleA = GrilleB.genere_grille()
        Grille = gl.grille(GrilleA)
        self.Grille = Grille
        
    # fonction qui verifie si la grille est vide --------------------------------------------------
    def win(self,grille=None):
        if(grille is None):
            grille=self.Grille 
        for i in range(10):
            for j in range(10):
                if ((not grille.is_vide([i,j])) ) :
                    if((not grille.shooted([i,j]) )):
                        return False
        return True 
    
    # fonction qui permet de tirer sure une case de la grille ------------------------------------
    def shoot(self,x,y,nb_shoots=None,grill=None):
        if( grill is None ):
            return self.Grille.shoot(x,y,nb_shoots)
        return gl.grille(grill).shoot(x,y,nb_shoots)
    def elemenate(self,x,y,grill=None):
        if( grill is None ):
                self.Grille.elemenate(x,y)
        gl.grille(grill).elemenate(x,y)
        
    def proba_box(self,grille=None,matrice=None):
        if( grille is None ):
            grille = self.Grille
        return grille.proba_box(matrice)
    
    def shooted (self,direction,tab=None,grille=None):
        if(grille is None):
            grille=self.Grille
        return grille.shooted(direction,tab)
    
    def probaJointe(self,grille,model):
        return self.Grille.probaJointe(grille,model)
    
    def containShip(self,model):
        return self.Grille.containShip(model)