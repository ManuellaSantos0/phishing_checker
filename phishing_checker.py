import requests
from bs4 import BeautifulSoup

#Função para checar se a URL existe
def url_existe(url):
    try:
        response = requests.head(url, timeout=5)
        if response.status_code < 400:
            return True
        else:
            return False
    except requests.RequestException:
        return False

#Listas de palavras suspeitas
url_suspeita = ["login", "verify", "secure", "update", "account", "free", "bonus", "premio", "gratuito"]
palavras_suspeitas = ["senha", "cartão", "dados", "confirme", "clique", "alerta", "phishing", "roubo"]

def analisar_url(url):
    risco = 0
    try:
        #Análise preliminar da URL
        for palavra in url_suspeita:
            if palavra in url:
                risco += 1.5  # peso maior para palavras suspeitas na URL

        #Requisição da página
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        html = response.text.lower()
        soup = BeautifulSoup(html, "html.parser")
        texto = soup.get_text()

        #Análise do conteúdo da página
        for palavra in palavras_suspeitas:
            if palavra in texto:
                risco += 1

        #Classificação final do risco
        if risco == 0:
            classificacao = "SEGURO"
        elif risco <= 2:
            classificacao = "BAIXO"
        elif risco <= 4:
            classificacao = "MÉDIO"
        else:
            classificacao = "ALTO"

        print(f"\n🔐 Resultado: O site '{url}' apresenta risco: **{classificacao}**")

    except requests.exceptions.RequestException:
        print(f"\n⚠️ Erro: Não foi possível acessar o site '{url}'. Verifique se ele existe ou se está online.")
    except Exception as e:
        print(f"\n❌ Erro inesperado: {str(e)}")

def main():
    url = input("🔎 Digite a URL que deseja analisar (com http ou https): ").lower()

    if not url_existe(url):
        print(f"⚠️ A URL '{url}' não existe ou não está acessível.")
        return

    analisar_url(url)

if __name__ == "__main__":
    main()