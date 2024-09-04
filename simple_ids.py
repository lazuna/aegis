import socket

def intrusion_detection(port, suspicious_patterns):
    with socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP) as sock:
        sock.bind(('', port))
        while True:
            packet, _ = sock.recvfrom(65565)
            for pattern in suspicious_patterns:
                if pattern in packet.decode(errors='ignore'):
                    print(f"Suspicious activity detected: {pattern}")

port = 80
suspicious_patterns = [b'GET /admin', b'SQL Injection']
intrusion_detection(port, suspicious_patterns)
