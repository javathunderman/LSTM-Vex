import statistics
def read():
    data = []
    with open("dump.csv") as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    content = [x.replace(',', '') for x in content]
    content.pop(0)
    content = [float(i) for i in content]
    with open("result.txt", "a") as r: 
        r.write(str(statistics.median(content)))
#    print(statistics.median(content))
