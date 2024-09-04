import psutil
import time

def log_bandwidth_usage(log_file, interval):
    prev_bytes_sent = psutil.net_io_counters().bytes_sent
    prev_bytes_recv = psutil.net_io_counters().bytes_recv
    with open(log_file, 'a') as file:
        while True:
            time.sleep(interval)
            net_io = psutil.net_io_counters()
            bytes_sent = net_io.bytes_sent
            bytes_recv = net_io.bytes_recv
            sent_speed = (bytes_sent - prev_bytes_sent) / interval
            recv_speed = (bytes_recv - prev_bytes_recv) / interval
            log_entry = (f"Sent Speed: {sent_speed / 1024:.2f} KB/s | "
                         f"Received Speed: {recv_speed / 1024:.2f} KB/s\n")
            file.write(log_entry)
            prev_bytes_sent = bytes_sent
            prev_bytes_recv = bytes_recv

log_file = 'bandwidth_usage.log'
interval = 60  # Log every 60 seconds
log_bandwidth_usage(log_file, interval)
