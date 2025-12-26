import pytest

from app.discount import apply_discount


def test_apply_discount_vip():
    assert apply_discount(100.0, "vip") == pytest.approx(80.0)


def test_apply_discount_staff():
    assert apply_discount(200.0, "staff") == pytest.approx(100.0)


def test_apply_discount_none():
    assert apply_discount(50.0, "guest") == pytest.approx(50.0)


def test_apply_discount_zero_and_negative():
    assert apply_discount(0.0, "vip") == pytest.approx(0.0)
    assert apply_discount(-10.0, "staff") == pytest.approx(-5.0)
