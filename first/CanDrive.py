import unittest

# FUNCTION PROVIDED BY THE INSTRUCTIONS
def can_drive(age):
    driving_age = 16
    return age >= driving_age

# TEST CLASS AND CASES
class TestCanDrive(unittest.TestCase):
    def test_age_below_driving_age(self):
        self.assertEqual(can_drive(15), False)

    def test_age_exactly_driving_age(self):
        self.assertEqual(can_drive(16), True)

    def test_age_above_driving_age(self):
        self.assertEqual(can_drive(18), True)

    def test_age_100(self):
        self.assertEqual(can_drive(100), True)

    def test_age_50(self):
        self.assertEqual(can_drive(50), True)

    def test_age_5(self):
        self.assertEqual(can_drive(5), False)
    
    def test_negative_age(self):
        self.assertEqual(can_drive(-1), False)

    def test_zero_age(self):
        self.assertEqual(can_drive(0), False)
