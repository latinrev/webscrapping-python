import urllib.request
from bs4 import BeautifulSoup

page = urllib.request.urlopen("https://twitter.com/DolarTrue_")
soup = BeautifulSoup(page,features='lxml')
with open ('text.html','w')as fp:
    fp.write(str(soup.encode('utf-8')))
wholePage = open ('text.html','r').read()
startPoint = wholePage.find('Dolar en BsS : ')
endPoint = wholePage.find('.',startPoint)
dolarPrice = wholePage[startPoint:endPoint+3]
print("""
  _____   ____  _               _____    _____  _____  _____ _____ ______ 
 |  __ \ / __ \| |        /\   |  __ \  |  __ \|  __ \|_   _/ ____|  ____|
 | |  | | |  | | |       /  \  | |__) | | |__) | |__) | | || |    | |__   
 | |  | | |  | | |      / /\ \ |  _  /  |  ___/|  _  /  | || |    |  __|  
 | |__| | |__| | |____ / ____ \| | \ \  | |    | | \ \ _| || |____| |____ 
 |_____/ \____/|______/_/    \_\_|  \_\ |_|    |_|  \_\_____\_____|______|
__________________________________________________________________________\n""")
print(dolarPrice)