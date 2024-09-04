import subprocess
import time

def check_latency(server, interval):
    with open('latency.log', 'a') as file:
        while True:
            result = subprocess.run(['ping', '-c', '1', server], capture_output=True, text=True)
            if result.returncode == 0:
                latency = result.stdout.split('time=')[1].split(' ms')[0]
                file.write(f"{time.ctime()}: Latency to {server} is {latency} ms\n")
            else:
                file.write(f"{time.ctime()}: Failed to ping {server}\n")
            time.sleep(interval)

server = '8.8.8.8'
interval = 60  # Check every 60 seconds
check_latency(server, interval)
