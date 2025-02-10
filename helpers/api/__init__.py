from flask_restful import Resource, Api
from resources.IndexResouce import IndexResource
from resources.PropriedadeResource import PropriedadesResource

api = Api(prefix="/api")

api.add_resource(IndexResource, '/')

api.add_resource(PropriedadesResource, '/propriedades')
