from marshmallow import Schema, fields, validate

propriedade_fields = {
    'nome': fields.String,
    'cidade': fields.String,
}


class Propriedade():
    def __init__(self, nome, cidade) -> None:
        self.nome = nome
        self.cidade = cidade

    def __repr__(self) -> str:
        return f"<Propriedade: {self.nome}, {self.cidade}>"

    def getNome(self):
        return self.nome

    def toJson(self):
        return {'nome': self.nome, 'cidade': self.cidade}


class PropriedadeSchema(Schema):
    nome = fields.String(validate=validate.Length(min=2, max=50),
                         required=True, error_messages={"required": "Nome é obrigatório."})
    cidade = fields.String(required=True)
