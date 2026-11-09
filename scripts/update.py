"""Uppdaterar sweden-zipcode.csv från PostNords sammanställning av postnummerändringar.

    python scripts/update.py < andringar.txt
"""
import csv
import re
import sys
from pathlib import Path

CSV = Path(__file__).resolve().parent.parent / "sweden-zipcode.csv"
# Nuvarande postnr, Behålls/Stängs, postort, nytt postnr, Nytt/Befintligt, ny postort, Ny/Befintlig
ROW = re.compile(r"(\d{5})\*?\s*(Behålls|Stängs)\s+.+?\s+(\d{5})\s*(?:Nytt|Bef\w*)\s+(.+?)\s+(?:Ny|Bef\w*)(?:\s|$)", re.I)

with open(CSV, encoding="utf-8", newline="") as f:
    zips = {r["Zip"]: r["City"] for r in csv.DictReader(f)}

sys.stdin.reconfigure(encoding="utf-8")
rows, closed, new = 0, set(), {}
for line in sys.stdin:
    if m := ROW.match(line.strip()):
        old, status, zip, city = m.groups()
        rows += 1
        new[zip] = city.upper()
        if status.lower() == "stängs":
            closed.add(old)

for z in closed - new.keys():
    zips.pop(z, None)
zips.update(new)

with open(CSV, "w", encoding="utf-8", newline="") as f:
    w = csv.writer(f, lineterminator="\n")
    w.writerow(["Zip", "City"])
    w.writerows(sorted(zips.items()))

print(f"{rows} rader, {len(zips)} postnummer")
