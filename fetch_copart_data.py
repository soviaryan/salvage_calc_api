import requests
import json  # Add this to format JSON

# Replace with your actual API key
API_KEY = "dc5e18c8fd38c731662c12d0260714f5f77702d5b52042549221c8f172836f85"
LOT_NUMBER = "41344685"  # Replace with a real Copart lot number

url = f"https://copart-iaai-api.com/api/lot/{LOT_NUMBER}"
headers = {"Authorization": f"Bearer {API_KEY}"}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    print(json.dumps(data, indent=4))  # Pretty print JSON output
else:
    print(f"Error: {response.status_code}, {response.text}")
