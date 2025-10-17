from flask import Flask
from flask_socketio import SocketIO, emit
import threading

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def index():
    return "Chat backend is running!"

@socketio.on('message')
def handle_message(msg):
    print("Message received from client:", msg)
    emit('message', msg, broadcast=True)

# Background task to read input and broadcast
def backend_input():
    while True:
        msg = input("Enter backend message: ")
        socketio.emit('message', f"Backend: {msg}", namespace='/', to=None)

if __name__ == '__main__':
    # Start input thread
    thread = threading.Thread(target=backend_input)
    thread.daemon = True
    thread.start()

    # Run SocketIO server
    socketio.run(app, host='0.0.0.0', port=5000)