from pathlib import Path
import pandas as pd
import time
from bib import SpotifyAPI

api = SpotifyAPI.from_json(r"C:\Users\leona\OneDrive\Documentos\MBA Eng Dados\Projeto Final de curso\eng-tech\config\secrets.json")

# 1. Carrega a lista original
df_lista = pd.read_csv(r"C:\Users\leona\OneDrive\Documentos\MBA Eng Dados\Projeto Final de curso\eng-tech\config\artists.csv", header=None, sep=',').transpose()
df_lista.columns = ["artista"]
df_lista["artista"] = df_lista["artista"].str.strip()
df_lista = df_lista.reset_index(drop=True)

pasta_saida = Path(r"C:\Users\leona\OneDrive\Documentos\MBA Eng Dados\Projeto Final de curso\eng-tech\backend\arq")
pasta_saida.mkdir(parents=True, exist_ok=True)

# Marca o início
inicio = time.perf_counter()

# 2. Loop usando a df_lista
for i in range(len(df_lista)):
    # .values[0] ou .item() garante que pegamos apenas a STRING do nome
    nome_artista = df_lista.loc[i, "artista"]
    print(f"Processando Artista {i+1}: {nome_artista}")
    
    try:
        artistas_res = api.request_paginated(
            endpoint="search",
            params={
                "q": nome_artista,
                "type": "artist"
            },
            chave_principal="artists",
            limit=10,
            max_paginas=4
        )

        # Criamos um NOVO dataframe para os resultados da busca (df_res)
        # Assim não sobrescrevemos a lista original (df_lista)
        df_res = pd.json_normalize(artistas_res)

        # Limpa o nome do artista para evitar caracteres proibidos em nomes de arquivos (\ / : * ? " < > |)
        nome_arquivo_limpo = "".join(c for c in nome_artista if c.isalnum() or c in (' ', '_')).strip()

        # Salva o arquivo CSV
        df_res.to_csv(
            pasta_saida / f"artista_{i+1}_{nome_arquivo_limpo}.csv",
            index=False,
            encoding='utf-8-sig' # Garante compatibilidade com acentos no Excel
        )

    except Exception as e:
        print(f"Erro ao processar {nome_artista}: {e}")

    # time.sleep(0.3)

# Marca o fim
fim = time.perf_counter()

tempo_total = fim - inicio
print(f"Tempo de execução: {tempo_total:.4f} segundos")