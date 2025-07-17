from bs4 import BeautifulSoup
import requests
import pandas as pd
import yfinance as yf
import plotly.express as px

#Question 1: a) Using the Ticker function enter the ticker symbol of the stock we want to extract data on to create a
#               ticker object. The stock is Tesla and its ticker symbol is TSLA.

#            b) Using the ticker object and the function history extract stock information and save it in a dataframe
#               named tesla_data. Set the period parameter to "max" so we get information for the maximum amount of time.

#            c) Reset the index using the reset_index(inplace=True) function on the tesla_data DataFrame and display the
#               first five rows of the tesla_data dataframe using the head function. Take a screenshot of the results and code
#               from the beginning of Question 1 to the results below.

tsla = yf.Ticker("TSLA")
tesla_data = tsla.history(period="max")
tesla_data.reset_index(inplace=True)
print(tesla_data.head(5))

#Question 2: a) Use the requests library to download the webpage

#            b) Parse the html data using beautiful_soup using parser i.e html5lib or html.parser.

#            c) Using BeautifulSoup or the read_html function extract the table with Tesla Revenue and store it into a
#               dataframe named tesla_revenue. The dataframe should have columns Date and Revenue.

html_data = requests.get(url="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/revenue.htm").text
bs = BeautifulSoup(html_data, "html.parser")
all_rows = bs.find_all("tbody")[1].find_all("tr")

dates = list()
revenue = list()

for row in all_rows:
    values = row.find_all("td")
    dates.append(values[0].text)
    revenue.append(values[1].text)

tesla_revenue = pd.DataFrame(data={"Date": dates, "Revenue": revenue})

tesla_revenue["Revenue"] = tesla_revenue["Revenue"].str.replace(",|\$", "", regex=True)
tesla_revenue.dropna(inplace=True)
tesla_revenue = tesla_revenue[tesla_revenue["Revenue"] != ""]

print(tesla_revenue.tail(5))

#Question 3: a) Using the Ticker function enter the ticker symbol of the stock we want to extract data on to create a
#               ticker object. The stock is GameStop and its ticker symbol is GME.

#            b) Using the ticker object and the function history extract stock information and save it in a dataframe
#               named gme_data. Set the period parameter to "max" so we get information for the maximum amount of time.

#            c) Reset the index using the reset_index(inplace=True) function on the gme_data DataFrame and display the
#               first five rows of the gme_data dataframe using the head function. Take a screenshot of the results and code
#               from the beginning of Question 3 to the results below.

gme = yf.Ticker("GME")
gme_data = gme.history(period="max")
gme_data.reset_index(inplace=True)
print(gme_data.head(5))

#Question 4: a) Use the requests library to download the webpage

#            b) Parse the html data using beautiful_soup using parser i.e html5lib or html.parser.

#            c) Using BeautifulSoup or the read_html function extract the table with GameStop Revenue and store it into
#               a dataframe named gme_revenue. The dataframe should have columns Date and Revenue. Make sure the comma and
#               dollar sign is removed from the Revenue column.

#            d) Display the last five rows of the gme_revenue dataframe using the tail function. Take a screenshot of the results.

html_data_2 = requests.get(url="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/stock.html").text
bs = BeautifulSoup(html_data_2, "html.parser")
all_rows = bs.find_all("tbody")[1].find_all("tr")

dates = list()
revenue = list()

for row in all_rows:
    values = row.find_all("td")
    dates.append(values[0].text)
    revenue.append(values[1].text)

gme_revenue = pd.DataFrame(data={"Date": dates, "Revenue": revenue})

gme_revenue["Revenue"] = gme_revenue["Revenue"].str.replace(",|\$", "", regex=True)
gme_revenue.dropna(inplace=True)
gme_revenue = gme_revenue[gme_revenue["Revenue"] != ""]

print(gme_revenue.tail(5))

#Question 5: Plot Tesla Stock Graph

tesla_revenue["Date"] = pd.to_datetime(tesla_revenue["Date"])
convert_dict_1 = {'Revenue': int}
tesla_revenue = tesla_revenue.astype(convert_dict_1)

fig = px.line(tesla_revenue, x="Date", y="Revenue")
fig.show()

#Question 6: Plot GameStop Stock Graph

gme_revenue["Date"] = pd.to_datetime(gme_revenue["Date"])
convert_dict_2 = {"Revenue": int}
gme_revenue = gme_revenue.astype(convert_dict_2)

fig = px.line(gme_revenue, x="Date", y="Revenue")
fig.show()
