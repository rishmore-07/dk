import csv

with open("exp5.csv") as f:
    nodes = list(csv.DictReader(f))

valid = []
for r in nodes:
    print("Polled:", r["node_id"], r["clock_time_sec"])
    if r["is_faulty"].upper() == "TRUE":
        print("Discarded:", r["node_id"])
    else:
        valid.append(r)

if valid:
    avg = sum(int(r["clock_time_sec"]) for r in valid) / len(valid)
    print("Average Time:", avg)
    for r in valid:
        offset = avg - int(r["clock_time_sec"])
        print(r["node_id"], "Adjustment:", offset)
else:
    print("No valid clocks")
