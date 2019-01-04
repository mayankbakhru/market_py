import urllib.request 
from bs4 import BeautifulSoup
import pandas as pd

webUrl = urllib.request.urlopen('https://en.m.wikipedia.org/wiki/List_of_S%26P_500_companies')
print ("result code: " + str(webUrl.getcode())) 
if (webUrl.getcode() == 200):
    data = webUrl.read()
    # print(data)
    soup = BeautifulSoup(data, 'html.parser')
    table = soup.find('table', id="constituents")
    table_rows = table.find_all('tr')
    table_header = table.find_all('th')
    l = []
    for tr in table_rows:
        td = tr.find_all('td')
        row = [tr.text for tr in td]
        l.append(row)
        # print(row)
    # print(soup.prettify())
    print ('printing list')
    
    # print(len(l))
    # print (table_header)
    # print (type(table_header))
    df = pd.DataFrame(l, columns=["Symbol","Security","SEC filings","GICS Sector","GICS Sub Industry","Headquarters Location","Date first added","CIK","Founded"])
    print(df['Symbol'])
    
else:
    print ("Received error, cannot parse results")

