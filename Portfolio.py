import datetime


class Portfolio:
    def __init__(self, stocks):
        self.stocks = stocks

    def profit(self, startDate, endDate):
        if startDate > endDate:
            raise Exception("Invalid Dates")
        initialValue = 0.0
        finalValue = 0.0
        for stock in self.stocks:
            finalValue += stock.price(endDate)
            initialValue += stock.price(startDate)
        return (finalValue - initialValue) / float(initialValue)

    def annualizedReturn(self, startYear, endYear):
        if endYear - startYear < 0 or endYear >= datetime.datetime.now().year:
            raise Exception("Invalid Dates")
        years = (endYear - startYear) + 1
        accumulateProfit = 1
        for i in range(years):
            startDate = datetime.datetime(startYear + i, 1, 1)
            endDate = datetime.datetime(startYear + i, 12, 31)
            accumulateProfit *= 1 + self.profit(startDate, endDate)
        return (accumulateProfit ** (1 / float(years))) - 1
