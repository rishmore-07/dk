import csv
import threading
import time

lock = threading.Lock()
completed = []

def worker(r):
    print("Started:", r["task_id"])
    time.sleep(int(r["burst_ms"]) / 1000)
    with lock:
        print("Lock acquired:", r["task_id"])
        completed.append(r["task_id"])
        print("Completed:", r["task_id"])
        print("Lock released")

with open("exp2.csv") as f:
    tasks = list(csv.DictReader(f))

threads = []
for r in tasks:
    t = threading.Thread(target=worker, args=(r,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("Final completed tasks:", completed)
