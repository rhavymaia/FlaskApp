from marshmallow import Schema, fields, validate


class Propriedade():
    def __init__(self, id, nome, cidade) -> None:
        self.id = id
        self.nome = nome
        self.cidade = cidade

    def __repr__(self) -> str:
        return f"<Propriedade: {self.id}, {self.nome}, {self.cidade}>"

    def getNome(self):
        return self.nome

    def toJson(self):
        return {'id': self.id, 'nome': self.nome, 'cidade': self.cidade}


class PropriedadeSchema(Schema):
    nome = fields.String(validate=validate.Length(min=2, max=50),
                         required=True, error_messages={"required": "Nome é obrigatório."})
    cidade = fields.String(required=True)
