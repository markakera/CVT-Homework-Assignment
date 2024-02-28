from flask import Flask, render_template, request, session, redirect
from flask_socketio import join_room,leave_room, send, SocketIO
#imports the variables from flask and flask socket

app = Flask(__name__)
app.config["SECRET_KEY"] = 'asd'
socketio = SocketIO(app)
#creates socketIO instance which binds it with the created flask application (app flask) and a secret key for extra security    

clients_inside = 0

@app.route("/room", methods=["POST", "GET"])
def room():     
    return render_template('base.html')
#a function that gets called when ever theres a request for the root url
#so when ever a user vists the url, he meets the room.html template

@socketio.on('connect')
def connect():
    if clients_inside>=2:
        print('cant join chatroom, full')
        return False
    else:
        join_room('room')
        print('client connected')
        clients_inside = clients_inside + 1
#a function that lets user connect unless there are 2 already inside

@socketio.on('disconnect')
def disconnect():
    leave_room('room')
    clients_inside = clients_inside-1
    print("client disconnected")
#a function that lets a user disconnect

@socketio.on('send_message')
def messaging(data):
    sender = data['sender']
    message = data['message']
    send({'sender':sender,'message':message}room:'room')
# a function that lets a user send a message , which will be broadcasted in the chatroom

if __name__ == "__main__":
    socketio.run(app)