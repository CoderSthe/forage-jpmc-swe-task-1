import unittest
from client3 import getDataPoint, getRatio


class ClientTest(unittest.TestCase):
    def test_getDataPoint_calculatePrice(self):
        quotes = [
            {
                "top_ask": {"price": 121.2, "size": 36},
                "timestamp": "2019-02-11 22:06:30.572453",
                "top_bid": {"price": 120.48, "size": 109},
                "id": "0.109974697771",
                "stock": "ABC",
            },
            {
                "top_ask": {"price": 121.68, "size": 4},
                "timestamp": "2019-02-11 22:06:30.572453",
                "top_bid": {"price": 117.87, "size": 81},
                "id": "0.109974697771",
                "stock": "DEF",
            },
        ]
        """ ------------ Add the assertion below ------------ """

    def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
        quotes = [
            {
                "top_ask": {"price": 119.2, "size": 36},
                "timestamp": "2019-02-11 22:06:30.572453",
                "top_bid": {"price": 120.48, "size": 109},
                "id": "0.109974697771",
                "stock": "ABC",
            },
            {
                "top_ask": {"price": 121.68, "size": 4},
                "timestamp": "2019-02-11 22:06:30.572453",
                "top_bid": {"price": 117.87, "size": 81},
                "id": "0.109974697771",
                "stock": "DEF",
            },
        ]
        """ ------------ Add the assertion below ------------ """

    """ ------------ Add more unit tests ------------ """

    def test_getRatio_division_by_zero(self):
        self.assertIsNone(getRatio(121.20, 0))
        self.assertIsNone(getRatio(119.68, 0))

    
    def test_getRatio_division_by_non_zero_number(self):
        self.assertEqual(getRatio(120.00, 60.00), 2.0)
        self.assertEqual(getRatio(90.00, 60.00), 1.5)
        self.assertEqual(getRatio(100.00,100.00), 1.0)


if __name__ == "__main__":
    unittest.main()
