import datetime
import urllib
import urllib2
import html5lib
from bs4 import BeautifulSoup
import requests
from datetime import timedelta

intialHitUrl = "http://www.goibibo.com/hotels/international-inn-hotel-in-delhi-2354262762760247957"
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0','Accept-Language':'en-US,en;q=0.8','Accept-Encoding':'gzip, deflate, sdch','Referer':'http://www.google.com'}
sess = requests.session()
session_response = sess.get(intialHitUrl,headers=headers)	
html_content = session_response.content
soup = BeautifulSoup(html_content, 'html5lib')
scriptData = soup.find_all("script")
mainData = scriptData[38].text.replace("\n","")
print mainData[81:90]

	
# for d in scriptData:

# 	if ("hotel_city_id" in d):
# 		print d
# tab = scriptTag[0].get("value")
# origin = scriptTag[1].get("value")
# error_url = scriptTag[3].get("value")
# do_availability_check = scriptTag[4].get("value")
# aid = scriptTag[5].get("value")
# dcid = scriptTag[6].get("value")
# label = scriptTag[7].get("value")
# sid = scriptTag[8].get("value")
# no_redirect_check = scriptTag[9].get("value")
# dest_type = scriptTag[10].get("value")
# dest_id = scriptTag[11].get("value")
# highlighted_hotels = scriptTag[12].get("value")


# encodeStart_monthday = (datetime.date.today().strftime("%d").lstrip('0'))
# encodeStart_year_month = (datetime.date.today().strftime("%Y-%m"))
# enodeEnd_monthday = ((datetime.date.today() + timedelta(days=1)).strftime("%d").lstrip('0'))
# enodeEnd_year_month = ((datetime.date.today() + timedelta(days=1)).strftime("%Y-%m"))

# checkin_monthday = urllib.urlencode({"checkin_monthday":encodeStart_monthday})
# checkin_year_month = urllib.urlencode({"checkin_year_month":encodeStart_year_month})
# checkout_monthday = urllib.urlencode({"checkout_monthday":enodeEnd_monthday})
# checkout_year_month = urllib.urlencode({"checkout_year_month":enodeEnd_year_month})


# getURL = "http://www.booking.com/hotel/in/crowne-plaza-new-delhi-okhla.html?"+checkin_monthday+'&'+checkin_year_month+'&'+checkout_monthday+'&'+checkout_year_month+'&'+urllib.urlencode({"tab":tab})+'&'+urllib.urlencode({"origin":origin})+'&'+urllib.urlencode({"error_url":error_url})+'&'+urllib.urlencode({"do_availability_check":do_availability_check})+'&'+urllib.urlencode({"aid":aid})+'&'+urllib.urlencode({"dcid":dcid})+'&'+urllib.urlencode({"label":label})+'&'+urllib.urlencode({"sid":sid})+'&'+urllib.urlencode({"no_redirect_check":no_redirect_check})+'&'+urllib.urlencode({"dest_type":dest_type})+'&'+ urllib.urlencode({"dest_id":dest_id})+'&'+urllib.urlencode({"highlighted_hotels":highlighted_hotels})
# headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0','Accept-Language':'en-US,en;q=0.8','Accept-Encoding':'gzip, deflate, sdch','Referer':'http://www.booking.com/hotel/in/crowne-plaza-new-delhi-okhla.html'}
# sess = requests.session()
# session_response = sess.get(getURL,headers=headers)
# html_content = session_response.content
# soup = BeautifulSoup(html_content, 'html5lib')
# tableData = soup.find_all("strong",{"class":"rooms-table-room-price"})
# price = tableData[0].text.replace("Rs.","").strip()
# print price
