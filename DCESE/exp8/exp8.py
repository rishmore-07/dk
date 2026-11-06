import csv

with open("exp8.csv") as f:
    nodes = list(csv.DictReader(f))

alive = sorted(int(r["node_id"]) for r in nodes
               if r["is_alive"].upper() == "TRUE")
failed = [r["node_id"] for r in nodes
          if r["is_current_coordinator"].upper() == "TRUE"
          and r["is_alive"].upper() == "FALSE"]

print("Failed Coordinator:", failed)
if alive:
    initiator = alive[0]
    print(initiator, "starts election")
    for n in alive:
        if n > initiator:
            print(initiator, "sends ELECTION to", n)
            print(n, "replies OK")
    leader = max(alive)
    print(leader, "broadcasts COORDINATOR")
else:
    print("No active nodes")
