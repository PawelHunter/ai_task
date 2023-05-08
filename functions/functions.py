import requests
import json
import requests
import openai

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


def load_ex(ex_name):
    url = f"https://zadania.aidevs.pl/token/{ex_name}"
    data_1 = {'apikey': globals()["API_KEY"]}
    headers = {'Content-type': 'application/json'}
    response_token = requests.post(url, data=json.dumps(data_1), headers=headers)
    globals()["token"] = response_token.json()["token"]
    url2 = f'https://zadania.aidevs.pl/task/{globals()["token"]}'
    response = requests.get(url2)
    return response.json()

def found_proper_man(task_messages: dict) -> (str, str):
    for i in task_messages["input"]:
        if i.split()[0] in task_messages["question"]:
            return i , task_messages["question"]


def api_openia_request(question_problem):
    ai_api_key = globals()["AI_API_KEY"]
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {ai_api_key}"
    }
    input_data = {
     "model": "gpt-3.5-turbo",
     "messages": [{"role": "user", "content": question_problem}],
     "temperature": 0.7
   }
    url = f"https://api.openai.com/v1/chat/completions"
    response = requests.post(url, headers=headers, data=json.dumps(input_data))
    if response.status_code == 200:
        result = response.json()
        print("ok")
        return result
    else:
        print("API Error: ", response.text)
        return -1


def send_a_response(answer):
    headers = {'Content-type': 'application/json'}
    url = f'https://zadania.aidevs.pl/answer/{globals()["token"]}'
    data_5 = {"answer": answer}
    response = requests.post(url, data=json.dumps(data_5), headers=headers)

    data = response.json()
    print(data)