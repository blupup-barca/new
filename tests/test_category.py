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
