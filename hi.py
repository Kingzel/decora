import ikea_api

# Constants like country, language, base url
constants = ikea_api.Constants(country="au", language="en")
# Search API
search = ikea_api.Search(constants)
# Search endpoint with prepared data
endpoint = search.search("Billy")


json_dump =ikea_api.run(endpoint)

i= 0
for key in json_dump:
    if i ==0:
        print(key, json_dump[key])
        i+=1

