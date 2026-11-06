import csv

with open("exp4.csv") as f:
    for r in csv.DictReader(f):
        t0 = int(r["t0_send_ms"])
        ts = int(r["t_server_ms"])
        t1 = int(r["t1_recv_ms"])
        rtt = t1 - t0
        adjusted = ts + rtt / 2
        offset = adjusted - t1
        print("Client:", r["client_id"])
        print("RTT:", rtt)
        print("Adjusted Time:", adjusted)
        print("Offset:", offset)
