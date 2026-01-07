import pytest
from app.discount import apply_discount


def test_apply_discount_vip():
    assert apply_discount(100.0, "vip") == 80.0


def test_apply_discount_staff():
    assert apply_discount(100.0, "staff") == 50.0


def test_apply_discount_regular():
    assert apply_discount(100.0, "regular") == 100.0