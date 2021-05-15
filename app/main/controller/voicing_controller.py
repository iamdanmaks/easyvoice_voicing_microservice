from flask import request
from flask_restplus import Resource

from flask_restplus import Namespace, fields

from ..service.voicing_service import voice_text


api = Namespace('text voicing', description='voicing related operations')
voice = api.model('text_voicing', {
        'voice_id': fields.String(required=True, description='voice public id'),
        'query_id': fields.String(required=True, description='query public id'),
        'text': fields.String(required=True, description='string with text to be voiced')
    })


@api.route('/')
class TextVoicing(Resource):
    @api.response(200, 'Text successfully voiced.')
    @api.doc('voice the text')
    @api.expect(voice)
    def post(self):
        """Voice the text """
        data = request.json
        return voice_text(
            data.get('voice_id'), 
            data.get('query_id'),
            data.get('text')
        )
