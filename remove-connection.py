import json
import urllib.parse

def read_large_json(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield json.loads(line)

for item in read_large_json('all-connections.json'):
    print(urllib.parse.quote(item[0]['name'],safe=''))



