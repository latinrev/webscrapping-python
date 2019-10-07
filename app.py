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
Simple script using Web scrapping to get the price US Dollars in Bolivares Soberanos
# webscrapping-python
Simple script using Web scrapping get the price US Dollars in Bolivares Soberanos
#How does it work?
It uses python library Beautiful Soup 4(Compatible with python 3+) which it uses to get an image from the website.
> An image? But you are displaying text in the console!
Well basically we use another python library called PyTesseract, which uses the OCR called tesseract which we will use to convert the image we downloaded to text and display it as a text
