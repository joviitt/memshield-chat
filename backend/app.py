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

# Function to read from terminal and broadcast
def backend_input():
    while True:
        msg = input("Enter backend message: ")
        socketio.emit('message', f"Backend: {msg}", broadcast=True)

if __name__ == '__main__':
    # Run the input thread alongside Flask
    thread = threading.Thread(target=backend_input)
    thread.daemon = True
    thread.start()

    socketio.run(app, host='0.0.0.0', port=5000)