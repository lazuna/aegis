import requests

def analyze_headers(url):
    response = requests.head(url)
    headers = response.headers
    for key, value in headers.items():
        print(f"{key}: {value}")

url = 'http://example.com'
analyze_headers(url)
