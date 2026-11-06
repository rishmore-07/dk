import csv
from concurrent.futures import ThreadPoolExecutor

with open("exp10.csv") as f:
    A = []
    for r in csv.DictReader(f):
        A.append([int(r[f"col_{i}"]) for i in range(4)])

B = A

def multiply(row):
    result = []
    for col in zip(*B):
        result.append(sum(x * y for x, y in zip(row, col)))
    print("Worker computed:", result)
    return result

print("MASTER: Scattering rows")
with ThreadPoolExecutor(max_workers=4) as pool:
    C = list(pool.map(multiply, A))

print("MASTER: Gathering results")
for row in C:
    print(row)
