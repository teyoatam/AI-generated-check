from typing import Iterable, Mapping
def calculate_average_order_value(orders: Iterable[Mapping]) -> float:
    if not orders: 
        return 0.0
    
    total = 0.0
    count = 0
    
    for order in orders:
        if not isinstance(order, Mapping):
            continue
        
        status = order.get("status")
        if isinstance(status, str) and status.lower() == "cancelled":
            continue
        
        amount = order.get("amount")
        if amount is None:
            continue
        
        try:
            amount_value = float(amount)
        except (TypeError, ValueError):
            continue
        
        total += amount_value
        count += 1
    
    return total / count if count > 0 else 0.0