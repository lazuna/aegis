import socket

def network_sniffer(interface):
    with socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3)) as sock:
        sock.bind((interface, 0))
        while True:
            raw_data, addr = sock.recvfrom(65535)
            print(f"Received packet: {raw_data}")

interface = 'eth0'
network_sniffer(interface)
