import csv
import socket
from datetime import datetime

def nslookup(ip_file):
    # Open the file containing IP addresses
    with open(ip_file, 'r') as f:
        # Read all IP addresses into a list
        ips = f.readlines()
    
    results = []
    # Iterate over each IP address
    for ip in ips:
        # Remove leading/trailing whitespaces from the IP address
        ip = ip.strip()
        try:
            # Attempt to perform a reverse DNS lookup to get the DNS name associated with the IP
            dns_name = socket.gethostbyaddr(ip)[0]
        except socket.herror:
            # If reverse DNS lookup fails, mark the DNS name as "Unknown"
            dns_name = "Unknown"
        # Append the IP address and its corresponding DNS name (or "Unknown") to the results list
        results.append((ip, dns_name))
    
    # Get the current date and time
    now = datetime.now()
    # Generate the output file name using the current date and time
    output_file = f"nslookup_{now.strftime('%Y-%m-%d_%H-%M-%S')}.csv"
    
    # Write the results to a CSV file
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        # Write the header row
        writer.writerow(['IP Address', 'DNS Name'])
        # Write the IP addresses and their corresponding DNS names to the CSV file
        writer.writerows(results)
    
    # Print a message indicating that the DNS lookup has completed and specify the output file
    print("DNS lookup completed. Results written to", output_file)

if __name__ == "__main__":
    # Prompt the user to enter the path to the input file containing IP addresses
    input_file = input("Enter the path to the input file (txt): ")
    # Call the nslookup function with the input file path provided by the user
    nslookup(input_file)
