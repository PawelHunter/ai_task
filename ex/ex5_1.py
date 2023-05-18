from functions.functions import *
import requests
import json
load_data_from_file(r"data/key.json")

#task
task_name = "blogger"
task_messages = load_ex(task_name)

print(task_messages)
answer = api_openia_request(str(task_messages["blog"]),task_messages["msg"]+" in polish. Maksymalnie po pięć zdań zdania na rodział. Faormat answer as a dict")

answer = answer["choices"][0]["message"]["content"]


answer = api_openia_request(answer,"wypisz wartosci słownika w formie listy")
answer = answer["choices"][0]["message"]["content"]

print(eval(answer))
#step 5
send_a_response(eval(answer))