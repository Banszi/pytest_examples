from typing import List


class ShoppingCart:

    def __init__(self, max_items: int) -> None:
        self.items: List[str] = []
        self.max_items: int = max_items
        self.total_price: float = 0

    def add(self, item: str) -> None:
        if self.size() == self.max_items:
            raise OverflowError('Can NOT add next item into cart! Maximum number has been achieved!')
        self.items.append(item)

    def size(self) -> int:
        return len(self.items)

    def get_items(self) -> List[str]:
        return self.items

    def get_total_price(self, price_map) -> float:
        for product in self.items:
            self.total_price += price_map.get(product)
        return self.total_price

