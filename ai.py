from player import Player

class AI(Player):
    def __init__(self, name) -> None:
        super().__init__(name)
        self.name = name
