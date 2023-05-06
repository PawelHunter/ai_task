
import requests
import json

def load_data_from_file(file_name ) -> None:
    with open(file_name, 'r') as f:
        _data = json.load(f)
    for key, value in _data.items():
        globals()[key] = value

# Replace 'API_KEY' with your actual API key
# API_KEY = 'API_KEY'
load_data_from_file(r"..\data\key.json")


#step1
url = 'https://zadania.aidevs.pl/token/helloapi'
data_1 = {'apikey': globals()["API_KEY"]}
headers = {'Content-type': 'application/json'}

response = requests.post(url, data=json.dumps(data_1), headers=headers)

data_2 = response.json()
print(data_2)

#step2
url = f'https://zadania.aidevs.pl/task/{data_2["token"]}'
response = requests.get(url)

data_3 = response.json()
print(data_3)

#step3
url = f'https://zadania.aidevs.pl/answer/{data_2["token"]}'
data_4 = {"answer": data_3["cookie"]}
response = requests.post(url, data=json.dumps(data_4), headers=headers)

data = response.json()
print(data)
