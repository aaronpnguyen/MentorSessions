from typing import List
from product import Product

class Store:
    def __init__(self, name: str, products: List = []) -> None:
        self.name = name
        self.products = products

    def update_store_prices(self, increase: bool, percent: int):
        for product in self.products:
            product: Product
            
            current_price = product.price
            product.update_price(increase, percent)
            print(f"""
                {product.name} was updated to {product.get_price()}
                The old price was {current_price}
            """)