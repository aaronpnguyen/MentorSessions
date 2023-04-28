import typing

class Product:
    def __init__(self, name: str, quantity: int, price: int) -> None:
        self.name = name
        self.quantity = quantity
        self.price = price

    def get_price(self) -> str:
        return f"${self.price}"

    def update_price(self, increase: bool, percent: int):
        '''
        If increase == true, have the price of the product increase
        Else, decrease in price by a certain percent
        '''
        self.price = self.price
        percent /= 100
        if increase:
            self.price += self.price * percent
        else:
            self.price -= self.price * percent