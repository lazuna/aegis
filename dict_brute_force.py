import requests

def directory_bruteforce(url, wordlist):
    found_directories = []
    with open(wordlist, 'r') as file:
        for line in file:
            directory = line.strip()
            target_url = f"{url}/{directory}"
            response = requests.get(target_url)
            if response.status_code == 200:
                found_directories.append(target_url)
    return found_directories

url = 'http://example.com'
wordlist = 'directories.txt'
found = directory_bruteforce(url, wordlist)
print(f"Found directories: {found}")
