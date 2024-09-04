import ssl
import socket
from datetime import datetime

def check_ssl_expiry(domain):
    context = ssl.create_default_context()
    with socket.create_connection((domain, 443)) as sock:
        with context.wrap_socket(sock, server_hostname=domain) as ssock:
            cert = ssock.getpeercert()
            expiry_date = datetime.strptime(cert['notAfter'], '%b %d %H:%M:%S %Y %Z')
            return expiry_date

domain = 'example.com'
expiry_date = check_ssl_expiry(domain)
print(f"SSL certificate for {domain} expires on: {expiry_date}")
