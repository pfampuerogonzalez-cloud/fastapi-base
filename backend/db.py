import psycopg2

def conectar_db():
    conn = psycopg2.connect(
        host="db",          # nombre del servicio en docker
        database="fastapi_db",
        user="admin",
        password="admin"
    )
    return conn