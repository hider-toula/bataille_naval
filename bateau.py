class bateau ():
    def __init__(self,id):
        self.id =id 
    
    # fonction qui renvoit la taille du bateau --------------------------------------------------
    def getSize(self):
        if self.id == 1 :
            return 5
        elif self.id == 2:
            return 4
        elif self.id == 3:
            return 3
        elif self.id == 4:
            return 3
        elif self.id == 5:
            return 2
        else:
            return 0
        
    # fonction qui renvoit l'id du bateau ------------------------------------------------------- 
    def getId(self):
        return self.id