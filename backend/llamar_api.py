import requests


def buscar_noticias(query):
    
    url = "https://newsapi.org/v2/everything"

    params = {
        "q":query,
        "language":"es",
        "apiKey":"aa7575b28a444037859696a6db42856c"
    }

    response = requests.get(url, params=params)
    data = response.json()

    return  data.get("articles" , [])
    















buscar_noticias("chile")










