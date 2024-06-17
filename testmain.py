import pytest
from main import Category, Product

@pytest.fixture
def sample_product():
    return Product("Наушники", 9999, 10)


@pytest.fixture
def sample_category(sample_product):
    return Category("Электроника", "Категория электронных товаров", [sample_product])


def test_total_categories(sample_category):
    assert Category.total_categories == 1


def test_unique_products():
    assert Category.unique_products == 1


def test_category_init(sample_category):
    assert sample_category.title == "Электроника"
    assert sample_category.description == "Категория электронных товаров"
    assert sample_category.products[0] == "Наушники, 9999 руб. Остаток: 10 шт."


def test_product_init(sample_product):
    assert sample_product.name == "Наушники"
    assert sample_product.price == 9999
    assert sample_product.quantity == 10


def test_count_products(sample_category):
    assert len(sample_category.products) == 1


def test_price_setter(sample_product):
    sample_product.price = -1000
    assert sample_product.price == 9999


def test_product_str_method(sample_product):
    """Тестирование строкового представления продукта"""
    expected_str = f"{sample_product.name}, {sample_product.price} руб. Остаток: {sample_product.quantity} шт."
    assert str(sample_product) == expected_str

def test_product_addition(sample_product):
    other_product = Product("Чехол для наушников", 500, 3)
    total_value = sample_product + other_product
    expected_value = (sample_product.price * sample_product.quantity) + (other_product.price * other_product.quantity)
    assert total_value == expected_value, f"Ожидаемое значение: {expected_value}, полученное значение: {total_value}"


if __name__ == "__main__":
    pytest.main()
