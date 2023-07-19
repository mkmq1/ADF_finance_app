# Import libraries
import unittest
import finance_calc


# Create class that inherits TestCase class
class Test_finance_calc(unittest.TestCase):
    # Create method to assert calculate_compound_interest produces correct result
    def test_calculate_compound_interest(self):
        # Create assertion using self.assertEqual() method
        self.assertEqual(
            finance_calc.calculate_compound_interest(12, 1000, 5, 15),
            2041.7417464102255,
            "Incorrect amount",
        )


# Call unittest.main() when running script from the command-line
if __name__ == "__main__":
    unittest.main()
