import requests


request = requests.get('http://www.geoplugin.net/json.gp')
if request.status_code != 200:
    print('Não foi possivel obter a localização')
else:
    print(request.text)
