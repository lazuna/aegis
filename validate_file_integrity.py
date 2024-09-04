import hashlib

def calculate_hash(file_path):
    hasher = hashlib.sha256()
    with open(file_path, 'rb') as file:
        buf = file.read()
        hasher.update(buf)
    return hasher.hexdigest()

def check_file_integrity(file_path, stored_hash):
    current_hash = calculate_hash(file_path)
    if current_hash == stored_hash:
        print(f"File {file_path} is intact.")
    else:
        print(f"File {file_path} has been modified!")

file_path = 'important_file.txt'
stored_hash = 'previously_stored_hash_value'
check_file_integrity(file_path, stored_hash)
