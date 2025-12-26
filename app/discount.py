def apply_discount(price: float, user_level: str) -> float:
    if user_level == "vip":
        return price * 0.8
    if user_level == "staff":
        return price * 0.5
    return price
