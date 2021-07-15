import unittest
from city_functions import get_location


class LocationsTestCase(unittest.TestCase):

    def test_city_country(self):
        """Do locations like Canby, Minnesota work?"""
        full_loc = get_location('canby', 'minnesota')
        self.assertEqual(full_loc, 'Canby, Minnesota')


    def test_city_country_population(self):
        """Do locations like Minneapolis, Minnesota, Population: 300,000 work?"""
        full_loc = get_location('santiago', 'chile', '50000000')
        self.assertEqual(full_loc, 'Santiago, Chile, Population: 50000000')


if __name__ == '__main__':
    unittest.main()