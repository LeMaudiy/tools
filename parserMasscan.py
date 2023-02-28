import re

filename = input("Entrez le nom du fichier : ")

with open(filename, 'r') as file:
    for line in file:
        if "open port" in line:
            ip = re.search(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', line).group()
            port = re.search(r'(\d+)/tcp', line).group(1)
            print(f"{ip}:{port}")
