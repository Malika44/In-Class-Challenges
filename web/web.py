import requests
from bs4 import BeautifulSoup
import pandas as pd

# Target URL
url = "https://books.toscrape.com/"

# Send HTTP request
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find all book containers
books = soup.find_all('article', class_='product_pod')

# Extract book info
data = []
for book in books:
    title = book.h3.a['title']
    price = book.find('p', class_='price_color').text
    data.append({'Title': title, 'Price': price})

# Save to CSV
df = pd.DataFrame(data)
print(df)
df.to_csv('books_data.csv', index=False)
