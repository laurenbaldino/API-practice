import requests
import json
from requests.auth import HTTPBasicAuth

auth = HTTPBasicAuth('apikey', '1234')
response = requests.get('https://restcountries.eu/rest/v2/all')
print(response.status_code)
parsed_json = json.loads(response.text)

# parsed_countries = []

# total = 0
# for country in parsed_json:
#     # print(country['area'])
#     if country['area']:
#         total = total + country['area']
#     else:
#         print(country['name'])

# print(total // len(parsed_json))

parsed_countries = {}

## {
## "English": 2,
## "Spanish": 65
## }

for country in parsed_json:
    for language in country['languages']:
        if language['name'] in parsed_countries.keys():
            parsed_countries[language['name']] = parsed_countries[language['name']] + 1
        else:
            parsed_countries[language['name']] = 1
print(str(parsed_countries))






# parsed_countries = []
# for country in parsed_json:
#     # if country['name'][0] == 'A':
#     for currency in country['currencies']:
#         if currency['code'] == 'USD' and country['area'] > 100:
#             parsed_countries.append(country)

# for country in parsed_countries:
#     print(country['name'] + ':' + str(country['currencies']))
# print(parsed_countries)

# response = requests.post('https://restcountries.eu/rest/v2/submit', data=parsed_countries)

