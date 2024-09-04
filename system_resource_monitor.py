import psutil
import time

def log_resource_usage(log_file, interval):
    with open(log_file, 'a') as file:
        while True:
            cpu_usage = psutil.cpu_percent(interval=1)
            memory_info = psutil.virtual_memory()
            log_entry = (f"CPU Usage: {cpu_usage}% | "
                         f"Memory Usage: {memory_info.percent}%\n")
            file.write(log_entry)
            time.sleep(interval)

log_file = 'resource_usage.log'
interval = 60  # Log every 60 seconds
log_resource_usage(log_file, interval)
