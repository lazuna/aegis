import socket

def port_scan(host, port_range):
    open_ports = []
    for port in range(*port_range):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            if s.connect_ex((host, port)) == 0:
                open_ports.append(port)
    return open_ports

host = '127.0.0.1'
port_range = (1, 1025)
open_ports = port_scan(host, port_range)
print(f"Open ports on {host}: {open_ports}")
