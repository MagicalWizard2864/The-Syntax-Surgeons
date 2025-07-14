import requests
import pandas as pd

# Step 1: Get JSON data from the API
url = "https://cryptobubbles.net/backend/data/bubbles1000.usd.json"
response = requests.get(url)
data = response.json()

# Step 2: Convert JSON data to a pandas DataFrame
df = pd.DataFrame(data)

# Step 3: Save the DataFrame to an Excel file
df.to_excel('bubbles_data.xlsx', index=False, sheet_name='Bubbles')

print("Data has been successfully saved to 'bubbles_data.xlsx'")