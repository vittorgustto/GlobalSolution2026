# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
  <a href="https://www.fiap.com.br/">
    <img src="./assets/logo-fiap.png" alt="FIAP - Faculdade de Informática e Administração Paulista" style="border:0; width:40%; height:40%;">
  </a>
</p>

<br>


## Grupo 39

## 👨‍🎓 Integrantes: 
- <a href="https://www.linkedin.com/in/vittor-augusto/">Vitor Augusto Gomes</a>
- <a href="https://www.linkedin.com/in/jo%C3%A3o-vitor-lopes-beiro-59a007248/">João Vitor Lopes Beiro</a>
- <a href="">Lucas Gabriel Alves da Costa</a>

## 👩‍🏫 Professores:
### Tutor(a) 
- <a href="https://www.linkedin.com/in/leonardoorabona/">Leonardo Ruiz Orabona</a>
### Coordenador(a)
- <a href="https://www.linkedin.com/in/profandregodoi/">André Godoi Chiovato</a>


## 📜 Descrição

# 🚀 OrbitaGuard AI

## 🎓 FIAP – Graduação ON em Inteligência Artificial

### 🌎 Global Solution 2026.1

**Tema:** Economia Espacial e Inteligência Artificial

**Projeto:** OrbitaGuard AI – Monitoramento Inteligente de Riscos Ambientais com Dados Orbitais, Visão Computacional e IA Generativa

---

# 🚀 Evolução Acadêmica e Disciplinas Integradas

Este repositório faz parte da trajetória desenvolvida durante a Graduação ON em Inteligência Artificial da FIAP, reunindo conhecimentos adquiridos ao longo do curso em projetos, desafios, Global Solutions e atividades práticas.

Este projeto integra conceitos estudados nas fases anteriore da Graduação ON em Inteligência Artificial:

* Inteligência Artificial
* IA Generativa
* Machine Learning
* Data Analytics
* Sistemas Multiagentes
* Visão Computacional
* Cloud Computing
* IoT e Sistemas Embarcados
* Engenharia de Software
* Computação Aplicada à Economia Espacial

---

# 🎯 Objetivo

Este projeto contribui para:

📌 Aplicação prática de Inteligência Artificial

📌 Integração entre disciplinas

📌 Desenvolvimento de soluções para economia espacial

📌 Aplicação de conceitos de análise de dados em cenários reais

---

# 📚 Sobre o Projeto

O **OrbitaGuard AI** é uma Prova de Conceito (POC) desenvolvida para a Global Solution 2026.1 da FIAP.

A solução demonstra como tecnologias de Inteligência Artificial podem transformar dados espaciais em informações úteis para tomada de decisão na Terra.

Utilizando dados orbitais simulados inspirados em plataformas como NASA EarthData, Sentinel-2 e Copernicus, o sistema realiza:

* Monitoramento ambiental inteligente;
* Cálculo de índices de vegetação (NDVI);
* Classificação automática de riscos;
* Geração de alertas ambientais;
* Explicação automática dos resultados através de IA Generativa;
* Dashboard interativo para visualização dos dados.

---

# 🎯 Problema

Satélites geram diariamente enormes volumes de dados ambientais.

Embora esses dados sejam extremamente valiosos para monitoramento climático, prevenção de desastres e análise territorial, sua interpretação normalmente exige conhecimento técnico especializado.

O OrbitaGuard AI foi criado para reduzir essa barreira, transformando informações complexas em alertas claros, acessíveis e acionáveis.

---

# 💡 Solução Proposta

A plataforma realiza:

1. Coleta de dados orbitais (simulados na POC);
2. Processamento dos indicadores ambientais;
3. Cálculo de score de risco;
4. Classificação automática de alertas;
5. Geração de explicações em linguagem natural;
6. Disponibilização dos resultados em dashboard web interativo.

---

# 📊 Funcionalidades

✅ Processamento de dados ambientais

✅ Cálculo de NDVI

✅ Classificação de risco

✅ IA Generativa para explicação dos alertas

✅ Dashboard interativo

✅ Simulação de integração com sensores ESP32

✅ Estrutura preparada para integração com APIs espaciais reais

---

# 🧠 Tecnologias Utilizadas

## Inteligência Artificial

* Machine Learning
* Classificação de Risco
* IA Generativa
* RAG (Retrieval-Augmented Generation)

## Ciência e Análise de Dados

* Python
* Pandas
* NumPy
* Processamento de Dados

## Visualização

* Streamlit
* Matplotlib

## Economia Espacial

* Conceitos inspirados em:

  * NASA EarthData
  * Sentinel-2
  * Copernicus

## Sistemas Embarcados

* Arquitetura preparada para integração com ESP32

---

# 🏗️ Arquitetura da Solução

```text
                   DADOS ORBITAIS
          (NASA • Sentinel • Copernicus)
                           │
                           ▼
                PIPELINE DE PROCESSAMENTO
                           │
                           ▼
                 CÁLCULO DE NDVI
                           │
                           ▼
                CLASSIFICAÇÃO DE RISCO
                           │
                           ▼
               IA GENERATIVA + RAG
                           │
                           ▼
                  DASHBOARD WEB
                           │
                           ▼
                     USUÁRIO FINAL
```

---

# 🔄 Fluxo da Aplicação

```text
Coleta de Dados
        ↓
Processamento
        ↓
Análise NDVI
        ↓
Score de Risco
        ↓
Classificação
        ↓
Explicação por IA
        ↓
Dashboard
```

---

# 📁 Estrutura do Projeto

```text
GlobalSOlution2026
│
├── assets
│   ├── arquitetura_orbitaguard.png
│   ├── logo-fiap.png
│   └── dashboard_preview.png
│
├── data
│   └── ndvi_dataset.csv
│
├── src
│   ├── app_streamlit.py
│   ├── pipeline_ndvi.py
│   ├── rag_assistant.py
│   └── agents.py
│
├── docs
│   ├── requirements.txt
│   └── OrbitaGuard_AI_GS_2026.pdf
│
│
└── README.md
```

---

# ⚙️ Como Executar

## 1. Clonar o repositório

```bash
git clone URL_DO_REPOSITORIO
```

## 2. Entrar na pasta

```bash
cd repo_orbitaguard_ai
```

## 3. Criar ambiente virtual

```bash
python -m venv .venv
```

## 4. Ativar ambiente

### Windows

```bash
.venv\Scripts\activate
```

### Linux / Mac

```bash
source .venv/bin/activate
```

## 5. Instalar dependências

```bash
pip install -r requirements.txt
```

## 6. Executar processamento

```bash
python src/pipeline_ndvi.py
```

## 7. Executar dashboard

```bash
streamlit run src/app_streamlit.py
```

---

# 🎥 Vídeo Demonstrativo

Link do vídeo:

```text
[LINK_VÍDEO](https://www.youtube.com/watch?v=t_eFFafz8Ks)
```

---

## 📁 Estrutura de pastas

Dentre os arquivos e pastas presentes na raiz do projeto, definem-se:

- <b>.github</b>: Nesta pasta ficarão os arquivos de configuração específicos do GitHub que ajudam a gerenciar e automatizar processos no repositório.

- <b>assets</b>: aqui estão os arquivos relacionados a elementos não-estruturados deste repositório, como imagens.

- <b>config</b>: Posicione aqui arquivos de configuração que são usados para definir parâmetros e ajustes do projeto.

- <b>docs</b>: aqui estão todos os documentos do projeto que as atividades poderão pedir. Na subpasta "other", adicione documentos complementares e menos importantes.

- <b>scripts</b>: Posicione aqui scripts auxiliares para tarefas específicas do seu projeto. Exemplo: deploy, migrações de banco de dados, backups.

- <b>src</b>: Todo o código fonte criado para o desenvolvimento do projeto ao longo das 7 fases.

- <b>README.md</b>: arquivo que serve como guia e explicação geral sobre o projeto (o mesmo que você está lendo agora).



## 📋 Licença

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?
