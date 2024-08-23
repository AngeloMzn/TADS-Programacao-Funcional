import json


from functions import functions
from tests import isJsonDataUp, isMainDataUp

with open("thefuck-sample-100.json", encoding='utf-8') as json_data:
    data = json.load(json_data)

#test if json data is up to use
#print(isJsonDataUp.isJsonDataUp(data))

mainData = functions.getMainData(data)

#test mainData
#print(isMainDataUp.isMainDataUp(mainData))

