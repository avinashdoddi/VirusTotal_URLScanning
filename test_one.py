import requests
url = 'https://www.virustotal.com/vtapi/v2/url/report'
params = {'apikey': '5f522cd287653f78b1378fceb8929a938bcf8012f524e008301cc7fb3ec4a533', 'resource':"http://two"}
response = requests.get(url, params=params)
print(response.json())
