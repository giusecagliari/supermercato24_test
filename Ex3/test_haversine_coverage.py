import unittest
import pprint
from haversine_coverage import haversine_coverage


class TestHaversineCoverage(unittest.TestCase):
    def test_haversine_coverage(self):
        pp = pprint.PrettyPrinter()
        pp.pprint(haversine_coverage())


if __name__ == '__main__':
    unittest.main()
