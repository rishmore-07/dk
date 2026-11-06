import csv

with open("exp9.csv") as f:
    jobs = list(csv.DictReader(f))

workers = ["W1", "W2", "W3"]
load = {w: 0 for w in workers}

for i, job in enumerate(jobs):
    w = workers[i % len(workers)]
    job["assigned_worker"] = w
    job["status"] = "ASSIGNED"
    load[w] += int(job["compute_units"])
    print(job["job_id"], "assigned to", w)
    print("Current Load:", load)

print("Final Load:", load)
