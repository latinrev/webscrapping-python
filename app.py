import urllib.request
from bs4 import BeautifulSoup
import os
import asyncio
import threading
import time

title = """
  _____   ____  _               _____    _____  _____  _____ _____ ______ 
 |  __ \ / __ \| |        /\   |  __ \  |  __ \|  __ \|_   _/ ____|  ____|
 | |  | | |  | | |       /  \  | |__) | | |__) | |__) | | || |    | |__   
 | |  | | |  | | |      / /\ \ |  _  /  |  ___/|  _  /  | || |    |  __|  
 | |__| | |__| | |____ / ____ \| | \ \  | |    | | \ \ _| || |____| |____ 
 |_____/ \____/|______/_/    \_\_|  \_\ |_|    |_|  \_\_____\_____|______|
__________________________________________________________________________\n"""

print(title)
time.sleep(1)
dolarPrice = ''

def getPrice():
      global dolarPrice
      page = urllib.request.urlopen("https://twitter.com/DolarTrue_")
      soup = BeautifulSoup(page,features='lxml')
      wholePage = str(soup.encode('utf-8'))
      startPoint = wholePage.find('Dolar en BsS : ')
      endPoint = wholePage.find('.',startPoint)
      dolarPrice = wholePage[startPoint:endPoint+3]

      

def loading():
  loadingChars = "/—\|" 
  for char in loadingChars:
        print('Loading...' + char)
        time.sleep(0.2)
        os.system('cls')
            
            
t = threading.Thread(target =  getPrice) 

t.start()
while t.is_alive():
  loading()
  
print(title)
print(dolarPrice)