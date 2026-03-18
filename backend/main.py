from fastapi import FastAPI
from db import conectar_db
app = FastAPI()

@app.get("/listo")
def home():
    return {"status": "ok", "mensaje": "API funcionando 🚀"}


@app.post("/login")
def login(email: str, password: str):

    # 1. conectar a la DB
    conn = conectar_db()
    cursor = conn.cursor()

    # 2. ejecutar query
    query = "SELECT * FROM usuarios WHERE email = %s AND password = %s"
    cursor.execute(query, (email, password))

    # 3. obtener resultado
    user = cursor.fetchone()

    # 4. cerrar conexión
    cursor.close()
    conn.close()

    # 5. lógica con Python
    if user:
        return {"mensaje": "Login exitoso"}
    else:
        return {"error": "Credenciales incorrectas"}