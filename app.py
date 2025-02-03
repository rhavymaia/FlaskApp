from flask import request, jsonify

from helpers.application import app
from resources.PropriedadeResource import propriedades_route


@app.route("/")
def homeResource():
    aplicacao = {'versao': '1.0'}
    return jsonify(aplicacao), 200


app.register_blueprint(propriedades_route)
