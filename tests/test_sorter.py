import unittest

from package_dispatcher import sort


class TestSortPackages(unittest.TestCase):
    # STANDARD cases
    def test_standard_small_light(self):
        self.assertEqual(sort(10, 10, 10, 5), "STANDARD")

    def test_standard_just_under_bulky_volume(self):
        self.assertEqual(sort(99, 100, 100, 19), "STANDARD")

    def test_standard_just_under_heavy(self):
        self.assertEqual(sort(10, 10, 10, 19.99), "STANDARD")

    # SPECIAL: bulky only
    def test_special_bulky_by_volume(self):
        self.assertEqual(sort(100, 100, 100, 10), "SPECIAL")

    def test_special_bulky_by_single_dimension(self):
        self.assertEqual(sort(150, 10, 10, 5), "SPECIAL")

    def test_special_bulky_height_dimension(self):
        self.assertEqual(sort(10, 150, 10, 5), "SPECIAL")

    def test_special_bulky_length_dimension(self):
        self.assertEqual(sort(10, 10, 150, 5), "SPECIAL")

    # SPECIAL: heavy only
    def test_special_heavy(self):
        self.assertEqual(sort(10, 10, 10, 20), "SPECIAL")

    def test_special_heavy_above_threshold(self):
        self.assertEqual(sort(10, 10, 10, 50), "SPECIAL")

    # REJECTED: bulky AND heavy
    def test_rejected_bulky_volume_and_heavy(self):
        self.assertEqual(sort(100, 100, 100, 20), "REJECTED")

    def test_rejected_bulky_dimension_and_heavy(self):
        self.assertEqual(sort(150, 10, 10, 25), "REJECTED")

    def test_rejected_both_extreme(self):
        self.assertEqual(sort(200, 200, 200, 100), "REJECTED")

    # Edge cases
    def test_exact_volume_threshold(self):
        self.assertEqual(sort(100, 100, 100, 19), "SPECIAL")

    def test_exact_mass_threshold(self):
        self.assertEqual(sort(10, 10, 10, 20), "SPECIAL")

    def test_zero_dimensions(self):
        self.assertEqual(sort(0, 0, 0, 0), "STANDARD")

    def test_very_large_package(self):
        self.assertEqual(sort(1000, 1000, 1000, 1000), "REJECTED")


if __name__ == "__main__":
    unittest.main(verbosity=2)
