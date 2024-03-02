import ikea_api
import json
import pandas as pd
# impr
# Constants like country, language, base url
constants = ikea_api.Constants(country="au", language="en")
# Search API
search = ikea_api.Search(constants)
# Search endpoint with prepared data
endpoint = search.search("sofa")


json_dump =ikea_api.run(endpoint)

items = json_dump['searchResultPage']['products']['main']['items']
pure_items = []

for item in items:
    pure_items.append(item['product'])
    # print(item['product'])

# ingka_items = ikea_api.PipItem(constants)
# dvala_e = ingka_items.get_item("29484813")
# dvala = ikea_api.run(dvala_e)
#     print(key)

# print(pure_items)

# print(pure_items[0], pure_items[-1])

keys_to_keep = ["name", "typeName", "mainImageUrl", "pipUrl", "ratingValue", "ratingCount", "salesPrice", "contextualImageUrl"]

# nested_keys = ["numberOfVariants", ]

# new_list_of_dicts = [{key: d['id'] for key in keys_to_keep} for d in pure_items]

merged_dict = {}




for item in pure_items:
    item_id = item['id']
    item_values = {key: item[key] for key in keys_to_keep if key in item}
    merged_dict[item_id] = item_values

# print(new_list_of_dicts[0])
# print(new_list_of_dicts[-1])


# print(merged_dict['70434368'])
print(merged_dict)

df = pd.DataFrame.from_dict(merged_dict, orient='index')



# 
json_str = json.dumps(pure_items, indent=4)

print(df.head)


# items_str = json.dumps(items, indent=3)
# dv = json.dumps(dvala, indent=3)
# print(json_str)

with open('ins.json','w+') as f:
    f.write(json_str)
    # print()