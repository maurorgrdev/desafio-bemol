from crypt import methods
from flask import Blueprint

#Get UserController
from presentation.controllers.CheckCepController import CheckCep
CheckCepRouter = Blueprint('AddressController', __name__)

CheckCepRouter.route('/check-cep',methods=['POST'], )(CheckCep.check_cep)