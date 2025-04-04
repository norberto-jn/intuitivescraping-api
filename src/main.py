from flask import Flask
from flask_cors import CORS
from flask_socketio import SocketIO
from file.controllers.file_controller import file_controller

def create_app():
    app = Flask(__name__)
    CORS(app, resources={r"/*": {"origins": "*"}})
    socketio = SocketIO(app, cors_allowed_origins="*", async_mode='eventlet')
    app.register_blueprint(file_controller)
    
    return app, socketio

app, socketio = create_app()

if __name__ == '__main__':
    socketio.run(app, port=3001, debug=True, host='0.0.0.0')
