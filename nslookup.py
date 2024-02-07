import csv
import socket
from datetime import datetime

def nslookup(ip_file):
    with open(ip_file, 'r') as f:
        ips = f.readlines()
    
    results = []
    for ip in ips:
        ip = ip.strip()
        try:
            dns_name = socket.gethostbyaddr(ip)[0]
        except socket.herror:
            dns_name = "Unknown"
        results.append((ip, dns_name))
    
    now = datetime.now()
    output_file = f"nslookup_{now.strftime('%Y-%m-%d_%H-%M-%S')}.csv"
    
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['IP Address', 'DNS Name'])
        writer.writerows(results)
    
    print("DNS lookup completed. Results written to", output_file)

if __name__ == "__main__":
    input_file = input("Enter the path to the input file (txt): ")
    nslookup(input_file)
