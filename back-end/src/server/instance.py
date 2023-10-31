from flask import Flask, Blueprint
from flask_restx import Api

# Server Instance

class Server():
    def __init__(self) -> None:
        self.app = Flask(__name__)
        self.blueprint = Blueprint('api', __name__, url_prefix='/api')
        self.api = Api(self.blueprint, doc='/doc', title='Street Flask API')
        self.app.register_blueprint(self.blueprint)

        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/street'
        self.app.config['PROPAGATE_EXCEPTIONS'] = True
        self.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

        self.user_ns = self.user_ns()
        self.address_ns = self.address_ns()
        self.check_cep_ns = self.check_cep_ns()

    def user_ns(self, ):
        return self.api.namespace(name='User', description='users realeted operations', path='/')
    
    def address_ns(self, ):
        return self.api.namespace(name='Address', description='address realeted operations', path='/')
    
    def check_cep_ns(self, ):
        return self.api.namespace(name='Check Cep', description='check_cep realeted operations', path='/')

    def run(self, ):
        self.app.run(
            port=9000,
            debug=True,
            host='0.0.0.0'
        )

server = Server()