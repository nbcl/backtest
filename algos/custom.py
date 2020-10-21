import backtrader as bt


class CustomAlgoExample(bt.Strategy):
    def __init__(self):
        pass

    def log(self, txt, dt=None):
        dt = dt or self.datas[0].datetime.date(0)
        print('%s, %s' % (dt.isoformat(), txt))

    def next(self):
        self.log('LOG, %.2f' % self.datas[0].close[0])