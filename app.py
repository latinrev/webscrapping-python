import urllib.request
from bs4 import BeautifulSoup
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # this should be done only once 
page = urllib.request.urlopen("https://y7s2057b6d3dt2eur.wordssl.net/");
soup = BeautifulSoup(page,features='lxml');
all_links = soup.find_all('img');
for link in all_links:
    if 'banner_4' in link.get('src') :
        urllib.request.urlretrieve(link.get('src'),'banner.png');
        price = pytesseract.image_to_string('./banner.png')
        print("""////////////////////////////////////////////////////////
                |                                                       |
                |                                                       |
                |                    DOLAR TODAY PRICE                  |
                |                                                       |
                |///////////////////////////////////////////////////////|""")
print(price);
