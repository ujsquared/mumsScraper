from lxml import etree as et
from bs4 import BeautifulSoup
import requests
import lxml
stud_id = 323001
final_id = "b" + str(stud_id)
for i in range(0,10):
    cookies = {
        'PHPSESSID': 'o6siie0s8d50s514t92gd2biu1',
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

    data = '------WebKitFormBoundary8C1b1uZrjCPzK8XC\r\nContent-Disposition: form-data; name="PID"\r\n\r\n\r\n------WebKitFormBoundary8C1b1uZrjCPzK8XC\r\nContent-Disposition: form-data; name="POID"\r\n\r\n\r\n------WebKitFormBoundary8C1b1uZrjCPzK8XC\r\nContent-Disposition: form-data; name="SRCHSTR"\r\n\r\n'+str(final_id)+'\r\n------WebKitFormBoundary8C1b1uZrjCPzK8XC--\r\n'

    response = requests.post('https://hib.iiit-bh.ac.in/m-ums-2.0/app.misc/search/stuList.php', cookies=cookies, headers=headers, data=data, verify=False)

    text_response = response.content
    soup = BeautifulSoup(text_response,'html.parser')
    print(soup.prettify())
    print(final_id)
    stud_id+=1
    final_id = "b" + str(stud_id)

