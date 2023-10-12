import re
import pandas as pd

with open('logs.txt', 'r', encoding='utf-8') as f:
    log_lines = f.readlines()

data = []
ip = None

for line in log_lines:
    ip_match = re.search(r'(\d+\.\d+\.\d+\.\d+)', line)
    state_match = re.search(r'State:\s*([\w\s]+)', line)

    if ip_match:
        ip = ip_match.group(1)
    elif state_match:
        state = state_match.group(1)
        data.append({'IP': ip, 'State': state.strip()})

df = pd.DataFrame(data)
df.to_csv('output.csv', index=False)

