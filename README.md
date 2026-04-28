
# EngTech

Projeto final do MBA em Engenharia de Dados, com abordagem prática (Hands On) voltada aos fundamentos de dados e Big Data.

## Sobre o Projeto

Este repositório contém o desenvolvimento do trabalho final do MBA em Engenharia de Dados, com foco na aplicação prática de conceitos fundamentais da área, incluindo processamento de dados em larga escala e construção de pipelines de dados.

# 🎧 MusicMatch Analytics – Plataforma de Recomendação Musical

## 1. Nome do Projeto
**MusicMatch Analytics – Plataforma de Recomendação Musical**

---

## 2. Integrantes

- Davi Araujo - 10731795  
- Rafael Cruz - 10732175  
- Everton Ribeiro - 10732297  
- Felipe Santana - 10732452  
- Erickson Silva - 10732435  
- Leonardo Gomes - 10731860  

---

## 3. Contextualização

Com o crescimento das plataformas de streaming, os usuários consomem uma grande quantidade de músicas diariamente. No entanto, a descoberta de novas músicas alinhadas ao gosto pessoal ainda pode ser limitada.

Este projeto propõe o desenvolvimento de uma plataforma baseada em dados que coleta informações da API do Spotify, organiza esses dados em um banco estruturado e utiliza técnicas de análise e Machine Learning para recomendar músicas similares com base em padrões identificados.

---

## 4. Problema a Ser Resolvido

Como recomendar músicas relevantes para um usuário com base em dados reais, considerando características musicais, artistas e padrões existentes na base?

---

## 5. Objetivo do Projeto

Desenvolver uma solução completa que:

- Coleta dados musicais via API do Spotify  
- Armazena e estrutura esses dados em um banco PostgreSQL  
- Realiza análises exploratórias dos dados  
- Disponibiliza dashboards analíticos no Power BI  
- Permite interação via Streamlit  
- Aplica um modelo de recomendação baseado em similaridade  

---

## 6. Arquitetura da Solução

### Fluxo de Dados


### Descrição

- **Spotify API**: Fonte de dados (artistas, álbuns, músicas)  
- **Python**: Coleta, tratamento e ingestão dos dados  
- **PostgreSQL**: Armazenamento estruturado  
- **Power BI**: Visualização e análise dos dados  
- **Streamlit**: Interface interativa  
- **Machine Learning**: Recomendação de músicas  

---

## 7. Tecnologias Utilizadas

- Python (requests, pandas)  
- API do Spotify  
- PostgreSQL  
- Power BI  
- Streamlit  
- GitHub (controle de versão)  

---

## 8. Estrutura de Dados (Visão Inicial)

Principais entidades:

- Artistas  
- Álbuns  
- Músicas  
- Gêneros  
- Relacionamentos entre músicas/artistas  

---

## 9. Funcionamento do Sistema (Streamlit)

O usuário não digita informações manualmente.

A interface será baseada em **dropdowns (listas suspensas)** alimentados diretamente do banco PostgreSQL.

### O usuário poderá selecionar:

- Artista  
- Música  
- Gênero  
- Filtros adicionais (ex: popularidade, quantidade de recomendações)  

### Resultado:

O sistema retorna uma lista de músicas recomendadas com base em similaridade.

---

## 10. Estratégia de Machine Learning

Será utilizado um modelo de recomendação baseado em similaridade entre itens (**content-based filtering**).

A recomendação será feita considerando atributos como:

- Artista  
- Gênero  
- Popularidade  
- Relações entre músicas  

> Caso disponível via API, poderão ser utilizados atributos adicionais.

---

## 11. Etapas do Projeto

### Etapa 1 – Processamento e Ingestão

- Conexão com API do Spotify  
- Coleta de dados (artistas, álbuns, músicas)  
- Tratamento e normalização dos dados  
- Armazenamento no PostgreSQL  

### Etapa 2 – Análise Exploratória e Limpeza

- Remoção de duplicidades  
- Padronização dos dados  
- Criação de relações entre entidades  
- Desenvolvimento de dashboards no Power BI  

### Etapa 3 – Machine Learning e Aplicação

- Implementação do modelo de recomendação  
- Desenvolvimento da interface no Streamlit  
- Integração com banco de dados  
- Exibição das recomendações  

---

## 12. Análises Esperadas (Power BI)

- Artistas mais populares  
- Distribuição de gêneros  
- Relação entre artistas e músicas  
- Volume de músicas por artista  
- Insights sobre padrões musicais  

---

## 13. Diferencial do Projeto

- Uso de dados reais via API  
- Integração completa (API + Banco + BI + App)  
- Interface interativa com Streamlit  
- Aplicação prática de Machine Learning  
- Arquitetura alinhada com Engenharia de Dados  

---

## 14. Riscos e Mitigações

| Risco                          | Mitigação                              |
|--------------------------------|----------------------------------------|
| Limitações da API do Spotify   | Persistência dos dados no PostgreSQL   |
| Escopo muito amplo             | Foco em recomendação por similaridade  |

---

## 15. Conclusão

O projeto demonstra na prática todo o ciclo de dados:

- Coleta  
- Armazenamento  
- Tratamento  
- Análise  
- Aplicação com Machine Learning  

---
