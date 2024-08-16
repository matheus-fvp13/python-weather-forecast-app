import json
# import pprint
import requests

request = requests.get('http://www.geoplugin.net/json.gp')

if request.status_code != 200:
    print('Não foi possivel obter a localização')
else:
    location = json.loads(request.text)
    latitude = location['geoplugin_latitude']
    longitude = location['geoplugin_longitude']
