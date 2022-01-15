import requests
from bs4 import BeautifulSoup

url = "https://finance.yahoo.com/quote/GOOGL?p=GOOGL&.tsrc=fin-srch"

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'}

html_page = requests.get(url, headers=headers)

# Create a sub object
soup = BeautifulSoup(html_page.content, 'lxml')

# Header info
header_info = soup.find_all("div", id="quote-header-info")[0]

# Extract the title only using the get_text() method.
stock_title = header_info.find("h1").get_text()

# Extract the current price.
current_price = header_info.find("fin-streamer", class_="Fw(b) Fz(36px) Mb(-4px) D(ib)").get_text()

# Extract the table information
table_info = soup.find_all("div", class_="D(ib) W(1/2) Bxz(bb) Pend(12px) Va(t) ie-7_D(i) smartphone_D(b) smartphone_W(100%) smartphone_Pend(0px) smartphone_BdY smartphone_Bdc($seperatorColor)")[0].find_all("tr")


print(stock_title)
print(current_price)

# Extract the heading and the values using a for loop.
for i in range(0,8):
  heading = table_info[i].find_all("td")[0].get_text()
  value = table_info[i].find_all("td")[1].get_text()

  print(heading + " - " + value)


