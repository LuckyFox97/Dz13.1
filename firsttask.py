class Category:
    """Класс для добавления категории"""
    title: str
    description: str
    products: list

    def __init__(self, title, description, products):
        self.title = title
        self.description = description
        self.products = products


class Product:
    """Класс для добавления продукта"""
    title: str
    description: str
    price: int
    quantity_in_stock: int

    def __init__(self, title, description, price, quantity_in_stock):
        self.title = title
        self.description = description
        self.price = price
        self.quantity_in_stock = quantity_in_stock
