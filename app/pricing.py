from app.discount import apply_discount

def calculate_price(base_price: float, user_level: str) -> float:
    if base_price < 0:
        raise ValueError("base_price must be non-negative")

    discounted = apply_discount(base_price, user_level)
    return round(discounted, 2)
