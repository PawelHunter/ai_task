from functions.functions import *
import requests
import json
load_data_from_file(r"data/key.json")

#task
task_name = "inprompt"
task_messages = load_ex(task_name)

response = found_proper_man(task_messages)

answer = api_openia_request(response[0]+'.'+response[1])

answer = answer["choices"][0]["message"]["content"]

print(answer)

#step 5
send_a_response(answer)
