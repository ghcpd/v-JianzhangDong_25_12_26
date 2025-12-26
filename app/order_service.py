from app.validators import validate_positive_int
from app.pricing import calculate_price
from app.repository import InMemoryRepository

_repo = InMemoryRepository()

def create_order(order_id: str, base_price: float, user_level: str) -> dict:
    validate_positive_int(int(base_price), "base_price")
    final_price = calculate_price(base_price, user_level)

    order = {
        "id": order_id,
        "price": final_price,
        "status": "created",
    }
    _repo.save(order_id, order)
    return order

def get_order(order_id: str) -> dict:
    return _repo.get(order_id)
