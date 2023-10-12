import re

filename = input("Entrez le nom du fichier : ")
output_filename = input("Entrez le nom du fichier de sortie : ")

def ip_sort_key(ip):
    return tuple(map(int, ip.split('.')))

ip_port_list = []

with open(filename, 'r') as file:
    for line in file:
        if "open port" in line:
            ip = re.search(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', line)
            port = re.search(r'(\d+)/tcp', line)            
            if ip and port:
                ip_port_list.append(f"{ip.group()}:{port.group(1)}")

ip_port_list.sort(key=lambda x: ip_sort_key(x.split(':')[0]))

with open(output_filename, 'w') as out_file:
    for ip_port in ip_port_list:
        out_file.write(ip_port + '\n')
