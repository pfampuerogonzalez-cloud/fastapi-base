from fastapi import FastAPI
from db import conectar_db
from llamar_api import buscar_noticias
from noticias_a_db import guardar_noticias


app = FastAPI()


@app.get("/")
def home():
    return {"status": "ok", "mensaje": "API funcionando 🚀"}


@app.post("/obtener_noticias")
def  obtener_noticias(query: str):

    if not query:
        return {"error": "query vacío"}

    lista_de_noticias = buscar_noticias(query)
    guardar = guardar_noticias(lista_de_noticias)

    return {
        "mensaje":"noticias agregadas",
        "cantidad": guardar
    }

@app.get("/listar_desde_db")
def listar_noticias():
    conn = conectar_db()
    cursor = conn.cursor()

    cursor.execute("SELECT titulo, descripcion FROM noticias")

    noticias = cursor.fetchall()

    cursor.close()
    conn.close()
    news = []
    for n in noticias:
        noticias.append({
            "titulo": n[0],
            "description":n[1]
        
        })
        return noticias
    

    








