from product import Product
from store import Store

# Products
apple = Product("Apples", 25, 1)
tv = Product("Flat Screen", 5, 5000)

# Stores
best_buy = Store("Best Buy", [apple, tv])

best_buy.update_store_prices(True, 50)
