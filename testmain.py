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


if __name__ == "__main__":
    pytest.main()
