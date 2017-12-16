# Practice scraping data using bs4
#
# https://www.dataquest.io/blog/web-scraping-tutorial-python/
#
# Lacey Sanchez


# # Attempt 1
# import bs4
# from urllib.request import urlopen as ureq
# from urllib.request import Request
# from bs4 import BeautifulSoup as soup

# my_url = 'https://www.forever21.com/us/shop/Catalog/Category/f21/sale_dresses'
# req = Request(my_url)
# # Opens up connection and grabs the page
# uclient = ureq(my_url)
# # Loads client into variable
# page_html = uclient.read()
# #Closes the client
# uclient.close()
# # Does HTML parsing
# page_soup = soup(page_html, 'html.parser')
# products = page_soup.find_all('div', {'class': 'pi_container'})
# //*[@id="products"]/div[1]
# //*[@id="products"]/div[2]


# # Attempt 2, test data
# import requests
# import bs4

# page = requests.get("http://dataquestio.github.io/web-scraping-pages/ids_and_classes.html")
# soup = BeautifulSoup(page.content, "html.parser")
# print(soup.prettify()) # HTML content of page, printed nicely


# Attempt 3, real example
import requests
import bs4
import pandas as pd

# page = requests.get("http://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168#.WjJTrhNSy8U")
# soup = BeautifulSoup(page.content, "html.parser")
# seven_day = soup.find(id="seven-day-forecast")
# forecast_items = seven_day.find_all(class_="tombstone-container")
# tonight = forecast_items[0]
# print(tonight.prettify()) # HTML content of page, printed nicely
# periods = [pt.get_text() for pt in seven_day.select(".tombstone-container .period-name")]
# short_descs = [sd.get_text() for sd in seven_day.select(".tombstone-container .short-desc")]
# temps = [t.get_text() for t in seven_day.select(".tombstone-container .temp")]
# descs = [d["title"] for d in seven_day.select(".tombstone-container img")]
# weather = pd.DataFrame({"period": periods, "short_desc": short_descs, "temp": temps, "desc": descs})


# # Attempt 4, attempt 1 data
# import requests
# import bs4

# page = requests.get("https://www.forever21.com/us/shop/Catalog/Category/f21/sale_dresses")
# soup = BeautifulSoup(page.content, "html.parser")
# dresses = soup.find(id="products")
# dress_product = dresses.find_all(class_="div.col_s_9_of_10 fl txl")


# # Attempt 5
# import requests
# import bs4

# page = requests.get("http://www.nasdaq.com/markets/indices/major-indices.aspx")
# soup = BeautifulSoup(page.content, "html.parser")
# market_index = soup.find(id="scr-res-table")


# Attempt 6
tbls_lst = parse_url("http://www.nasdaq.com/markets/indices/major-indices.aspx")
tbl = tbls_lst[3]
tbl = tbl.rename(columns={"Index Value": "index_value", "Name": "name", "Symbol": "symbol", "High": "high", "Low": "low"})
tbl.symbol.replace(to_replace="\n", value="", inplace=True, regex=True)
tbl.high.replace(to_replace=",", value="", inplace=True, regex=True)
tbl.low.replace(to_replace=",", value="", inplace=True, regex=True)
tbl.index_value.replace(to_replace=",", value="", inplace=True, regex=True)
pd.to_numeric(tbl.low)
pd.to_numeric(tbl.high)
pd.to_numeric(tbl.index_value)
tbl.drop("Change Net / %", inplace=True, axis=1)
tbl.high = tbl.high.astype(float)
tbl.low = tbl.low.astype(float)
tbl.index_value = tbl.index_value.astype(float)
tbl["range"] = tbl["high"].sub(tbl["low"], axis=0)


# AUXILLARY FUNCTIONS
def parse_url(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    return [parse_html_table(table) for table in soup.find_all("table")]


def parse_html_table(table):
    n_columns = 0
    n_rows=0
    column_names = []
    # Find number of rows and columns
    # we also find the column titles if we can
    for row in table.find_all('tr'):                
        # Determine the number of rows in the table
        td_tags = row.find_all('td')
        if len(td_tags) > 0:
            n_rows+=1
            if n_columns == 0:
                # Set the number of columns for our table
                n_columns = len(td_tags)                        
        # Handle column names if we find them
        th_tags = row.find_all('th') 
        if len(th_tags) > 0 and len(column_names) == 0:
            for th in th_tags:
                column_names.append(th.get_text())    
    # Safeguard on Column Titles
    if len(column_names) > 0 and len(column_names) != n_columns:
        raise Exception("Column titles do not match the number of columns")    
    columns = column_names if len(column_names) > 0 else range(0,n_columns)
    df = pd.DataFrame(columns = columns, index= range(0,n_rows))
    row_marker = 0
    for row in table.find_all('tr'):
        column_marker = 0
        columns = row.find_all('td')
        for column in columns:
            df.iat[row_marker,column_marker] = column.get_text()
            column_marker += 1
        if len(columns) > 0:
            row_marker += 1                    
    # Convert to float if possible
    for col in df:
        try:
            df[col] = df[col].astype(float)
        except ValueError:
            pass            
    return df



