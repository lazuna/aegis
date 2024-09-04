import time

def monitor_log_file(log_file, keywords):
    with open(log_file, 'r') as file:
        file.seek(0, 2)  # Move to the end of the file
        while True:
            line = file.readline()
            if not line:
                time.sleep(0.1)
                continue
            for keyword in keywords:
                if keyword in line:
                    print(f"Keyword '{keyword}' found: {line.strip()}")

log_file = '/var/log/auth.log'
keywords = ['Failed password', 'authentication failure']
monitor_log_file(log_file, keywords)
