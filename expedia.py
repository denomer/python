import datetime
import urllib
import urllib2
import html5lib
from bs4 import BeautifulSoup
import requests
from datetime import timedelta

encodeStart = (datetime.date.today().strftime("%d/%m/%Y"))
enodeEnd = ((datetime.date.today() + timedelta(days=1)).strftime("%d/%m/%Y"))
checkin = urllib.urlencode({"chkin":encodeStart})
chkout = urllib.urlencode({"chkout":enodeEnd})
getURL = "https://www.expedia.co.in/Delhi-Hotels-Crowne-Plaza-Hotel-New-Delhi-Okhla.h3884851.Hotel-Information?"+checkin+'&'+chkout+"&rm1=a2#rooms-and-rates"
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0','Accept-Language':'en-US,en;q=0.8','Accept-Encoding':'gzip, deflate, sdch','Referer':'http://www.google.com'}
sess = requests.session()
session_response = sess.get(getURL,headers=headers)
html_content = session_response.content
soup = BeautifulSoup(html_content, 'html5lib')
tableData = soup.find_all("div",{"class":"room-price-info-wrapper"})
tdTags = tableData[0].find("span",{"class":"room-price one-night-room-price"})	
one_night_price = tdTags.text.replace("Rs.","").strip()
print one_night_price




			

			