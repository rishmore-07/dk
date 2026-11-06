import csv

def processData(x):
    return x * 2

with open("exp1.csv") as f:
    for r in csv.DictReader(f):
        x = int(r["param_value"])
        method = r["method_name"]
        print("[DISPATCH]", r["client_name"], method)
        if method == "processData":
            print("[SERVER EXECUTION]", x)
            result = processData(x)
            print("[RETURN]", result)
