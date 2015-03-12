import requests
 
res = requests.post("http://pwbgis.kcg.gov.tw/construction/construction.aspx?id=63")

print res.text

