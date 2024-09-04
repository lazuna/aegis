import hashlib

def crack_hash(hash_to_crack, dict_file):
    with open(dict_file, 'r') as file:
        for line in file:
            word = line.strip()
            if hashlib.md5(word.encode()).hexdigest() == hash_to_crack:
                return word
    return None

hash_to_crack = '5f4dcc3b5aa765d61d8327deb882cf99'  # Example: 'password'
dict_file = 'passwords.txt'
result = crack_hash(hash_to_crack, dict_file)
if result:
    print(f"Password found: {result}")
else:
    print("Password not found.")
