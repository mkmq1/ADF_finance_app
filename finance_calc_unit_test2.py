# Import libraries
import unittest
import finance_calc


# Create class that inherits TestCase class
class Test_finance_calc(unittest.TestCase):
    # Create method to assert calculate_required_interest_rate produces first, a result, and second, a correct result
    def test_calculate_required_interest_rate(self):
        # Create assertion using self.assertEqual() method
        self.assertEqual(
            finance_calc.calculate_required_interest_rate(1000, 3000, 5, 15),
            12,
            "Incorrect amount",
        )


# Call unittest.main() when running script from the command-line
if __name__ == "__main__":
    unittest.main()
