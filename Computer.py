class Computer:
    def __init__(self, price):
        self.__max_price = price

    def sell(self):
        print(f"Selling price: {self.__max_price}")

    def set_max_price(self, price):
        self.__max_price = price

obj = Computer(1000)
obj.sell()
obj.set_max_price(1200)
obj.sell()
