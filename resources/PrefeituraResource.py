from flask_restful import Resource, reqparse, marshal
from helpers.auth.token_handler.token_verificador import token_verifica
from model.endereco import *
from model.cidade import *
from model.prefeitura import *
from model.message import *
from helpers.database import db
from helpers.base_logger import logger


class Prefeituras(Resource):

    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('endereco', type=dict, help= 'Problema no endereço', required=True)
        self.parser.add_argument('nome', type=str, help='Problema no nome', required=True)
        self.parser.add_argument('secretario', type=str, help='Problema no id do secretario', required=True)

    @token_verifica
    def get(self, refresh_token, token_tipo):
        logger.info("Prefeituras listados com sucesso!")
        prefeituras = Prefeitura.query.all()
        return marshal(prefeituras, prefeitura_fields), 200

    @token_verifica
    def post(self, refresh_token, token_tipo):
        args = self.parser.parse_args()
        try:
            nome = args["nome"]
            secretario = args["secretario"]
            enderecoResponse = args["endereco"]

            #Criar endereço
            endereco = Endereco(
                cep=enderecoResponse["cep"],
                numero=enderecoResponse["numero"],
                complemento=enderecoResponse["complemento"],
                referencia=enderecoResponse["referencia"],
                logradouro=enderecoResponse["logradouro"],
                id_cidade=enderecoResponse["id_cidade"],
                id_pessoa=enderecoResponse["id_pessoa"]
            )

            db.session.add(endereco)
            db.session.commit()

            prefeitura = Prefeitura(nome, secretario, id_endereco=endereco.id)

            db.session.add(prefeitura)
            db.session.commit()

            logger.info("Prefeitura cadastrada com sucesso!")

            return marshal(prefeitura, prefeitura_fields), 201
        except Exception as e:
            logger.error(f"error: {e}")

            message = Message("Error ao cadastrar a Prefeitura", 2)
            return marshal(message, message_fields), 404

class PrefeituraById(Resource):

    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('endereco', type=dict, help= 'Problema no endereço', required=True)
        self.parser.add_argument('nome', type=str, help='Problema no nome', required=True)
        self.parser.add_argument('secretario', type=str, help='Problema no id do secretario', required=True)

    @token_verifica
    def get(self, refresh_token, token_tipo, id):
        prefeitura = Prefeitura.query.get(id)

        if prefeitura is None:
            logger.error(f"Prefeitura {id} não encontrado")

            message = Message(f"Prefeitura {id} não encontrado", 1)
            return marshal(message), 404

        logger.info(f"Prefeitura {id} encontrado com sucesso!")
        return marshal(prefeitura, prefeitura_fields)

    @token_verifica
    def put(self, refresh_token, token_tipo, id):
        args = self.parser.parse_args()

        try:
            prefeitura = Prefeitura.query.get(id)

            if prefeitura is None:
                logger.error(f"Prefeitura {id} não encontrado")
                message = Message(f"Prefeitura {id} não encontrado", 1)
                return marshal(message, message_fields)

            prefeitura.nome = args["nome"]
            prefeitura.secretario = args["secretario"]
            prefeitura.id_endereco = args["id_endereco"]

            db.session.add(prefeitura)
            db.session.commit()

            logger.info("Prefeitura cadastrado com sucesso!")
            return marshal(prefeitura, prefeitura_fields), 200
        except Exception as e:
            logger.error(f"error: {e}")

            message = Message("Error ao atualizar a Prefeitura", 2)
            return marshal(message, message_fields), 404

    @token_verifica
    def delete(self, refresh_token,token_tipo, id):
        prefeitura = Prefeitura.query.get(id)

        if prefeitura is None:
            logger.error(f"Prefeitura {id} não encontrado")
            message = Message(f"Prefeitura {id} não encontrado", 1)
            return marshal(message, message_fields)

        db.session.delete(prefeitura)
        db.session.commit()

        message = Message("Prefeitura deletado com sucesso!", 3)
        return marshal(message, message_fields), 200

class PrefeituraByNome(Resource):
    def get(self, nome):
        prefeitura = Prefeitura.query.filter(
            Prefeitura.nome.ilike(f"%{nome}%")
        ).all()

        if prefeitura is None:
            logger.error(f"Prefeitura {id} não encontrado")

            message = Message(f"Prefeitura {id} não encontrado", 1)
            return marshal(message), 404

        logger.info(f"Prefeitura {id} encontrado com sucesso!")
        return marshal(prefeitura, prefeitura_fields), 200