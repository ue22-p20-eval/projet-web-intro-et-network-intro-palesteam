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
            data, ret, lifes = self._player[nb_player].move(dx, dy, self._map, self._player)
            if type(data)==bool:
                self._generator = Generator(width=64, height=32)
                self._generator.gen_level()
                self._generator.gen_tiles_level()
                self._map = self._generator.tiles_level
                
                data = []
                for y in range(len(self._map)) :
                    for x in range(len(self._map[0])) :
                        data.append({"i": f"{y}", "j":f"{x}", "content":self._map[y][x]})

                for p in self._player :
                    p.initPos( self._map )
                    data.append({"i": f"{p.y_init}", "j":f"{p.x_init}", "content":p._symbol})

            return data, ret, lifes
                

        else : 
            return [], False, [e.vie for e in self._player]

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