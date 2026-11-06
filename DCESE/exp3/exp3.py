import csv

clock = {}
messages = {}
events = []

with open("exp3.csv") as f:
    for r in csv.DictReader(f):
        p = r["process_id"]
        kind = r["event_type"]
        clock.setdefault(p, int(r["initial_clock"]))
        if kind == "RECEIVE":
            sender = r["message_to"]
            clock[p] = max(clock[p], messages[(sender, p)]) + 1
        else:
            clock[p] += 1
        if kind == "SEND":
            messages[(p, r["message_to"])] = clock[p]
        events.append((clock[p], p, r["event_id"]))
        print(r["event_id"], "Clock:", clock[p])

print("Total timestamp order:")
for e in sorted(events):
    print(e)
