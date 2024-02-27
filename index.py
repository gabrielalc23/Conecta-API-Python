import requests

params = []

def choosePair():
    print('Por favor, escolha a primeira moeda para comparar')
    print('1 - BRL')
    print('2 - USD')
    print('3 - EUR')

    pair = int(input())
    
    if pair == 1: return 'BRL'
    if pair == 2: return 'USD'
    if pair == 3: return 'EUR'
    
    return pair

pair1 = choosePair()
pair2 = choosePair()

params.append(f'{pair1}-{pair2}')

more = int(input('Insira 1 se deseja continuar e qualquer outro numero para sair'))

while more == 1:
    pair1 = choosePair()
    pair2 = choosePair()

    params.append(f'{pair1}-{pair2}')

    more = int(input('Insira 1 se deseja continuar e qualquer outro numero para sair'))

coins = ','.join(params)

response = requests.get(f'https://economia.awesomeapi.com.br/last/{coins}')

responseParseJson = response.json()

for key, value in responseParseJson.items():
    print(key, value)