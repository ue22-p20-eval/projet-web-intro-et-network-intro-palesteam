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

@socketio.on("move")
def on_move_msg(json, methods=["GET", "POST"]):
    print("received move ws message")
    dx = json['dx']
    dy = json["dy"]

    data, ret = game.move(dx,dy)
    if ret:
        socketio.emit("response", data)

@socketio.on("add_player") 
def on_add_player_msg(json, methods=["GET","POST"]) :
    print("adding player")
    nb_player = json['nb']
    data,ret = game.add_player()
    if ret :
        socketio.emit("response_adding",data)


if __name__=="__main__":
    socketio.run(app, port=5001)


