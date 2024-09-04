import subprocess

def block_ip(ip):
    subprocess.call(['iptables', '-A', 'INPUT', '-s', ip, '-j', 'DROP'])

def unblock_ip(ip):
    subprocess.call(['iptables', '-D', 'INPUT', '-s', ip, '-j', 'DROP'])

blacklist = ['192.168.1.100', '192.168.1.101']
for ip in blacklist:
    block_ip(ip)
    print(f"Blocked IP: {ip}")
