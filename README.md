# software-license-true-up-calculator

Calculate software licence true-up cost from a CSV: installed minus licensed seats — OVER means seats to buy (difference × unit cost), UNDER means unused seats with the money that could be saved, EXACT when they match — largest true-up cost first.

## How to run

```sh
python3 main.py licences.csv
```

## Example output

```
Office: OVER by 4 seat(s) (14 installed vs 10 licensed) — true-up cost 200.00
CAD: UNDER by 3 seat(s) (7 installed vs 10 licensed) — could save 150.00
Total true-up cost: 200.00
```

Standard library only. Run the tests with `python3 -m unittest discover`.
