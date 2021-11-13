import json
from urllib.request import urlopen

#url = "https://data.internetstiftelsen.se/bardate_domains.json"
#json_url = urlopen(url)
#data = json.loads(json_url.read())

three_letter_list = []
four_letter_list = []
with open ('bardate_domains.json') as json_file:
    data = json.load(json_file)
    for domain in data['data']:
        if len(domain['name']) < 6:
            three_letter_list.append(domain['name'])
        elif len(domain['name']) < 7:
            four_letter_list.append(domain['name'])

print("three letter list")
for domain in three_letter_list:
    print(domain)

print("four letter list")

for domain in four_letter_list:
    print(domain)
