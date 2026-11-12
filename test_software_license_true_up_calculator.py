import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import unittest
from main import true_up

def row(software, licensed, installed, unit_cost):
    return {"software": software, "licensed_seats": str(licensed),
            "installed_seats": str(installed), "unit_cost": str(unit_cost)}

class TestTrueUp(unittest.TestCase):
    def test_over_cost(self):
        r = true_up([row("Office", 10, 14, 50.0)])[0]
        self.assertEqual((r[3], r[5], r[6]), (4, 200.0, "OVER"))
    def test_under_saving(self):
        r = true_up([row("Office", 10, 7, 50.0)])[0]
        self.assertEqual((r[3], r[5], r[6]), (-3, 150.0, "UNDER"))
    def test_exact(self):
        r = true_up([row("Office", 10, 10, 50.0)])[0]
        self.assertEqual((r[3], r[5], r[6]), (0, 0.0, "EXACT"))
    def test_largest_true_up_first(self):
        r = true_up([row("A", 10, 11, 10.0), row("B", 10, 20, 10.0)])
        self.assertEqual(r[0][0], "B")
    def test_zero_unit_cost(self):
        r = true_up([row("Free", 1, 5, 0.0)])[0]
        self.assertEqual((r[5], r[6]), (0.0, "OVER"))
    def test_empty_input(self):
        self.assertEqual(true_up([]), [])
