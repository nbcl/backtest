import backtrader as bt


class SmaCross(bt.Strategy):
    def __init__(self):
        sma1 = bt.ind.SMA(period=5)
        sma2 = bt.ind.SMA(period=20)
        self.crossover = bt.ind.CrossOver(sma1, sma2)

    def log(self, txt, dt=None):
        dt = dt or self.datas[0].datetime.date(0)
        print('%s, %s' % (dt.isoformat(), txt))

    def next(self):
        if not self.position:
            if self.crossover > 0:
                self.order = self.order_target_percent(target=1)
                self.log('BUY CREATE, %.2f' % self.datas[0].close[0])

        elif self.crossover < 0:
            self.order = self.order_target_percent(target=0)
            self.log('SELL CREATE, %.2f' % self.datas[0].close[0])
