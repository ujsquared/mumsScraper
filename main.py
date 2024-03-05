from lxml import etree as et
from bs4 import BeautifulSoup
import requests
import lxml
import json
import argparse
parser = argparse.ArgumentParser(description='A script that takes command-line arguments.')

# Define a positional argument
parser.add_argument('-b','--batchYear', type=int, help='Batch year whose data is being scraped')
parser.add_argument('-c','--newCookie', type=str, help='Cookie as an input for every data scrape')
args = parser.parse_args()
newCookie = args.newCookie
batchYear = args.batchYear
def nameGrabber(id):
    cookies = {
        'PHPSESSID': newCookie,
    }

    headers = {
        'Host': 'hib.iiit-bh.ac.in',
        # 'Content-Length': '325',
        'Cache-Control': 'max-age=0',
        'Sec-Ch-Ua': '"Chromium";v="121", "Not A(Brand";v="99"',
        'Sec-Ch-Ua-Mobile': '?0',
        'Sec-Ch-Ua-Platform': '"Linux"',
        'Upgrade-Insecure-Requests': '1',
        'Origin': 'https://hib.iiit-bh.ac.in',
        'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundary8C1b1uZrjCPzK8XC',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.160 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-User': '?1',
        'Sec-Fetch-Dest': 'frame',
        'Referer': 'https://hib.iiit-bh.ac.in/m-ums-2.0/app.misc/search/stuList.php',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'Priority': 'u=0, i',
        'Connection': 'close',
        # 'Cookie': 'PHPSESSID=o6siie0s8d50s514t92gd2biu1',
    }

    data = '------WebKitFormBoundary8C1b1uZrjCPzK8XC\r\nContent-Disposition: form-data; name="PID"\r\n\r\n\r\n------WebKitFormBoundary8C1b1uZrjCPzK8XC\r\nContent-Disposition: form-data; name="POID"\r\n\r\n\r\n------WebKitFormBoundary8C1b1uZrjCPzK8XC\r\nContent-Disposition: form-data; name="SRCHSTR"\r\n\r\n'+id+'\r\n------WebKitFormBoundary8C1b1uZrjCPzK8XC--\r\n'

    response = requests.post('https://hib.iiit-bh.ac.in/m-ums-2.0/app.misc/search/stuList.php', cookies=cookies, headers=headers, data=data, verify=False)

    soup = BeautifulSoup(response.text, 'html.parser')
    target = soup.find('p',{'style':'color:Black;text-decoration: none; white-space: normal;line-height: 1.0em;'})
    if target == None:
        return None
    else:
        return target.text

choice  = 1
noDataFlag = False
count = 0
dict_stud = [["sno","id","name"]]

for i in range(1,6):
    choice  = 1
    noDataFlag = False
    lastFive = int(batchYear)*1000 + 1
    while(choice == 1):
       while(noDataFlag == False):
             idFinal = 'b'+str(i)+str(lastFive)
             print(idFinal)
             nameMacha = nameGrabber(idFinal)    
             if(nameMacha == None):
                print("wtf error thrown catch kro")
                choice  = int(input(" +1 id(1) or +1 branch(0)? or  23 to move out of this  matrix"))
                if choice == 1:
                    lastFive+=1
                else:
                    noDataFlag = True
             else:
               dict_stud.append([count,idFinal,nameMacha])
               lastFive +=1
               count +=1
               print(nameMacha)
fileName = "Batch of '"+str(lastFive)[0:2]
print(fileName)
with open(fileName,"w") as outfile:
    json.dump(dict_stud, outfile)
print("The total student in this batch are - " + str(count))

