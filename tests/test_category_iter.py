import pytest


def test_category_iter(category_iterator):
    iter(category_iterator)
    assert category_iterator.index == 0
    assert next(category_iterator).name == "Сыр 1"
    assert next(category_iterator).name == "Сыр 2"

    with pytest.raises(StopIteration):
        next(category_iterator)
