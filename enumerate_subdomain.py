import requests

def subdomain_enum(domain, wordlist):
    subdomains = []
    with open(wordlist, 'r') as file:
        for line in file:
            subdomain = line.strip() + '.' + domain
            try:
                response = requests.get(f"http://{subdomain}")
                if response.status_code == 200:
                    subdomains.append(subdomain)
            except requests.ConnectionError:
                pass
    return subdomains

domain = 'example.com'
wordlist = 'subdomains.txt'
found_subdomains = subdomain_enum(domain, wordlist)
print(f"Found subdomains: {found_subdomains}")
