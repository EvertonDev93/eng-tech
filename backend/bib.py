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
    
    def renovar_token(self):
        """
        Renova o access token da API do Spotify.

        No fluxo Client Credentials, não existe refresh_token.
        A renovação é feita solicitando um novo access_token.
        """
        self.token = None
        return self.get_token()
    
    def _headers(self):
        """
        Monta os headers de autenticação para chamadas na API do Spotify.
        Caso ainda não exista token, gera um novo token automaticamente.
        """
        if not self.token:
            self.get_token()

        return {
            "Authorization": f"Bearer {self.token}"
        }
    
    def tratar_resposta_api(self, response):
        """
        Trata a resposta da API do Spotify.

        Retorna o JSON quando a chamada for bem-sucedida.
        Caso contrário, lança erros mais claros para depuração.
        """

        if response.status_code in [200, 201]:
            return response.json()

        if response.status_code == 204:
            return {}

        if response.status_code == 400:
            raise Exception(
                f"Erro 400 - Requisição inválida.\n"
                f"URL: {response.url}\n"
                f"Resposta: {response.text}"
            )

        if response.status_code == 401:
            raise Exception(
                f"Erro 401 - Token inválido ou expirado.\n"
                f"URL: {response.url}\n"
                f"Resposta: {response.text}"
            )

        if response.status_code == 403:
            raise Exception(
                f"Erro 403 - Sem permissão para acessar este recurso.\n"
                f"URL: {response.url}\n"
                f"Resposta: {response.text}"
            )

        if response.status_code == 404:
            raise Exception(
                f"Erro 404 - Recurso não encontrado.\n"
                f"URL: {response.url}\n"
                f"Resposta: {response.text}"
            )

        if response.status_code == 429:
            retry_after = response.headers.get("Retry-After", "não informado")

            raise Exception(
                f"Erro 429 - Limite de requisições atingido.\n"
                f"Tente novamente após: {retry_after} segundos.\n"
                f"URL: {response.url}\n"
                f"Resposta: {response.text}"
            )

        if response.status_code >= 500:
            raise Exception(
                f"Erro {response.status_code} - Erro no servidor do Spotify.\n"
                f"URL: {response.url}\n"
                f"Resposta: {response.text}"
            )

        raise Exception(
            f"Erro inesperado: {response.status_code}\n"
            f"URL: {response.url}\n"
            f"Resposta: {response.text}"
        )
    
    def request_get(self, endpoint, params=None, tentar_renovar_token=True):
        """
        Executa uma chamada GET genérica na API do Spotify.

        Args:
            endpoint (str): Endpoint da API. Ex: 'search' ou 'artists/{id}/albums'
            params (dict): Parâmetros da consulta.
            tentar_renovar_token (bool): Se True, renova o token automaticamente em erro 401.

        Returns:
            dict: Resposta da API em formato JSON.
        """

        base_url = "https://api.spotify.com/v1"

        url = f"{base_url}/{endpoint.lstrip('/')}"

        response = requests.get(
            url,
            headers=self._headers(),
            params=params,
            timeout=30
        )

        if response.status_code == 401 and tentar_renovar_token:
            self.renovar_token()

            response = requests.get(
                url,
                headers=self._headers(),
                params=params,
                timeout=30
            )

        return self.tratar_resposta_api(response)
    
    def request_paginated(
        self,
        endpoint,
        params=None,
        chave_principal=None,
        chave_items="items",
        limit=50,
        max_paginas=None
    ):
        """
        Executa chamadas GET paginadas na API do Spotify.

        Args:
            endpoint (str): Endpoint da API. Ex: 'search', 'artists/{id}/albums'
            params (dict): Parâmetros da consulta.
            chave_principal (str): Chave principal onde ficam os dados paginados.
                                Ex: 'artists', 'tracks', 'albums', 'playlists'.
                                Use None quando o retorno já tiver 'items' na raiz.
            chave_items (str): Nome da chave que contém os registros. Normalmente 'items'.
            limit (int): Quantidade de registros por página.
            max_paginas (int): Número máximo de páginas para buscar. Se None, busca tudo.

        Returns:
            list: Lista com todos os registros encontrados.
        """

        if params is None:
            params = {}

        todos_items = []
        offset = params.get("offset", 0)
        pagina_atual = 0

        while True:
            params_pagina = params.copy()
            params_pagina["limit"] = limit
            params_pagina["offset"] = offset

            dados = self.request_get(
                endpoint=endpoint,
                params=params_pagina
            )

            if chave_principal:
                bloco = dados.get(chave_principal, {})
            else:
                bloco = dados

            items = bloco.get(chave_items, [])

            if not items:
                break

            todos_items.extend(items)

            pagina_atual += 1

            if max_paginas is not None and pagina_atual >= max_paginas:
                break

            proxima_pagina = bloco.get("next")

            if not proxima_pagina:
                break

            offset += limit

        return todos_items

# client_id, client_secret = carregar_credenciais_spotify()

# print("Client ID: " + client_id + "\nClient Secret: " + client_secret)

# api = SpotifyAPI.from_json(r"C:\Users\leona\OneDrive\Documentos\MBA Eng Dados\Projeto Final de curso\eng-tech\config\secrets.json")

# dados = api.request_get(
#     endpoint="search",
#     params={
#         "q": "Drake",
#         "type": "artist",
#         "limit": 10
#     }
# )

# print(dados)