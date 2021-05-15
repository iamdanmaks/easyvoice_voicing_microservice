from flask_restplus import Api
from flask import Blueprint

from .main.controller.voicing_controller import api as voicing_ns


blueprint = Blueprint('api', __name__)

api = Api(blueprint,
            title='TEXT VOICING MICROSERVICE',
            version='1.0',
            description='flask restplus microservice'
          )

api.add_namespace(voicing_ns, path='/voice')
