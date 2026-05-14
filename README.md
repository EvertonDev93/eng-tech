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

**<img width="1024" height="483" alt="3bfe3986-00e5-41b2-afac-264bba54664e" src="https://github.com/user-attachments/assets/8c0e6574-ff3d-471a-8683-2a8ede78535e" />**

1. **Ingestão:** Scripts Python automatizam o download dos ficheiros `.zip` diretamente dos links da Receita Federal.
2. **Landing Zone (Raw):** Armazenamento dos dados brutos para garantir a linhagem e possibilidade de reprocessamento.
3. **Processamento (Bronze/Silver):** Descompactação e limpeza via Pandas. Aqui é realizado o **Join** crucial entre *Empresas* e *Estabelecimentos* através do `CNPJ BÁSICO`.
4. **Data Warehouse (Gold):** Carga dos dados higienizados no **PostgreSQL**, estruturando as variáveis para o modelo de Machine Learning e para o dashboard.

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
