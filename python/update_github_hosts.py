#! /Users/jinpeng/miniconda3/bin/python
import requests
import os
import re

url = 'https://raw.hellogithub.com/hosts'
response = requests.get(url)

if response.status_code == 200:
    hosts_file_path = '/etc/hosts'

    with open(hosts_file_path, 'r') as f:
        hosts_file_contents = f.readlines()

    start_line = None
    end_line = None

    for i, line in enumerate(hosts_file_contents):
        if line.strip() == '# GitHub520 Host Start':
            start_line = i
        elif line.strip() == '# GitHub520 Host End':
            end_line = i

    if start_line is not None and end_line is not None:
        delimiter = '\n'
        new_lines = re.split(f'(?<={delimiter})', response.text)
        hosts_file_contents[start_line:end_line+1] = new_lines
        with open(hosts_file_path, 'w') as f:
            f.writelines(hosts_file_contents)
        print('Content replaced successfully.')
    else:
        print('Could not find start and end markers in the hosts file.')
else:
    print(f'Error downloading file. Status code: {response.status_code}')

