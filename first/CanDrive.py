import unittest

# FUNCTION PROVIDED BY THE INSTRUCTIONS
def can_drive(age):
    driving_age = 16
    return age >= driving_age

# TEST CLASS AND CASES
class TestCanDrive(unittest.TestCase):
    def test_age_below_driving_age(self):
        self.assertEqual(can_drive(15), False, "Age 15 should not be allowed to drive.")

    def test_age_exactly_driving_age(self):
        self.assertEqual(can_drive(16), True, "Age 16 should be allowed to drive.")

    def test_age_above_driving_age(self):
        self.assertEqual(can_drive(18), True, "Age 18 should be allowed to drive.")

    def test_age_100(self):
        self.assertEqual(can_drive(100), True, "Age 100 should be allowed to drive.")

    def test_age_50(self):
        self.assertEqual(can_drive(50), True, "Age 50 should be allowed to drive.")

    def test_age_5(self):
        self.assertEqual(can_drive(5), False, "Age 5 should not be allowed to drive.")

    def test_negative_age(self):
        self.assertEqual(can_drive(-1), False, "Negative ages should not be allowed to drive.")

    def test_zero_age(self):
        self.assertEqual(can_drive(0), False, "Age 0 should not be allowed to drive.")
