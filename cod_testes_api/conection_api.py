import base64
import requests
import pandas as pd
from typing import Dict, Any, List


class SpotifyClient:
    """
    Cliente para autenticação e consumo da API do Spotify.
    """

    AUTH_URL = "https://accounts.spotify.com/api/token"
    BASE_URL = "https://api.spotify.com/v1"

    def __init__(self, client_id: str, client_secret: str) -> None:
        self.client_id = client_id
        self.client_secret = client_secret
        self.access_token = self._get_access_token()

    def _get_access_token(self) -> str:
        """
        Obtém token de acesso (Client Credentials Flow).
        """
        auth_str = f"{self.client_id}:{self.client_secret}"
        b64_auth_str = base64.b64encode(auth_str.encode()).decode()

        headers = {
            "Authorization": f"Basic {b64_auth_str}"
        }

        data = {
            "grant_type": "client_credentials"
        }

        response = requests.post(self.AUTH_URL, headers=headers, data=data)

        if response.status_code != 200:
            print(response.text)
            response.raise_for_status()

        response.raise_for_status()

        return response.json()["access_token"]

    def _get_headers(self) -> Dict[str, str]:
        return {
            "Authorization": f"Bearer {self.access_token}"
        }

    def _request(self, url: str, params: Dict[str, Any]) -> Dict[str, Any]:
        response = requests.get(
            url,
            headers=self._get_headers(),
            params=params
        )

        print("STATUS:", response.status_code)
        print("URL:", response.url)
        print("RESPONSE:", response.text)

        response.raise_for_status()
        return response.json()

    def search_artists_paginated(
        self,
        artist_name: str,
        total: int = 200
    ) -> pd.DataFrame:
        """
        Busca artistas com paginação (limit=50).
        """
        all_artists: List[Dict[str, Any]] = []
        limit = 50

        for offset in range(0, total, limit):

            params = {
                "q": artist_name,
                "type": "artist",
                "limit": 10,
                "offset": offset
            }

            data = self._request(
                f"{self.BASE_URL}/search",
                params
            )

            items = data["artists"]["items"]

            if not items:
                break

            all_artists.extend(items)

        return self._transform_artists(all_artists)

    @staticmethod
    def _transform_artists(artists: List[Dict[str, Any]]) -> pd.DataFrame:
        """
        Normaliza o JSON de artistas para DataFrame.
        """
        records = []

        for artist in artists:

            # imagem principal (maior resolução)
            image_url = None
            if artist.get("images"):
                image_url = artist["images"][0]["url"]

            records.append({
                "artist_id": artist.get("id"),
                "artist_name": artist.get("name"),
                "artist_type": artist.get("type"),
                "spotify_url": artist.get("external_urls", {}).get("spotify"),
                "api_href": artist.get("href"),
                "uri": artist.get("uri"),
                "image_url": image_url
            })

        return pd.DataFrame(records)


# =========================
# EXECUÇÃO
# =========================
if __name__ == "__main__":

    CLIENT_ID = "ba291c9bb13a420aaf366b6e11bebbf1"
    CLIENT_SECRET = "8318e3c15b2c4be480814469b1b32db3"

    spotify = SpotifyClient(CLIENT_ID, CLIENT_SECRET)

    df_artists = spotify.search_artists_paginated(
        artist_name="Drake",
        total=200  # controla quantos você quer buscar
    )

    print(df_artists)
    print(f"Total de artistas coletados: {len(df_artists)}")