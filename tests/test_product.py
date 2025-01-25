from src.product import Product


def test_product_init(first_product):
    assert first_product.name == "Сыр"
    assert first_product.description == "Сыр с плесенью"
    assert first_product.price == 100.50
    assert first_product.quantity == 3


def product_create():
    product = Product("Samsung", "256GB", 10000.0, 5)
    assert product.name == "Samsung"
    assert product.description == "256GB"
    assert product.price == 10000.0
    assert product.quantity == 5


def test_price_init(capsys, first_product):
    first_product.price = 0.0
    meesage = capsys.readouterr()
    assert meesage.out.strip() == "Цена не должна быть нулевая или отрицательная"

    first_product.price = -1.0
    meesage = capsys.readouterr()
    assert meesage.out.strip() == "Цена не должна быть нулевая или отрицательная"

    first_product.price = 1000.0
    assert first_product.price == 1000.0
