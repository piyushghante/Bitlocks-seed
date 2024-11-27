# # import requests
# # from bs4 import BeautifulSoup
# # import pandas as pd

# # # Define the URL of the page to scrape
# # url = 'https://amoy.polygonscan.com/address/0x13A4d9D75cEB75087EA77DA0CEB89d558b2F9091'

# # # Define headers to mimic a real browser request
# # headers = {
# #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
# #     'Accept-Language': 'en-US,en;q=0.9',
# # }

# # # Send a GET request to the URL with headers
# # response = requests.get(url, headers=headers)
# # response.raise_for_status()  # Check if the request was successful

# # # Parse the HTML content of the page
# # soup = BeautifulSoup(response.text, 'html.parser')

# # # Find the transaction table
# # table = soup.find('table', {'class': 'table'})

# # # Extract the header
# # headers = [header.text.strip() for header in table.find_all('th')]

# # # Extract the rows
# # rows = []
# # for row in table.find_all('tr')[1:]:  # Skip the header row
# #     cells = [cell.text.strip() for cell in row.find_all('td')]
# #     if len(cells) < len(headers):
# #         # Pad with empty strings for missing columns
# #         cells.extend([''] * (len(headers) - len(cells)))
# #     elif len(cells) > len(headers):
# #         # Truncate if there are extra columns
# #         cells = cells[:len(headers)]
# #     rows.append(cells)

# # # Create a DataFrame from the extracted data
# # df = pd.DataFrame(rows, columns=headers)

# # # Save the DataFrame to a CSV file
# # csv_file = 'transactions.csv'
# # df.to_csv(csv_file, index=False)

# # print(f'Transaction table has been saved to {csv_file}')


import requests
from bs4 import BeautifulSoup
import pandas as pd
import streamlit as st

def ui_track():

# Define a function to fetch and display transaction data
    def fetch_transactions(address):
        # Define the URL of the page to scrape with the user-provided address
        url = f'https://amoy.polygonscan.com/address/{address}'

        # Define headers to mimic a real browser request
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        # Send a GET request to the URL with headers
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Check if the request was successful

        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the transaction table
        table = soup.find('table', {'class': 'table'})

        if table:
            # Extract the header
            headers = [header.text.strip() if header.text.strip() != '' else f"Column_{i}" 
                    for i, header in enumerate(table.find_all('th'))]

            # Make sure headers are unique by appending indices to duplicate column names
            unique_headers = []
            for i, header in enumerate(headers):
                count = headers[:i].count(header)
                unique_headers.append(f"{header}_{count + 1}" if count > 0 else header)

            # Extract the rows
            rows = []
            for row in table.find_all('tr')[1:]:  # Skip the header row
                cells = [cell.text.strip() for cell in row.find_all('td')]
                if len(cells) < len(unique_headers):
                    # Pad with empty strings for missing columns
                    cells.extend([''] * (len(unique_headers) - len(cells)))
                elif len(cells) > len(unique_headers):
                    # Truncate if there are extra columns
                    cells = cells[:len(unique_headers)]
                rows.append(cells)

            # Create a DataFrame from the extracted data
            df = pd.DataFrame(rows, columns=unique_headers)
            

            return df
        else:
            st.error("No transaction table found on the page.")
            return pd.DataFrame()  # Return an empty DataFrame if no table is found


    # Streamlit UI
    st.title("PolygonScan Transaction ")

    # Input field for address (as a string)
    address = st.text_input("Enter the address (e.g., 0x13A4d9D75cEB75087EA77DA0CEB89d558b2F9091):")

    # Fetch and display transaction data when the user provides an address
    if address:
        st.write(f"Fetching transactions for address: {address}")

        # Fetch the data
        df = fetch_transactions(address)

        # If the DataFrame is not empty, display it
        if not df.empty:
            st.dataframe(df,width=1600, height=300)
        else:
            st.write("No data available for this address.")

