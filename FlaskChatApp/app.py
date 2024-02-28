from flask import Flask, render_template, request, session, redirect
from flask_socketio import send, SocketIO
#imports the variables from flask and flask socket

app = Flask(__name__)
app.config["SECRET_KEY"] = 'asd'
socketio = SocketIO(app)

@app.route('/')
def room():     
    return render_template('room.html')

if __name__ == "__main__":
    socketio.run(app, debug=True, port=5001)