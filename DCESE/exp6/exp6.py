import csv

clocks = [[0, 0, 0] for _ in range(3)]
messages = {}
events = {}

with open("exp6.csv") as f:
    for r in csv.DictReader(f):
        p = int(r["process_id"][1]) - 1
        action = r["event_action"]
        target = r["target_process"]
        if action == "RECEIVE":
            sender = int(target[1]) - 1
            msg = messages.pop((sender, p))
            clocks[p] = [max(a, b) for a, b in zip(clocks[p], msg)]
        clocks[p][p] += 1
        if action == "SEND":
            dest = int(target[1]) - 1
            messages[(p, dest)] = clocks[p].copy()
        events[r["event_id"]] = clocks[p].copy()
        print(r["event_id"], clocks[p])

def before(a, b):
    return all(x <= y for x, y in zip(a, b)) and a != b

ids = list(events)
for i in range(len(ids)):
    for j in range(i + 1, len(ids)):
        a, b = events[ids[i]], events[ids[j]]
        if before(a, b):
            relation = "Causal: first before second"
        elif before(b, a):
            relation = "Causal: second before first"
        else:
            relation = "Concurrent"
        print(ids[i], ids[j], relation)
