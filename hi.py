import ikea_api
import json
# impr
# Constants like country, language, base url
constants = ikea_api.Constants(country="au", language="en")
# Search API
search = ikea_api.Search(constants)
# Search endpoint with prepared data
endpoint = search.search("Table")


json_dump =ikea_api.run(endpoint)

# i= 0
# for key in json_dump:
#     print(key)
json_str = json.dumps(json_dump, indent=4)
print(json_str)
with open('dump.json','w+') as f:
    f.write(json_str)
    # print()