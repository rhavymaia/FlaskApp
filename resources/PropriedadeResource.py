from flask import Blueprint, jsonify, request
from marshmallow import ValidationError
from psycopg2 import Error as DatabaseError

from helpers.logging import logger
from helpers.database import getConnection

from models.Propriedade import Propriedade, PropriedadeSchema

propriedades_route = Blueprint(
    'propriedades', __name__, url_prefix='/propriedades')


@propriedades_route.get("")
def propriedades_get():
    try:
        logger.info("Listando propriedades")
        # 1 - Conectar.
        connection = getConnection()
        # 2 - Obter cursor.
        cursor = connection.cursor()
        # 3 - Executar.
        cursor.execute(
            "select * from tb_propriedades")
        # 4 - retorna resultset
        resultset = cursor.fetchall()
        # Iterar e transformar dados.
        propriedades = []
        for item in resultset:
            id = item[0]
            nome = item[1]
            cidade = item[2]
            propriedade = Propriedade(id, nome, cidade)
            logger.info(propriedade)
            propriedades.append(propriedade.toJson())
    except DatabaseError as e:
        return jsonify({'error': str(e)}), 500

    return jsonify(propriedades), 200


@propriedades_route.post("")
def propriedades_post():

    logger.info("Inserindo propriedade")
    # Validação
    schema = PropriedadeSchema()

    try:
        # Captar o json da requisição e adicionar na lista.
        data = request.json
        propriedadeNova = schema.load(data)

        # 1 - Conectar.
        connection = getConnection()

        # 2 - Obter cursor.
        cursor = connection.cursor()

        # 3 - Executar.
        cursor.execute(
            "insert into tb_propriedades(nome, cidade) values (?, ?)", (propriedadeNova['nome'], propriedadeNova['cidade']))

        # 3.1 - Confirmar - commit.
        connection.commit()

        # id = cursor.lastrowid
        # propriedadeNova['id'] = id

        resultset = cursor.fecthone()

    except ValidationError as err:
        return jsonify({'error': err.messages}), 400
    except DatabaseError as e:
        return jsonify({'error': str(e)}), 500

    return jsonify(propriedadeNova), 200


def getPropriedadeById(idPropriedade):
    try:
        # Retornar o resultset.
        # 1 - Conectar.
        connection = getConnection()
        # 2 - Obter cursor.
        cursor = connection.cursor()
        # 3 - Executar.
        cursor.execute(
            "select * from tb_propriedades where id = ?", (idPropriedade,))
        # 4 - Retornar resultset
        resultset = cursor.fetchone()  # [] -> ()
    except sqlite3.Error as e:
        return jsonify({'error': str(e)}), 500

    return resultset


@propriedades_route.get("/<int:idPropriedade>")
def propriedade_get(idPropriedade):
    try:
        resultset = getPropriedadeById(idPropriedade)
        # Transformar dados.
        if resultset is not None:
            propriedade = {
                'id': resultset[0], 'nome': resultset[1], 'cidade': resultset[2]}
        else:
            return (jsonify({'mensagem': 'Propriedade não encontrada'}), 404)
    except DatabaseError as e:
        return jsonify({'error': str(e)}), 500

    return jsonify(propriedade), 200


@propriedades_route.put("/<int:idPropriedade>")
def propriedades_put(idPropriedade):
    try:
        # Captar o json da requisição e adicionar na lista.
        propriedadeAtualizada = request.json
        # 1 - Conectar.
        connection = getConnection()
        # 2 - Obter cursor.
        cursor = connection.cursor()
        # Verificar se a pripriedade a ser atualizada existe.
        resultset = getPropriedadeById(idPropriedade)
        if resultset is not None:
            # 3 - Executar.
            cursor.execute("update tb_propriedades set nome=?, cidade=? where id=?",
                           (propriedadeAtualizada['nome'], propriedadeAtualizada['cidade'], idPropriedade))
            # 3.1 - Confirmar - commit.
            connection.commit()
            # Adicionar id ao json.
            propriedadeAtualizada['id'] = idPropriedade
            return jsonify(propriedadeAtualizada), 200
    except DatabaseError as e:
        return jsonify({'error': str(e)}), 500

    return (jsonify({'mensagem': 'Propriedade não encontrada'}), 404)


@propriedades_route.delete("/<int:idPropriedade>")
def propriedades_delete(idPropriedade):
    try:
        # 1 - Conectar.
        connection = getConnection()
        # 2 - Obter cursor.
        cursor = connection.cursor()
        # Verificar se a pripriedade a ser atualizada existe.
        resultset = getPropriedadeById(idPropriedade)
        if resultset is not None:
            # 3 - Executar.
            cursor.execute(
                "delete from tb_propriedades where id = ?", (idPropriedade, ))
            # 3.1 - Confirmar - commit.
            connection.commit()
            return {'mensagem': "Removido com sucesso"}, 200
    except DatabaseError as e:
        return jsonify({'error': str(e)}), 500

    return (jsonify({'mensagem': 'Propriedade não encontrada'}), 404)
