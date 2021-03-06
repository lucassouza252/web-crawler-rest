from flask import Flask
from flask_restx import Api

class Server():
    def __init__(self) -> None:
        self.app = Flask(__name__)
        self.api = Api(
            self.app, 
            version="1.0", 
            title="News Crawler", 
            description="Rest API with crawler endpoint.", 
            doc="/docs"
        )
    
    def run(self) -> None:
        self.app.run(debug=True)

server = Server()