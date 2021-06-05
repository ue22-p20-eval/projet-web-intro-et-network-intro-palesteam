

class Player:
    def __init__(self, symbol="@", vie=1):
        self._symbol = symbol
        self.x_init = None
        self.y_init = None
        self._x = None
        self._y = None
        self.vie = vie

    def initPos(self, _map):
        n_row = len(_map)
        n_col = len(_map[0])

        y_init = n_row//2
        found = False
        while found is False:
            y_init += 1
            for i,c in enumerate(_map[y_init]):
                if c == "°":
                    x_init = i
                    found = True
                    break

        self.x_init = x_init
        self.y_init = y_init
        self._x = x_init
        self._y = y_init

        _map[self._y][self._x] = self._symbol

    def move(self, dx, dy, map, list_player):
        new_x = self._x + dx
        new_y = self._y + dy
        if map[new_y][new_x] == "°" or map[new_y][new_x] == "x" or map[new_y][new_x] == "¤" or map[new_y][new_x] == "D" :
            if map[new_y][new_x] == "¤" :
                self.vie += 1
            ret =True
            map[new_y][new_x] = self._symbol
            map[self._y][self._x] = "x"
            data = [{"i": f"{self._y}", "j":f"{self._x}", "content":"x"}, {"i": f"{new_y}", "j":f"{new_x}", "content":self._symbol}]
            self._x = new_x
            self._y = new_y

        #if the player walks on a monster
        elif map[new_y][new_x] == "§" or map[new_y][new_x] == "H":
            if self.vie > 1:
                ret =True
                map[new_y][new_x] = self._symbol
                map[self._y][self._x] = "x"
                data = [{"i": f"{self._y}", "j":f"{self._x}", "content":"x"}, {"i": f"{new_y}", "j":f"{new_x}", "content":self._symbol}]
                self._x = new_x
                self._y = new_y
                self.vie -= 1 
            else:
                ret =True
                map[new_y][new_x] = "D"
                map[self._y][self._x] = "x"
                map[self.y_init][self.x_init] = self._symbol
                data = [{"i": f"{self.y_init}", "j":f"{self.x_init}", "content":self._symbol}, {"i": f"{new_y}", "j":f"{new_x}", "content":"D"}, {"i": f"{self._y}", "j":f"{self._x}", "content":"x"}]
                self._x = self.x_init
                self._y = self.y_init

        #if the player tries to walk (attacks) another player
        elif map[new_y][new_x] in [e._symbol for e in list_player] :
            ret = False
            data = []
            for i in range(len(list_player)) :
                if map[new_y][new_x] == list_player[i]._symbol :
                    data, ret = list_player[i].hit(map)
                
        else:
            ret = False
            data = []

        return data, ret, [e.vie for e in list_player]

    #when a player is hit by another player
    def hit(self, map) :
        if self.vie > 1 :
            self.vie -= 1
            ret = True
            data = []
        else : 
            ret = True
            map[self._y][self._x] = "D"
            map[self.y_init][self.x_init] = self._symbol
            data = [{"i": f"{self.y_init}", "j":f"{self.x_init}", "content":self._symbol}, {"i": f"{self._y}", "j":f"{self._x}", "content":"D"}]
            self._x = self.x_init
            self._y = self.y_init

        return data,ret