import re
import subprocess

def monitor_ssh_log(log_file, max_failures):
    fail_count = {}
    with open(log_file, 'r') as file:
        for line in file:
            if "Failed password" in line:
                ip = re.search(r'(\d+\.\d+\.\d+\.\d+)', line).group(1)
                fail_count[ip] = fail_count.get(ip, 0) + 1
                if fail_count[ip] >= max_failures:
                    block_ip(ip)
                    print(f"Blocked IP: {ip}")

def block_ip(ip):
    subprocess.call(['iptables', '-A', 'INPUT', '-s', ip, '-j', 'DROP'])

log_file = '/var/log/auth.log'
max_failures = 5
monitor_ssh_log(log_file, max_failures)
