import unittest

class TestSalaryCalculator(unittest.TestCase):
    def test_invalid_number_of_workdays(self):
        # Test case: Invalid number of workdays (negative)
        num_days = -1
        start_times = ["09:00", "17:00"]
        end_times = ["12:00", "20:00"]
        regular_hour_value = 20.0
        overtime_hour_value = 25.0

        # Expected result: ValueError
        with self.assertRaises(ValueError):
            calculate_salary(start_times, end_times, regular_hour_value, overtime_hour_value)

        # Test case: Invalid number of workdays (zero)
        num_days = 0
        start_times = ["09:00", "17:00"]
        end_times = ["12:00", "20:00"]
        regular_hour_value = 20.0
        overtime_hour_value = 25.0

        # Expected result: ValueError
        with self.assertRaises(ValueError):
            calculate_salary(start_times, end_times, regular_hour_value, overtime_hour_value)

        # Test case: Invalid number of workdays (more than expected)
        num_days = 10
        start_times = ["09:00", "17:00"]
        end_times = ["12:00", "20:00"]
        regular_hour_value = 20.0
        overtime_hour_value = 25.0

        # Expected result: ValueError
        with self.assertRaises(ValueError):
            calculate_salary(start_times, end_times, regular_hour_value, overtime_hour_value)

if __name__ == '__main__':
    unittest.main()