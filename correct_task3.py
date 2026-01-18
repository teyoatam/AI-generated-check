from typing import Iterable, Optional
def average_valid_measurements(values: Optional[Iterable]) -> Optional[float]:
    if values is None:
        return None
    
    total = 0.0
    count = 0
    
    for v in values:
        if v is not None:
            try:
                total += float(v)
                count += 1
            except (TypeError, ValueError):
                pass 
    
    return total / count if count else None