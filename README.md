# phishing_checker
Script em Python que verifica o nível de risco de uma URL com base em palavras suspeitas tanto na URL quanto no conteúdo da página. Ideal para treinar fundamentos de web scraping e lógica aplicada à cibersegurança.

# 🔍 Detector de Risco em URLs

Este é um projeto simples de análise de risco em sites suspeitos. O script verifica se a URL está acessível e avalia palavras suspeitas tanto na URL quanto no conteúdo da página, retornando uma classificação de risco.

## 🚀 Funcionalidades

- Verifica se a URL existe e está online.
- Analisa a URL em busca de termos suspeitos (ex: `login`, `verify`, `secure`).
- Analisa o texto da página para detectar palavras comuns em golpes (ex: `senha`, `confirme`, `phishing`).
- Classifica o risco da página como:
  - **SEGURO**
  - **BAIXO**
  - **MÉDIO**
  - **ALTO**

## 🧠 Como funciona

O script utiliza as bibliotecas `requests` e `BeautifulSoup` para extrair e analisar o conteúdo da página. A pontuação de risco é baseada em:

- Palavras suspeitas na URL (peso maior).
- Palavras no conteúdo da página.
- Classificação automática com base no score total.

