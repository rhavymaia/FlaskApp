from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Configuração para o primeiro banco
db.engine = db.create_engine(
    'postgresql://postgres:123456@localhost:5434/agriculaif')
