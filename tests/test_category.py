from src.product import Product


def test_category_init(for_category):
    assert for_category.name == "Молочные продукты"
    assert for_category.description == "Сыр с плесенью"
    assert for_category.count_of_categories == 1
    assert for_category.count_of_products == 2


def test_category_empty_products(for_category_empty_product):
    assert for_category_empty_product.count_of_products == 2
    assert for_category_empty_product.count_of_categories == 2


def test_products_property(for_category):
    assert (
        for_category.products
        == "Сыр 1, 150.5 руб. Остаток: 5 шт.\nСыр 2, 100.99 руб. Остаток: 10 шт.\n"
    )


def test_str_category(for_category):
    assert str(for_category) == "Молочные продукты, количество продуктов: 15 шт."


def test_middle_price(for_category, category_empty_product):
    assert for_category.middle_price() == 125.745
    assert category_empty_product.middle_price() == 0


def test_my_exception(capsys, for_category):
    assert len(for_category.products_list) == 2

    product_add = Product("Сыр 3", "Сыр с плесенью", 150.50, 5)
    for_category.add_product(product_add)
    message = capsys.readouterr()
    assert message.out.strip().split("\n")[-2] == "Товар добавлен успешно"
    assert (
        message.out.strip().split("\n")[-1] == "Обработка добавления товара завершена"
    )
