#install pandas and xlrd packages before running the script
import pandas as pd
import time
import json
import requests
import openpyxl as op
print("started")
# reading excel sheet
def api_fun(every_item):
    url = 'https://www.virustotal.com/vtapi/v2/url/report'
    params = {'apikey': '5f522cd287653f78b1378fceb8929a938bcf8012f524e008301cc7fb3ec4a533', 'resource':every_item}
    response = requests.get(url, params=params)
    #print(response.json())
    json_output = response.json()
    adding_output_list(json_output,every_item)

def adding_output_list(json_output,every_item):
    if json_output['response_code'] != 0:
        try:
            json_dict = json.dumps(json_output['url'])
            json_dict1 = json.dumps(json_output['positives'])
            json_output_list = [json_dict,json_dict1]
        except blank:
            print ("URL or positives are blank, check the URL onces")
            print(every_item)
            #write error URL's in once excel sheet
        else:
            Actual_list = []
            Actual_list.append(json_output_list)
            write_to_excel_sheet(Actual_list)
        # for each_item in Actual_list:
        #     print(each_item)
def write_to_excel_sheet(Actual_list):
    for each_item in Actual_list:
        ws.append(each_item)
    wb.save('file_test.xlsx')
    wb.close()


df = pd.read_excel("domain_names.xlsx")
wb = op.load_workbook('file_test.xlsx')
ws = wb.get_sheet_by_name('Sheet1')
domain_list = df['id'].tolist()
count = 0

for every_item in domain_list:
    print(every_item)
    api_fun(every_item)
    count = count + 1
    time.sleep(2)
    if count == 4:
        print('count reached to 4 wait for 60 sec')
        count = 0
        time.sleep(60)




#have to send 4 requests at once and need to wait for atleast a minute
#and then has to send another 4 and so on....
#def pull_domains_from_excel_sheet():
    #pass the domains throught VT API and store the result in excelsheet.


#the received output has to store in one excel sheet



#examine the output and keep the nessary col in the excel sheet.
