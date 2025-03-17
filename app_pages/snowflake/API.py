import requests
import pandas as pd
import json

urlFileType = "FULINS"
feedStartDate = "2024-08-03"
feedEndDate = "2024-08-03"
baseurl = "https://api.data.fca.org.uk/fca_data_firds_files"

urlAPI = f"{baseurl}?q=((file_type:{urlFileType})%20AND%20(publication_date:[{feedStartDate}%20TO%20{feedEndDate}]))&from=0&size=100&pretty=true"
response = requests.get(urlAPI)
data = response.json()

df = pd.DataFrame(data)

#print(df)

print(data["hits"]['total'])
 
lst = []
for i in data["hits"]["hits"]:
    lst.append(i["_source"]["download_link"])

print(lst[1])
print(lst[2])

print(json.dumps(lst[1], indent=4))