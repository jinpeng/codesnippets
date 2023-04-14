import re
import pandas as pd
import requests
from bs4 import BeautifulSoup

# Send a GET request to the webpage
url = 'https://www.forbes.com/lists/ai50/'
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'html.parser')

# Find the div tag with class 'table' in the webpage and get all its rows
div = soup.find('div', {'class': 'table-row-group'})
rows = div.find_all('a', {'class': re.compile('table-row')})

# Store headers in a list
headers = []
header_group = soup.find('div', {'class': 'header-group'})
header_list = header_group.find_all('span', {'class': re.compile('header-content-text')})
for header in header_list:
    headers.append(header.text.strip())

# Store each row's data in a list
data = []
for row in rows:
    cols = row.find_all('div', {'class': re.compile('table-cell')})
    cols = [col.text.strip() for col in cols]
    data.append(cols)

# Convert the list to a pandas dataframe
df = pd.DataFrame(data)
df.columns = headers

print(df)

# Export the dataframe to an Excel file
df.to_excel('table_data.xlsx', index=False)
