import ikea_api
import json
# impr
# Constants like country, language, base url
constants = ikea_api.Constants(country="au", language="en")
# Search API
search = ikea_api.Search(constants)
# Search endpoint with prepared data
endpoint = search.search("sofa")


json_dump =ikea_api.run(endpoint)

items = json_dump['searchResultPage']['products']['main']['items']
pure_items =[]

for item in items:
    pure_items.append(item['product'])
    # print(item['product'])

# ingka_items = ikea_api.PipItem(constants)
# dvala_e = ingka_items.get_item("29484813")
# dvala = ikea_api.run(dvala_e)
#     print(key)




json_str = json.dumps(pure_items, indent=4)


# items_str = json.dumps(items, indent=3)
# dv = json.dumps(dvala, indent=3)
# print(json_str)

with open('ins.json','w+') as f:
    f.write(json_str)
    # print()