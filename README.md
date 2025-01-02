# **CoinMarketCap Web Scraper**

### **Project Overview**
This project demonstrates web scraping techniques by extracting cryptocurrency data from [CoinMarketCap](https://coinmarketcap.com/). The scraper collects essential information such as cryptocurrency names, symbols, prices, and detailed links. Data is saved in multiple formats: CSV, JSON, and Excel.

This project showcases:
- Efficient data scraping and storage.
- Handling tabular and nested data with Python.
- Saving outputs in widely-used formats.

---

### **Features**
The scraper retrieves:
1. **Cryptocurrency Name**: Name of the cryptocurrency (e.g., Bitcoin, Ethereum).
2. **Symbol**: The ticker symbol (e.g., BTC, ETH).
3. **Price**: Current price in USD.
4. **Details Link**: A link to the cryptocurrency's detailed page on CoinMarketCap.

---

### **Technologies Used**
- **Python Libraries**:
  - `requests`: Fetch HTML content from the website.
  - `BeautifulSoup`: Parse and extract data from HTML.
  - `pandas`: Save data in CSV and Excel formats.
  - `json`: Export data in JSON format.
  - `time`: Adding Delays
  - `random`: Randomizing Delays
---

### **Data Storage**
The scraped data is stored in:
1. **CSV File**: `crypto_trends.csv`
2. **JSON File**: `crypto_trends.json`
3. **Excel File**: `crypto_trends.xlsx`

---
