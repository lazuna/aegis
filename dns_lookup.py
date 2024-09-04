import dns.resolver

def dns_lookup(domain):
    try:
        result = {}
        result['A'] = [ip.address for ip in dns.resolver.resolve(domain, 'A')]
        result['MX'] = [mx.exchange.to_text() for mx in dns.resolver.resolve(domain, 'MX')]
        result['CNAME'] = [cname.target.to_text() for cname in dns.resolver.resolve(domain, 'CNAME')]
        return result
    except Exception as e:
        return str(e)

domain = 'example.com'
dns_info = dns_lookup(domain)
print(f"DNS info for {domain}: {dns_info}")
