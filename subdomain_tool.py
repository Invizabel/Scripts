import os
import re
from collections import Counter
import pandas as pd

files = os.listdir("dns")
links = []

for file in files:
    data = pd.read_excel(f"dns/{file}")
    parse = re.findall("\S+\.\S+\.\S+",str(data).lower())
    for _ in parse:
        if not _.endswith(".") and re.search("[a-z]",_.split(".")[0]):
            links.append(_.split(".")[0])

init_links = Counter(links).most_common(20)
new_links = []
for link in init_links:
    new_links.append(link[0])

new_links.sort()

result = "["
for _ in new_links:
    result += f"{_},"

result += "]"
print(result)
