import backtrader as bt
import backtrader.feeds as btfeeds
import os


def backtest(algorithm, ticker):
    os.system("cls")
    cerebro = bt.Cerebro()
    cerebro.broker.setcash(10000)
    data = btfeeds.YahooFinanceCSVData(
        dataname="historical/sets/"+ticker+".csv")
    cerebro.adddata(data)
    cerebro.addstrategy(algorithm)
    cerebro.run()
    cerebro.plot()
