import unittest
from Portfolio import Portfolio
import datetime


class TestPortfolioMethods(unittest.TestCase):
    class DummyStock:
        def __init__(self, dummyPrice):
            self.dummyPrice = dummyPrice

        def price(self, date):
            if date == datetime.datetime(2022, 1, 1):
                return self.dummyPrice
            else:
                return self.dummyPrice + 0.05

    class DummyStock2:
        def price(self, date):
            if date.month == 1:
                return 1
            if date.year == 2015:
                return 1.0589
            elif date.year == 2016:
                return 1.095
            elif date.year == 2017:
                return 1.3366
            elif date.year == 2018:
                return 1.0456
            else:
                return 1.4623

    def testGetProfit(self):
        dummyStocks = [self.DummyStock(0.1)]
        dummyPortfolio = Portfolio(dummyStocks)
        self.assertEqual(
            dummyPortfolio.profit(
                datetime.datetime(2022, 1, 1), datetime.datetime(2022, 3, 1)
            ),
            0.5000000000000001,
        )

    def testGetProfitError(self):
        dummyStocks = [self.DummyStock(0.1)]
        dummyPortfolio = Portfolio(dummyStocks)
        with self.assertRaises(Exception) as context:
            dummyPortfolio.profit(
                datetime.datetime(2022, 1, 1), datetime.datetime(2021, 1, 1)
            )

        self.assertTrue("Invalid Dates" in str(context.exception))

    def testAnnualizedReturn(self):
        dummyStocks = [self.DummyStock2()]
        dummyPortfolio = Portfolio(dummyStocks)
        self.assertEqual(
            dummyPortfolio.annualizedReturn(2015, 2019),
            0.1883230349938072,
        )

    def testAnnualizedError(self):
        dummyStocks = [self.DummyStock(0.1)]
        dummyPortfolio = Portfolio(dummyStocks)
        with self.assertRaises(Exception) as context:
            dummyPortfolio.annualizedReturn(2018, 2017)

        self.assertTrue("Invalid Dates" in str(context.exception))

    def testAnnualizedLimitYear(self):
        dummyStocks = [self.DummyStock(0.1)]
        dummyPortfolio = Portfolio(dummyStocks)
        with self.assertRaises(Exception) as context:
            dummyPortfolio.annualizedReturn(2018, datetime.datetime.now().year)

        self.assertTrue("Invalid Dates" in str(context.exception))


if __name__ == "__main__":
    unittest.main()
