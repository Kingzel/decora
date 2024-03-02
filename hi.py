import ikea_api
import json
# impr
# Constants like country, language, base url
constants = ikea_api.Constants(country="au", language="en")
# Search API
search = ikea_api.Search(constants)
# Search endpoint with prepared data
endpoint = search.search("bed sheet")


json_dump =ikea_api.run(endpoint)
items = json_dump['searchResultPage']['products']['main']
# i= 0
# for key in json_dump:

ingka_items = ikea_api.PipItem(constants)
dvala_e = ingka_items.get_item("00357293")
dvala = ikea_api.run(dvala_e)
#     print(key)
json_str = json.dumps(json_dump, indent=4)
items_str = json.dumps(items, indent=3)
dv = json.dumps(dvala, indent=3)
# print(json_str)
with open('dvala.json','w+') as f:
    f.write(dv)
    # print()