from .map_generator import Generator
from .player import Player


class Game:
    def __init__(self, width=64, height=32):
        self._generator = Generator(width=width, height=height)
        self._generator.gen_level()
        self._generator.gen_tiles_level()
        self._map = self._generator.tiles_level
        
        
        self._player = [Player(symbol="P")]

        self._player[0].initPos( self._map )
        self.nb_player = 1

    def getMap(self):
        return self._map

    def move(self, dx, dy, nb_player):
        if len(self._player) > nb_player :
            return self._player[nb_player].move(dx, dy, self._map, self._player)
        else : 
            return [], False

    #adding a player when the button is clicked
    def add_player(self):
        ret = False
        if self.nb_player == 1 :
            ret = True
            self.nb_player+=1
            self._player.append(Player(symbol = "Q"))
            self._player[1].initPos(self._map)
            return [{"i": f"{self._player[1]._y}", "j":f"{self._player[1]._x}", "content":self._player[1]._symbol}],ret, [e.vie for e in self._player]
        return [], ret, [e.vie for e in self._player]