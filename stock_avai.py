import requests,time,os,random,config
token = config.tokenChannel
username_channel = config.usernameChannel
cwd = os.getcwd()
from bs4 import BeautifulSoup
import logging
logging.getLogger("requests").setLevel(logging.WARNING) 
header = {"accept-encoding": "gzip, deflate",
            "content-type": "text/plain;charset=UTF-8", 
      
            "origin" : "https://www.tokopedia.com",
            "referer": "https://www.tokopedia.com/pinzyofficial/earphone-pinzy-original-d1-series",
            "user-agent": 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
        }
s = requests.Session()
def check(url):
    while True:
        s.headers.update(header)
        r = s.get(url,headers=header)
        
        #print(f"[*] The status code is ", r.status_code)
        soup = BeautifulSoup(r.text, 'html.parser')
        get_data = soup.prettify()
    
        get_datas = get_data.split('totalStockFmt')
        
        get_datass = get_datas[1].split(r'\",\"menu\"')
        
        get_stock = get_datass[0].split(r'\":\"')
        get_stock = get_stock[1]
        title = get_data.split('pdpProductName')
        title = title[1].split(r'</h1>')
        title = title[0].split(r'">')
        title = title[1].strip()
        print(f"[*] [{time.strftime('%d-%m-%y %X')}] {title} | Stock: {get_stock}") 
      
         
        if get_stock.isdigit():
            if get_stock > 0:
                response = requests.post(
                url='https://api.telegram.org/bot{0}/{1}'.format(token, "sendMessage"),
                data={'chat_id': username_channel, 'text': f"[{time.strftime('%d-%m-%y %X')}] {title} | Stock: {get_stock}"}
            ).json()
        
         
def main():
    print("[*] Tokopedia Stock Checker!")
    url = input("[*] Input URL: ")
    s.headers.update(header)
    r = s.get(url,headers=header)
    
    #print(f"[*] The status code is ", r.status_code)
    soup = BeautifulSoup(r.text, 'html.parser')
    get_data = soup.prettify()

    get_datas = get_data.split('totalStockFmt')
    
    get_datass = get_datas[1].split(r'\",\"menu\"')
    
    get_stock = get_datass[0].split(r'\":\"')
    get_stock = get_stock[1]
    title = get_data.split('pdpProductName')
    title = title[1].split(r'</h1>')
    title = title[0].split(r'">')
    title = title[1].strip()
    
    print(f"[*] [{time.strftime('%d-%m-%y %X')}] {title} | Stock: {get_stock}")
    try:
            response = requests.post(
            url='https://api.telegram.org/bot{0}/{1}'.format(token, "sendMessage"),
            data={'chat_id': username_channel, 'text': f"[{time.strftime('%d-%m-%y %X')}] {title} | Stock: {get_stock}"}
        ).json()
    except:
        pass
    try:
        check(url)
    except:
        pass
    
main()
