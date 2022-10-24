from player import Player

class AI(Player):
    def __init__(self, name) -> None:
        super().__init__(name)
        self.name = name

#This is another inherited class from the parent class player