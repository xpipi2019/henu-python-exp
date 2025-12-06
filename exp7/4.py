"""
4、异常：
下面定义了一个CandleShop类：

class CandleShop:
    name = "Here's a Hot Tip: Buy Drip Candles"

    def __init__(self, stock):
        self.stock = stock

    def buy(self, color):
        self.stock[color] = self.stock[color] - 1

candle_shop = CandleShop({'blue': 6, 'red': 2, 'green': 0})
candle_shop.buy('blue')
1）自定义一个异常类OutOfStack
2）请修改实例buy当购买蜡烛的量超出库存时会抛出OutOfStack异常
3）想办法在主程序中加一个代码会引起程序抛出OutOfStack
4）捕获该异常，并输出异常的具体信息。
"""


class OutOfStack(Exception):
    pass


class CandleShop:
    name = "Here's a Hot Tip: Buy Drip Candles"

    def __init__(self, stock):
        self.stock = stock

    def buy(self, color):
        if self.stock[color] <= 0:
            raise OutOfStack(f"Out of stock: {color}")
        self.stock[color] = self.stock[color] - 1


candle_shop = CandleShop({"blue": 6, "red": 2, "green": 0})
candle_shop.buy("blue")
candle_shop.buy("blue")
candle_shop.buy("blue")
candle_shop.buy("blue")
candle_shop.buy("blue")
candle_shop.buy("blue")
try:
    candle_shop.buy("blue")
except OutOfStack as e:
    print(e)
