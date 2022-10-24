from player import Player

class Human(Player):
    def __init__(self, name) -> None:
        super().__init__(name)
        self.name = name
    
#This is a inherited class from the parent player class