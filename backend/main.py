from pathlib import Path
import pandas as pd
import time
from bib import SpotifyAPI

def salvar_dataframe_excel(df: pd.DataFrame, caminho_saida: Path):
    """
    Salva um DataFrame em Excel criando a pasta de destino, se necessário.
    """
    caminho_saida.parent.mkdir(parents=True, exist_ok=True)
    df.to_excel(caminho_saida, index=False)

api = SpotifyAPI.from_json(r"C:\Users\leona\OneDrive\Documentos\MBA Eng Dados\Projeto Final de curso\eng-tech\config\secrets.json")

pasta_saida = Path(r"C:\Users\leona\OneDrive\Documentos\MBA Eng Dados\Projeto Final de curso\eng-tech\backend\arq")
pasta_saida.mkdir(parents=True, exist_ok=True)

# Marca o início
inicio = time.perf_counter()

# ==========================
# 1. Search Artists
# ==========================
artistas = api.search_artists(
    artist_name="Drake",
    limit=10,
    max_paginas=1
)

df_artistas = pd.json_normalize(artistas)

salvar_dataframe_excel(
    df=df_artistas,
    caminho_saida=pasta_saida / "search_artists_drake.xlsx"
)

print("Arquivo gerado: data/raw/search_artists_drake.xlsx")
print(df_artistas.head())

# ==========================
# 2. Search Tracks
# ==========================
musicas = api.search_tracks(
    track_name="One Dance",
    limit=10,
    max_paginas=1,
    market="BR"
)

df_musicas = pd.json_normalize(musicas)

salvar_dataframe_excel(
    df=df_musicas,
    caminho_saida=pasta_saida / "search_tracks_one_dance.xlsx"
)

print("Arquivo gerado: data/raw/search_tracks_one_dance.xlsx")
print(df_musicas.head())

# ==========================
# 3. Search Albums
# ==========================
albuns = api.search_albums(
    album_name="Scorpion",
    limit=10,
    max_paginas=1,
    market="BR"
)

df_albuns = pd.json_normalize(albuns)

salvar_dataframe_excel(
    df=df_albuns,
    caminho_saida=pasta_saida / "search_albums_scorpion.xlsx"
)

print("Arquivo gerado: data/raw/search_albums_scorpion.xlsx")
print(df_albuns.head())

# ==========================
# 4. Search Playlists
# ==========================
playlists = api.search_playlists(
    playlist_name="Top Brasil",
    limit=10,
    max_paginas=1,
    market="BR"
)

df_playlists = pd.json_normalize(playlists)

salvar_dataframe_excel(
    df=df_playlists,
    caminho_saida=pasta_saida / "search_playlists_top_brasil.xlsx"
)

print("Arquivo gerado: data/raw/search_playlists_top_brasil.xlsx")
print(df_playlists.head())

print("\nTodos os arquivos foram gerados com sucesso.")

# Marca o fim
fim = time.perf_counter()

tempo_total = fim - inicio

print(f"Tempo de execução: {tempo_total:.4f} segundos")