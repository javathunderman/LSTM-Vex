import statistics
data = []
with open("dump.csv") as f:
    content = f.readlines()
content = [x.strip() for x in content]
content = [x.replace(',', '') for x in content]
content.pop(0)
content = [float(i) for i in content]

print(statistics.median(content))
