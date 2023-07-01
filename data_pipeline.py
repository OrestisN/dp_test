import numpy as np
import pandas as pd
import json
import requests
import sys

#covid_data = requests.get("https://covid19-lake.s3.us-east-2.amazonaws.com/uk_covid/json/2022-12-07.json")
#covid_data_json = json.loads(covid_data.text)

# with open ("2022-12-07.json") as handle:
#     json_covid_data = [json.loads(line) for line in handle]
#     # removing northern ireland
#     for dict in json_covid_data:
#         if dict["areaname"] != "Northern Ireland":
#     #print(len(json_covid_data))
#     #print(type(json_covid_data[0]))
data_list = []
for line in sys.stdin:
    json_covid_data = json.loads(line)
    # loading all into memory except nortrhern ireland
    if json_covid_data["areaName"] != "Northern Ireland":
        data_list.append(json_covid_data)
print(len(data_list))

    #print(json_covid_data["areaName"])
