import sqlite3
import pandas as pd

# Function to analyze quotes from the database
def analyze_quotes():
    conn = sqlite3.connect('quotes.db')
    
    # Query all quotes from the database
    query = 'SELECT * FROM quotes'
    df = pd.read_sql_query(query, conn)

    # Display some basic statistics
    print("Total number of quotes:", len(df))
    print("\nSample quotes:")
    print(df.head())

    # Close connection
    conn.close()

# Main function
def main():
    # Analyze quotes
    analyze_quotes()

if __name__ == "__main__":
    main()
