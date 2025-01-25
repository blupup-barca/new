import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def first_product():
    return Product("Сыр", "Сыр с плесенью", 100.50, 3)


@pytest.fixture
def for_category():
    return Category(
        name="Молочные продукты",
        description="Сыр с плесенью",
        products=[
            Product("Сыр 1", "Сыр с плесенью", 150.50, 5),
            Product("Сыр 2", "Сыр Российский", 100.99, 10),
        ],
    )


@pytest.fixture
def for_category_empty_product():
    return Category(name="Молочные продукты", description="Сыр с плесенью")
