def get_full_path(url='http://google.com/'):
    with open('new_cleaned_data.txt', 'r') as routes:
        urls = [url+line.strip() for line in set(routes)]
        print(len(urls))
    # print(set(map(str.strip, routes)))

import os

# from pathlib import Path
# entries = Path('acribia_test')
# for entry in entries.iterdir():
#     print(entry.name)
from pathlib import Path

