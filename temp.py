import psycopg2
conn = psycopg2.connect(database="agriculaif",
                        user="postgres",
                        password="123456",
                        host="localhost",
                        port="5434")
