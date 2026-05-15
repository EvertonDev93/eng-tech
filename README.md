# 📊 EngTech: Inteligência de Dados para Sobrevivência Empresarial

**Projeto de TCC em Engenharia de Dados com abordagem prática (Hands On), focado na construção de uma solução de dados end-to-end para análise de risco empresarial no Brasil.**

### 👥 Integrantes

* **Davi Araujo** - 10731795
* **Rafael Cruz** - 10732175
* **Everton Ribeiro** - 10732297
* **Felipe Santana** - 10732452
* **Erickson Silva** - 10732435
* **Leonardo Gomes** - 10731860

---

## 🚀 1. Visão Geral e Contexto de Negócio

A taxa de mortalidade de empresas no Brasil é um fator crítico para o desenvolvimento econômico. Este projeto apresenta uma solução de dados completa para responder a um problema real: **qual a probabilidade de uma empresa encerrar as suas atividades nos primeiros 5 anos de vida?**

A análise utiliza variáveis estruturais, financeiras e regionais para identificar padrões que expliquem este fenómeno, permitindo uma tomada de decisão baseada em dados para empreendedores e investidores.

## 🔗 2. Detalhamento das Fontes de Dados (Data Sources)

Para solucionar a fragmentação e detalhar a origem técnica, as fontes de dados foram mapeadas diretamente dos repositórios oficiais:

* **Repositório de Arquivos (RFB):** [Arquivos Receita Federal](https://arquivos.receitafederal.gov.br/index.php/s/YggdBLfdninEJX9?dir=/2025-10)
* *O que é:* Servidor que aloja os ficheiros brutos compactados (.zip). É a fonte primária de onde o pipeline extrai os dados mensalmente.


* **Portal de Dados Abertos (Gov.br):** [Dados.gov.br - CNPJ](https://dados.gov.br/dados/conjuntos-dados/cadastro-nacional-da-pessoa-juridica---cnpj)
* *O que é:* Catálogo que fornece os metadados, layouts e a descrição técnica de cada campo das tabelas.



### 🗺️ Mapeamento de Tabelas vs. Arquivos

| Nome da Tabela | Arquivo de Origem (RFB) | Conteúdo e Aplicação no Projeto |
| --- | --- | --- |
| **EMPRESAS** | `K3241.K0312.V1.EMPRE.D...zip` | Dados estruturais: Capital Social, Natureza Jurídica e Porte. |
| **ESTABELECIMENTOS** | `K3241.K0312.V1.ESTABELE.D...zip` | Dados de operação: CNAE, Situação Cadastral e Localização. |
| **SIMPLES** | `K3241.K0312.V1.SIMPLES.D...zip` | Dados tributários: Identificação de MEI e regime Simples. |

## 🏗️ 3. Arquitetura da Solução e Pipeline ETL

Para garantir um fluxo coeso e evitar o isolamento de informações, a arquitetura conecta todas as etapas:

**<img width="2986" height="1408" alt="Diagrama Atualziado" src="https://github.com/user-attachments/assets/0f7a043c-1e01-42ee-880d-d568763a40a7" />**

Com certeza! Com base na nova arquitetura e no detalhamento do seu pipeline ETL (onde o processamento central migrou do Pandas/Python para comandos SQL nativos dentro do PostgreSQL), aqui está o texto atualizado e corrigido para refletir o novo fluxo:

🏗️ 3. Arquitetura da Solução e Pipeline ETL

A arquitetura da solução foi projetada para ser altamente eficiente e robusta, utilizando orquestração via script batch (EXECUTAR.BAT) e as poderosas capacidades nativas do PostgreSQL para todo o processamento de dados (Medallion Architecture). A nova abordagem remove a dependência do Pandas/Python para transformações, priorizando o processamento "in-database" para maior performance.

Ingestão e Landing Zone (Raw): O fluxo de dados brutos inicia-se a partir de repositórios locais (C:/rfb/), onde se encontram os arquivos compactados (.zip) e descompactados (.csv). A Landing Zone é constituída por este diretório local, garantindo a linhagem dos dados e permitindo o reprocessamento rápido sem a necessidade de novos downloads.

Camada Bronze (Staging Area): A ingestão é orquestrada por um arquivo .bat que aciona um Script Python executado em terminal. Através de comandos \copy SQL nativos, a tarefa automatizada realiza o carregamento direto dos dados dos ficheiros .csv para tabelas de estágio no PostgreSQL. Nesta Camada Bronze, os dados são mantidos em tabelas de estágio separadas (empresas_bruta, estabelecimentos_bruta, paises_bruta, etc.), persistindo sua estrutura original de texto (LATIN1) para auditoria e linhagem.

Processamento e Camada Silver (Trusted): A fase de processamento é realizada exclusivamente dentro do PostgreSQL, utilizando comandos SQL nativos e T-SQL para as transformações. O pipeline executa a leitura das tabelas da Camada Bronze para executar: tipagem de datas (TO_DATE de 'YYYYMMDD' para date, com verificação de NULL), tipagem numérica (capital social), conversão de encoding (LATIN1 para UTF-8), e normalização de texto (limpeza). Os dados higienizados e tipados são persistidos na Camada Silver em suas respectivas tabelas normalizadas (empresas, estabelecimentos, cnaes, municipios, simples), sem Joins pré-processados, sendo um repositório confiável, estruturado e normalizado.

Data Warehouse (Gold Ready): Os dados normalizados e confiáveis na Camada Silver estão prontos para o enriquecimento e a estruturação de visões denormalizadas na futura Camada Gold. Esta fase final será responsável pela criação de variáveis para o treinamento de modelos de Machine Learning e pelo fornecimento de dados de alta performance para o consumo por dashboards analíticos.

## 🧠 4. Dicionário de Dados e Engenharia de Features

Com base no critério de seleção técnica, o modelo foca nas variáveis de maior impacto preditivo:

* **Variável Alvo (Target):** `SITUAÇÃO CADASTRAL` (Ativa/Baixada) processada com a `DATA DA SITUAÇÃO` para definir a falência em até 5 anos.
* **Features Selecionadas:**
* `CAPITAL SOCIAL`: Indicador de resistência financeira.
* `CNAE FISCAL`: Setor económico de atuação.
* `NATUREZA JURÍDICA`: Estrutura legal da empresa.
* `UF / MUNICÍPIO`: Contexto económico regional.
* `PORTE DA EMPRESA`: Tamanho e resiliência no mercado.



## 🧰 5. Tecnologias Utilizadas

* **Linguagens:** Python (Pandas, Scikit-Learn) e SQL.
* **Armazenamento:** PostgreSQL (Data Warehouse).
* **Visualização:** Power BI e Streamlit.
* **Versionamento:** Git & GitHub.

## 📊 6. Resultados Esperados

* **Modelo Preditivo de Risco:** Algoritmo capaz de classificar a probabilidade de falência com base nos dados de registo.
* **Dashboard Executivo:** Visualização geográfica e setorial da mortalidade empresarial no Brasil.
* **Simulador de Viabilidade:** Interface em Streamlit onde o utilizador insere dados de uma nova empresa e recebe uma análise de risco imediata.

---
