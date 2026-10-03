import urllib.request
import re

def get_ids(query, count):
    url = f'https://unsplash.com/s/photos/{query}'
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
        html = urllib.request.urlopen(req).read().decode('utf-8')
        # Unsplash photo IDs are usually 11 characters
        ids = re.findall(r'\"id\":\"([a-zA-Z0-9\-_]{11})\"', html)
        unique_ids = list(dict.fromkeys(ids))
        return unique_ids[:count]
    except Exception as e:
        return []

print('fashion:', get_ids('fashion', 10))
print('sewing:', get_ids('sewing', 10))
print('textiles:', get_ids('textiles', 10))
