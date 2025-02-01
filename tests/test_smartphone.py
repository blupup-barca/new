import pytest


def test_smartphone_init(first_smartphone):
    assert first_smartphone.name == "Samsung"
    assert first_smartphone.description == "256GB"
    assert first_smartphone.price == 180000.0
    assert first_smartphone.quantity == 5
    assert first_smartphone.efficiency == 95.5
    assert first_smartphone.model == "S23"
    assert first_smartphone.memory == 256
    assert first_smartphone.color == "Серый"
