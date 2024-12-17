import psycopg2
from helpers.logging import logger


def main(args=[]):
    logger.info("Conectando com o banco de dados.")
    connection = psycopg2.connect(database="agriculaif",
                                  user="postgres",
                                  password="123456",
                                  host="localhost",
                                  port="5434")

    logger.info("Criando as tabelas.")
    with connection.cursor() as cursor:
        cursor.execute(open("schema.sql", "r").read())

    logger.info("Finalizado com sucesso!")
    connection.close()


if __name__ == '__main__':
    main()
