import os
import requests
import json

f = open('token.txt', 'r')

token = f.read()

auth = " ".join(["Bearer", token])
auth

f.close()

url = 'https://api.youneedabudget.com\\v1\\budgets'
header = {'Authorization':auth}

r = requests.get(url, headers = header)
output = r.json()

import json
with open('output/data.json', 'w') as outfile:
    json.dump(output, outfile)

output = r.json()

budget_id = output["data"]["budgets"][0]["id"]

url_category = os.path.join(url, budget_id, 'categories')
