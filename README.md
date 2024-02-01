# Web Scraping and Analysis Project

This project demonstrates a simple web scraping and analysis workflow using Python. The goal is to scrape quotes from a website, store them in an SQLite database, and then perform basic analysis on the collected data.

## Features
* Web Scraping: Scrapes quotes from http://quotes.toscrape.com using the requests and beautifulsoup4 libraries.

* Database Storage: Stores the scraped quotes in an SQLite database (quotes.db) using the sqlite3 library.

* Data Analysis: Performs a simple analysis on the stored quotes, displaying basic statistics using the pandas library.

## Project Structure
scrape_quotes.py: The main script for scraping quotes and storing them in the database.

analyze_quotes.py: Script for analyzing the stored quotes in the database.

## Usage
Clone the repository:

```bash
git clone https://github.com/yourusername/web-scraping-analysis.git
cd web-scraping-analysis
```
Install dependencies:

```bash
pip install -r requirements.txt
```
Run the scraping script:

```bash
python scrape_quotes.py
```
Run the analysis script:

```bash
python analyze_quotes.py
```

## Requirements
Python 3.x
To install the required dependencies, run:

```bash
pip install -r requirements.txt
```


## Contributing
Feel free to contribute to this project by opening issues or submitting pull requests.
