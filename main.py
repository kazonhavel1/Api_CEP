import requests

cepdesejado = input('Digite o Cep desejado: ')

cep = requests.get(f'https://viacep.com.br/ws/{cepdesejado}/json/')
cep = cep.json()

if 'erro' in str(cep):
    print('CEP não encontrado :(')
else:
    print ('CEP:',cep['cep'],'\nLogradouro:',cep['logradouro'],'\nBairro:',cep['bairro'],'\nCidade:',
       cep['localidade'],'\nEstado:',cep['uf'])
    