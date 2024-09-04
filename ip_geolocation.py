import requests

def get_ip_geolocation(ip):
    response = requests.get(f"https://ipinfo.io/{ip}/json")
    if response.status_code == 200:
        return response.json()
    return None

ip = '8.8.8.8'
geo_info = get_ip_geolocation(ip)
if geo_info:
    print(f"Geolocation info for {ip}: {geo_info}")
else:
    print("Could not retrieve geolocation information.")
