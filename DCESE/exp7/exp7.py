import csv

with open("exp7.csv") as f:
    data = list(csv.DictReader(f))

nodes = {int(r["node_id"]): r for r in data}
start = int(data[0]["node_id"])
current = start
visited = []

print("Coordinator failed. Election started.")
while current not in visited:
    visited.append(current)
    if nodes[current]["is_active"].upper() == "TRUE":
        print("Token visits:", current)
    else:
        print("Skipping inactive:", current)
    current = int(nodes[current]["next_node_id"])

active = [n for n in visited if nodes[n]["is_active"].upper() == "TRUE"]
if active:
    leader = max(active)
    print("New Coordinator:", leader)
else:
    print("No active nodes")
