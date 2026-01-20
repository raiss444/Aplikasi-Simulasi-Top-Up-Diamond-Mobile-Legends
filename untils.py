import csv

def export_to_csv(data, filename="transaksi_ml.csv"):
    if not data:
        return False
    keys = data[0].keys()
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)
    return True
