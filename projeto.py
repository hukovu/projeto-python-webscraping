from urllib import request
from bs4 import BeautifulSoup

url = 'https://www.kabum.com.br/espaco-gamer/cadeiras-gamer'

response = request.get('https://www.kabum.com.br/espaco-gamer/cadeiras-gamer')

if response.status_code == 200:

    soup = BeautifulSoup(response.text, 'html parser')
    cadeiras = soup.find_all('div', class_='classe da cadeira')

    for cadeiras in cadeiras:
        nome_cadeira = cadeira.find ('h2').text
        preco_cadeira = cadeira.find('span', class_='preco').text
        print(f'Nome: {nome_cadeira}, Preço: {preco_cadeira}')

else:
    print(f'A solicitação falhou com o código de status {response.status_code}')
    