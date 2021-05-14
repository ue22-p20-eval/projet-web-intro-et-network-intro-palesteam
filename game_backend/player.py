

class Player:
    def __init__(self, symbol="@", vie=0):
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

    def move(self, dx, dy, map):
        new_x = self._x + dx
        new_y = self._y + dy
        if map[new_y][new_x] == "°" or map[new_y][new_x] == "x" or map[new_y][new_x] == "¤" :
            if map[new_y][new_x] == "¤" :
                self.vie += 1
            ret =True
            map[new_y][new_x] = self._symbol
            map[self._y][self._x] = "x"
            data = [{"i": f"{self._y}", "j":f"{self._x}", "content":"x"}, {"i": f"{new_y}", "j":f"{new_x}", "content":self._symbol}]
            self._x = new_x
            self._y = new_y

        elif map[new_y][new_x] == "§" or map[new_y][new_x] == "H":
            if self.vie >= 1:
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
        else:
            ret = False
            data = []
        return data, ret
