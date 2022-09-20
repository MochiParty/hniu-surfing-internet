from random import random
from traceback import print_tb
import requests
import os
import random

ret = os.system("ping baidu.com -n 1")
code = 200 if ret == 0 else 404
print("Ping code: ",code)

with open(os.getcwd()+"accounts.txt",'r') as f:
  lines = f.readlines()
  while(code != 200):
    num = random.randint(1,len(lines))
    info = lines[num].strip().split()
    data = {
    'DDDDD': info[0],
    'upass': info[1],
    'R1': '0',
    'R2': '',
    'R3': '0',
    'R6': '0',
    'para': '00',
    '0MKKey': '123456',
    'buttonClicked': '',
    'redirect_url': '',
    'err_flag': '',
    'username': '',
    'password': '',
    'user': '',
    'cmd': '',
    'Login': '',
    'v6ip': ''
  }
    response = requests.post('http://10.253.0.1/a70.htm', data=data, verify=False)
    code = response.status_code
    print("successfully login! status code:",response.status_code)
