# import numpy as np
# import pandas as pd
import json
# import requests
import sys
import mysql.connector

#covid_data = requests.get("https://covid19-lake.s3.us-east-2.amazonaws.com/uk_covid/json/2022-12-07.json")
#covid_data_json = json.loads(covid_data.text)
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="covid_db"
)
# mycursor = mydb.cursor()
# sql = "INSERT INTO covid_region_data (areaType,AreaName) VALUES (%s,%s)"
# val = ["test","test"]
# mycursor.execute(sql,val)
# mydb.commit()
# print(mycursor.rowcount, "record inserted.")

data_list = []
for line in sys.stdin:
    json_covid_data = json.loads(line)
    # loading all into memory except northern ireland and whole UK
    if json_covid_data['areaName'] != 'Northern Ireland' and json_covid_data['areaName'] != 'United Kingdom':
        data_list.append(json_covid_data)
# checks for if there are new patients or newCasesBySpecimenDate are over 300
print(len(data_list)) #check
data_list_new_patients = []
for area in data_list:
    if area['areaType'] == 'region':
      if area['newCasesByPublishDate'] > 0 or area['newCasesBySpecimenDate'] > 200:
         data_list_new_patients.append(area)
    elif area['areaType'] == 'nhsRegion':
       if area['newAdmissions'] > 0:
          data_list_new_patients.append(area)
print(len(data_list_new_patients))

insert_list_region = []
insert_list_patients = []
# clean up to be inserted into DB
for data in data_list_new_patients:
    new_region_row = []
    new_patients_row = []
    new_region_row.append(data["areaType"])
    new_region_row.append(data["areaName"])
    new_region_row.append(data["areaCode"])
    new_region_row.append(data["date"])

    if data['areaType'] == 'region':
        new_region_row.append(data["newCasesByPublishDate"])
        new_region_row.append(data["cumCasesByPublishDate"])
        new_region_row.append(len(data["maleCases"]))
        new_region_row.append(len(data["femaleCases"]))
        for m in data['maleCases']:
            new_patients_row.append([data['areaName'],"male", m["age"], m["rate"], m["value"]])
        for f in data['femaleCases']:
            new_patients_row.append([data['areaName'],"female", f["age"], f["rate"], f["value"]])
    elif data['areaType'] == 'nhsRegion':
        new_region_row.append(data["newAdmissions"])
        new_region_row.append(data["cumAdmissions"])
        for p in data['cumAdmissionsByAge']:
            new_patients_row.append([data['areaName'],"N/A", p["age"], p["rate"], p["value"]])
        #print(data['cumAdmissionsByAge'][0]['age'])
    insert_list_region.append(new_region_row)
    insert_list_patients.extend(new_patients_row)

print(insert_list_region)
print(len(insert_list_patients))

mycursor = mydb.cursor()
sql = "INSERT INTO covid_region_data (areaType, AreaName, areaCode, date, newCasesByDate, newCumCasesByDate, cumMaleCases, cumFemaleCases) VALUES (%s, %s, %s, %s, %s, %s,%s,%s)"
mycursor.executemany(sql, insert_list_region)
mydb.commit()
print(mycursor.rowcount, "was inserted.")

# mycursor = mydb.cursor()
# sql = "INSERT INTO patients (regionKey, sex, age, rate, value) VALUES (%s, %s, %s, %f, %f)"
# mycursor.executemany(sql, insert_list_patients)
# mydb.commit()
# print(mycursor.rowcount, "was inserted.")

#for row in data_list_new_patients
    
