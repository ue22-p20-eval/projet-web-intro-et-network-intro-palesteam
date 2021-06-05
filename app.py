from flask import Flask, render_template 
from flask_socketio import SocketIO
from game_backend import Game

app = Flask(__name__)
socketio = SocketIO(app)
game = Game()


@app.route("/")
def index():
    map = game.getMap()
    return render_template("index.html", mapdata=map, n_row=len(map), n_col=len(map[0]) )

@socketio.on("move1")
def on_move_msg(json, methods=["GET", "POST"]):
    print("received move1 ws message")
    dx = json['dx']
    dy = json["dy"]

    data, ret, lifes = game.move(dx,dy,0)
    if ret:
        socketio.emit("response_move1", [data, lifes])
        
#if the player 2 moves
@socketio.on("move2")
def on_move_msg(json, methods=["GET", "POST"]):
    print("received move2 ws message")
    dx = json['dx']
    dy = json["dy"]

    data, ret, lifes = game.move(dx,dy,1)
    if ret:
        socketio.emit("response_move2", [data, lifes])

#adding a player
@socketio.on("add_player") 
def on_add_player_msg(json, methods=["GET","POST"]) :
    print("adding player")
    nb_player = json['nb']
    data,ret, lifes = game.add_player()
    if ret :
        socketio.emit("response_adding", [data, lifes])


if __name__=="__main__":
    socketio.run(app, port=5001)


