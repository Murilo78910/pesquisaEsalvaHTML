import requests
from bs4 import BeautifulSoup

def salvar_html(url, nome_arquivo):
    # Faz a solicitação HTTP
    resposta = requests.get(url)
    content = resposta.content
    site = BeautifulSoup(content, 'html.parser')
    print(site.prettify())

    # Verifica se a solicitação foi bem-sucedida (código de status 200)
    if resposta.status_code == 200:

        # Obtém o conteúdo HTML da resposta
        html = resposta.text
        
        # Salva o conteúdo HTML em um arquivo
        with open(nome_arquivo + '.txt', 'w', encoding='utf-8') as arquivo:
            arquivo.write(html)
        print(f"HTML salvo em '{nome_arquivo}'")
    else:
        print(f"Erro ao acessar a URL: {resposta.status_code}")

# Solicita a URL ao usuário
url = input("Digite a URL que deseja salvar o HTML: ")

# Solicita o nome do arquivo
nome_arquivo = input("Digite o nome do arquivo para salvar o HTML: ")

# Salva o HTML da página
salvar_html(url, nome_arquivo)

