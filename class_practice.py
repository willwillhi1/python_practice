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
    
    def fight(self, opponent):
        if self.Atk > opponent.Atk:
            print("win!")
        elif self.Atk < opponent.Atk:
            print("lose!")
        else:
            print("draw!")
            
            
#Inheritance
class Pokemon1(Pokemon):
    #pass //same as Pokemon
    #override
    def __init__(self, Atk, Hp, Def):
        self.Atk = Atk
        self.Hp = Hp
        self.Def = Def
    def fight(self, opponent):
        super().fight(self, opponent)
        print('!!')
    
        
Pikachu = Pokemon(55, 36)
Pikachu.addMove("Nuzzle")
Pikachu.showMove()
Eevee = Pokemon(55, 55)
Pikachu.fight(Eevee)
# >>> draw



