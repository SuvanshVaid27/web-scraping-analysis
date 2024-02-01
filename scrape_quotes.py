import requests
from bs4 import BeautifulSoup
import sqlite3

# Function to scrape quotes from the website
def scrape_quotes():
    url = 'http://quotes.toscrape.com'
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        quotes = []

        for quote in soup.find_all('span', class_='text'):
            quotes.append(quote.text.strip())

        return quotes
    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
        return []

# Function to store quotes in an SQLite database
def store_quotes_in_database(quotes):
    conn = sqlite3.connect('quotes.db')
    cursor = conn.cursor()

    # Create a table if not exists
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS quotes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            quote TEXT
        )
    ''')

    # Insert quotes into the database
    cursor.executemany('INSERT INTO quotes (quote) VALUES (?)', [(quote,) for quote in quotes])

    # Commit changes and close connection
    conn.commit()
    conn.close()

# Main function
def main():
    # Scrape quotes
    quotes = scrape_quotes()

    if quotes:
        # Store quotes in the database
        store_quotes_in_database(quotes)
        print("Quotes stored in the database.")

if __name__ == "__main__":
    main()
