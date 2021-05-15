from .map_generator import Generator
from .player import Player


class Game:
    def __init__(self, width=64, height=32):
        self._generator = Generator(width=width, height=height)
        self._generator.gen_level()
        self._generator.gen_tiles_level()
        self._map = self._generator.tiles_level
        
        
        self._player = Player(symbol="P")
        self._player.initPos( self._map )
        self.nb_player = 1

    def getMap(self):
        return self._map

    def move(self, dx, dy):
        return self._player.move(dx, dy, self._map)

    def add_player(self):
        ret = False
        if self.nb_player == 1 :
            ret = True
            self.nb_player+=1
            self._Player2 = Player(symbol = "Q")
            self._Player2.initPos(self._map)
            return [{"i": f"{self._Player2._y}", "j":f"{self._Player2._x}", "content":self._Player2._symbol}],ret
        return [], ret