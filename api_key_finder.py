import re
import os

def find_api_keys(directory):
    api_key_patterns = [
        r'AKIA[0-9A-Z]{16}',  # AWS Access Key
        r'AIza[0-9A-Za-z_-]{35}',  # Google API Key
        r'sk_live_[0-9a-zA-Z]{24}'  # Stripe API Key
    ]
    
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(('.py', '.js', '.env')):
                with open(os.path.join(root, file), 'r') as f:
                    content = f.read()
                    for pattern in api_key_patterns:
                        for match in re.findall(pattern, content):
                            print(f"Found API key: {match} in {file}")

directory = 'path/to/codebase'
find_api_keys(directory)
