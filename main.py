class Category:
    """Класс для добавления категории"""
    title: str
    description: str
    products: list

    total_categories = 0  #Общее количество категорий
    unique_products = set()  #Множество для хранения уникальных названий продуктов

    def __init__(self, title, description, products):
        self.title = title
        self.description = description
        self.products = products
        Category.total_categories += 1
        for product in products:
            Category.unique_products.add(product.title)


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

