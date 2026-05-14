# 📊 EngTech

Projeto de TCC em Engenharia de Dados com abordagem prática (Hands On), focado na construção de uma solução de dados end-to-end para análise de risco empresarial no Brasil.

---

## 🚀 Visão Geral

Este projeto apresenta o desenvolvimento completo de uma solução de dados para responder a um problema real de negócio: **qual a probabilidade de uma empresa encerrar suas atividades nos primeiros 5 anos de vida e o impacto de fatores externos**.

A análise é baseada em variáveis estruturais como:

* CNAE (atividade econômica)
* Capital social
* Região

O projeto integra conceitos de Engenharia de Dados, Análise de Dados e Machine Learning.

---

## 🎯 Tema do Projeto

### Probabilidade de Falência de Empresas nos Primeiros 5 Anos e impactor de fatores externos

---

## 👥 Integrantes

* Davi Araujo - 10731795
* Rafael Cruz - 10732175
* Everton Ribeiro - 10732297
* Felipe Santana - 10732452
* Erickson Silva - 10732435
* Leonardo Gomes - 10731860

---

## 🧠 Contexto de Negócio

A taxa de mortalidade de empresas no Brasil é um fator crítico para o desenvolvimento econômico. Muitos negócios encerram suas atividades nos primeiros anos devido a fatores como gestão, capital insuficiente, características do setor e caracteristicas regionais.

Este projeto busca analisar padrões que expliquem esse fenômeno, utilizando dados estruturados para prever o risco de falência.

---

## ❓ Problema de Negócio

Qual a probabilidade de uma empresa encerrar suas atividades nos primeiros 5 anos, considerando:

* Seu setor de atuação (CNAE)
* Seu capital social inicial
* Região onde a empresa foi aberta

---

## 🎯 Objetivos

* Integrar dados de fontes públicas e/ou empresariais
* Construir um pipeline de dados escalável
* Analisar padrões de sobrevivência empresarial
* Desenvolver um modelo preditivo de risco
* Identificar setores com maior taxa de mortalidade
* Gerar insights estratégicos para tomada de decisão

---

## 🏗️ Arquitetura da Solução

### 🔄 Pipeline de Dados

| Etapa           | Descrição                                 |
| --------------- | ----------------------------------------- |
| Ingestão        | Coleta de dados empresariais              |
| Data Lake (Raw) | Armazenamento de dados brutos             |
| Processamento   | Limpeza e transformação                   |
| Data Warehouse  | Dados estruturados (PostgreSQL)           |
| Modelagem       | Machine Learning (classificação de risco) |
| Visualização    | Dashboards (Power BI / Streamlit)         |

---

## 🧰 Tecnologias Utilizadas

* Python (pandas, numpy, scikit-learn, PyCaret)
* SQL
* PostgreSQL
* Power BI
* Streamlit
* Git & GitHub

---

## 📂 Estrutura do Projeto

```
├── data/
│   ├── raw/
│   ├── processed/
│   └── external/
├── notebooks/
├── src/
├── dashboards/
├── reports/
├── README.md
└── requirements.txt
```

---

## 🔎 Metodologia

1. Coleta de dados empresariais
2. Tratamento e limpeza
3. Análise exploratória (EDA)
4. Engenharia de features (CNAE, capital social, tempo de vida)
5. Modelagem preditiva (classificação)
6. Avaliação de modelos
7. Geração de insights

---

## 📊 Resultados Esperados

* Probabilidade de falência por setor (CNAE)
* Impacto do capital social na sobrevivência
* Identificação de setores de alto risco
* Modelo preditivo de apoio à decisão
