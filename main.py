"""Calculate software licence true-up cost from installed vs licensed seats.

Usage: python3 main.py licences.csv
CSV columns: software,licensed_seats,installed_seats,unit_cost.
Difference = installed - licensed.
- OVER: more installed than licensed — true-up cost = difference
  x unit cost, and those seats must be bought.
- UNDER: fewer installed than licensed — unused seats, with the
  money that could be saved by dropping them.
- EXACT: installed matches licensed.
Largest true-up cost first, with the total cost to true up.
"""
import argparse, csv, sys

def true_up(rows):
    out = []
    for row in rows:
        licensed = int(row["licensed_seats"])
        installed = int(row["installed_seats"])
        unit_cost = float(row["unit_cost"])
        diff = installed - licensed
        if diff > 0:
            verdict = "OVER"
            cost = round(diff * unit_cost, 2)
        elif diff < 0:
            verdict = "UNDER"
            cost = round(-diff * unit_cost, 2)
        else:
            verdict = "EXACT"
            cost = 0.0
        out.append((row["software"].strip(), licensed, installed, diff,
                    unit_cost, cost, verdict))
    return sorted(out, key=lambda r: (-r[5] if r[6] == "OVER" else 0, r[0]))

def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path")
    args = parser.parse_args(argv)
    with open(args.path, newline="", encoding="utf-8") as f:
        results = true_up(list(csv.DictReader(f)))
    total = 0.0
    for software, licensed, installed, diff, unit_cost, cost, verdict in results:
        if verdict == "OVER":
            total += cost
            print(f"{software}: OVER by {diff} seat(s) ({installed} installed vs {licensed} licensed) — true-up cost {cost:.2f}")
        elif verdict == "UNDER":
            print(f"{software}: UNDER by {-diff} seat(s) ({installed} installed vs {licensed} licensed) — could save {cost:.2f}")
        else:
            print(f"{software}: EXACT ({installed} installed vs {licensed} licensed)")
    print(f"Total true-up cost: {total:.2f}")
    return 0

if __name__ == "__main__":
    sys.exit(main())
