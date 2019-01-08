import urllib.request 
from bs4 import BeautifulSoup
import pandas as pd

webUrl = urllib.request.urlopen('https://www.finviz.com/screener.ashx?v=111&f=earningsdate_thismonth,geo_usa,idx_sp500,sec_technology')
print ("result code: " + str(webUrl.getcode())) 
if (webUrl.getcode() == 200):
    data = webUrl.read()
    # print(data)
    soup = BeautifulSoup(data, 'html.parser')
    # table = soup.find_all('table', id="constituents")
    table_rows = soup.find_all('tr',class_="table-dark-row-cp")
    # table_header = table.find_all('th')
    l = []
    for tr in table_rows:
        td = tr.find_all('td')
        row = [tr.text for tr in td]
        l.append(row)
        # print(row)
    # print(soup.prettify())
    print ('printing list')
    
    print(len(l))
    print(l)
    # print (table_header)
    # print (type(table_header))
    #df = pd.DataFrame(l, columns=["Symbol","Security","SEC filings","GICS Sector","GICS Sub Industry","Headquarters Location","Date first added","CIK","Founded"])
    #print(df['Symbol'])

    
else:
    print ("Received error, cannot parse results")

