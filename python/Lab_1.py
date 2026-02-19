import requests

url = 'https://www.google.com'
response = requests.get(url)

print(response.status_code)

if response.status_code == 200:
    print("Content fetched successfully!")
    print(response.text)
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
