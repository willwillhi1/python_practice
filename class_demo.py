class Pokemon:
    movelist = [];
    #Constructor
    def __init__(self, Atk, Hp):
        self.Atk = Atk
        self.Hp = Hp
    #Method
    def addMove(self, move):
        self.movelist.append(move)
    
    def showMove(self):
        print(self.movelist)
        
Pikachu = Pokemon(55, 36)
Pikachu.addMove("Nuzzle")
Pikachu.showMove()
