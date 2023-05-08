
import requests
import json

def extract_flagged(json_data):
    data = json.loads(json_data)
    flagged_list = []

    for result in data["results"]:
        flagged_list.append(1 if result["flagged"] else 0)

    return flagged_list

def load_data_from_file(file_name ) -> None:
    with open(file_name, 'r') as f:
        _data = json.load(f)
    for key, value in _data.items():
        globals()[key] = value

# Replace 'API_KEY' with your actual API key
# API_KEY = 'API_KEY'
load_data_from_file(r"../data/key.json")


#step1
url = 'https://zadania.aidevs.pl/token/moderation'
data_1 = {'apikey': globals()["API_KEY"]}
headers = {'Content-type': 'application/json'}

response = requests.post(url, data=json.dumps(data_1), headers=headers)

data_2 = response.json()
print(data_2)

#step2
url = f'https://zadania.aidevs.pl/task/{data_2["token"]}'
response = requests.get(url)

data_3 = response.json()
#print(data_3)

#step3

ai_api_key = globals()["AI_API_KEY"]
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {ai_api_key}"
}
data_to_moderate = {
    "input": data_3["input"]
}
url = f"https://api.openai.com/v1/moderations"
response = requests.post(url, headers=headers, data=json.dumps(data_to_moderate))


#step 4
if response.status_code == 200:
    result = response.json()
    json_data = json.dumps(result, indent=4)
    print("ok")
else:
    print("API Error: ", response.text)




data_4 = extract_flagged(json_data)
print(data_4 )

#step 5
headers = {'Content-type': 'application/json'}
url = f'https://zadania.aidevs.pl/answer/{data_2["token"]}'
data_5 = {"answer": data_4}
response = requests.post(url, data=json.dumps(data_5), headers=headers)

data = response.json()
print(data)