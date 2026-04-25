import json
from pathlib import Path
import requests
import base64
import pandas as pd

def carregar_credenciais_spotify(caminho_json=r"config/credentials/secrets.json"):
    caminho = Path(caminho_json)

    if not caminho.exists():
        raise FileNotFoundError(f"Arquivo de credenciais não encontrado: {caminho}")

    with open(caminho, "r", encoding="utf-8") as arquivo:
        config = json.load(arquivo)

    client_id = config["spotify"]["client_id"]
    client_secret = config["spotify"]["client_secret"]

    if not client_id or not client_secret:
        raise ValueError("client_id ou client_secret estão vazios.")

    return client_id, client_secret

class SpotifyAPI:
    def __init__(self, client_id: str, client_secret: str):
        self.client_id = client_id
        self.client_secret = client_secret
        self.token = None

    @staticmethod
    def from_json(caminho_json="config/secrets.json"):
        caminho = Path(caminho_json)

        if not caminho.exists():
            raise FileNotFoundError(
                f"Arquivo de credenciais não encontrado: {caminho}"
            )

        with open(caminho, "r", encoding="utf-8") as arquivo:
            config = json.load(arquivo)

        client_id = config["spotify"]["client_id"]
        client_secret = config["spotify"]["client_secret"]

        return SpotifyAPI(client_id, client_secret)

    def get_token(self):
        auth_url = "https://accounts.spotify.com/api/token"

        auth_header = base64.b64encode(
            f"{self.client_id}:{self.client_secret}".encode()
        ).decode()

        headers = {
            "Authorization": f"Basic {auth_header}"
        }

        data = {
            "grant_type": "client_credentials"
        }

        response = requests.post(auth_url, headers=headers, data=data)

        if response.status_code != 200:
            raise Exception(
                f"Erro ao obter token: {response.status_code} - {response.text}"
            )

        self.token = response.json()["access_token"]
        return self.token

# client_id, client_secret = carregar_credenciais_spotify()

# print("Client ID: " + client_id + "\nClient Secret: " + client_secret)

spotify = SpotifyAPI.from_json(r"C:\Users\leona\OneDrive\Documentos\MBA Eng Dados\Projeto Final de curso\eng-tech\config\secrets.json")
token = spotify.get_token()

print("Token gerado com sucesso. \nToken: " + token)