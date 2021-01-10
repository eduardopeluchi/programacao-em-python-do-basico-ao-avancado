import requests
url = "https://www.conderg.org.br/"

if requests.get(url).status_code == 200:
    print("O servidor está disponível.")
else:
    print("O servidor está indisponível.")

input("Pressione ENTER para continuar...")