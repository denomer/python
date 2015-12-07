import datetime
import urllib
import urllib2
import html5lib
from bs4 import BeautifulSoup
import requests
from datetime import timedelta

intialHitUrl = "http://www.booking.com/hotel/in/crowne-plaza-new-delhi-okhla.html"
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0','Accept-Language':'en-US,en;q=0.8','Accept-Encoding':'gzip, deflate, sdch','Referer':'http://www.google.com'}
sess = requests.session()
session_response = sess.get(intialHitUrl,headers=headers)
html_content = session_response.content
soup = BeautifulSoup(html_content, 'html5lib')
data = soup.find("div",{"class":"hiddenInputSection"})
tagData = data.find_all("input")

tab = tagData[0].get("value")
origin = tagData[1].get("value")
error_url = tagData[3].get("value")
do_availability_check = tagData[4].get("value")
aid = tagData[5].get("value")
dcid = tagData[6].get("value")
label = tagData[7].get("value")
sid = tagData[8].get("value")
no_redirect_check = tagData[9].get("value")
dest_type = tagData[10].get("value")
dest_id = tagData[11].get("value")
highlighted_hotels = tagData[12].get("value")


encodeStart_monthday = (datetime.date.today().strftime("%d").lstrip('0'))
encodeStart_year_month = (datetime.date.today().strftime("%Y-%m"))
enodeEnd_monthday = ((datetime.date.today() + timedelta(days=1)).strftime("%d").lstrip('0'))
enodeEnd_year_month = ((datetime.date.today() + timedelta(days=1)).strftime("%Y-%m"))

checkin_monthday = urllib.urlencode({"checkin_monthday":encodeStart_monthday})
checkin_year_month = urllib.urlencode({"checkin_year_month":encodeStart_year_month})
checkout_monthday = urllib.urlencode({"checkout_monthday":enodeEnd_monthday})
checkout_year_month = urllib.urlencode({"checkout_year_month":enodeEnd_year_month})


getURL = "http://www.booking.com/hotel/in/crowne-plaza-new-delhi-okhla.html?"+checkin_monthday+'&'+checkin_year_month+'&'+checkout_monthday+'&'+checkout_year_month+'&'+urllib.urlencode({"tab":tab})+'&'+urllib.urlencode({"origin":origin})+'&'+urllib.urlencode({"error_url":error_url})+'&'+urllib.urlencode({"do_availability_check":do_availability_check})+'&'+urllib.urlencode({"aid":aid})+'&'+urllib.urlencode({"dcid":dcid})+'&'+urllib.urlencode({"label":label})+'&'+urllib.urlencode({"sid":sid})+'&'+urllib.urlencode({"no_redirect_check":no_redirect_check})+'&'+urllib.urlencode({"dest_type":dest_type})+'&'+ urllib.urlencode({"dest_id":dest_id})+'&'+urllib.urlencode({"highlighted_hotels":highlighted_hotels})
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0','Accept-Language':'en-US,en;q=0.8','Accept-Encoding':'gzip, deflate, sdch','Referer':'http://www.booking.com/hotel/in/crowne-plaza-new-delhi-okhla.html'}
sess = requests.session()
session_response = sess.get(getURL,headers=headers)
html_content = session_response.content
soup = BeautifulSoup(html_content, 'html5lib')
tableData = soup.find_all("strong",{"class":"rooms-table-room-price"})
price = tableData[0].text.replace("Rs.","").strip()
print price
