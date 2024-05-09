from typing import Any


class Room:
    def __init__(self, floor: int, beds: int, guestNum: int, price, id=None) -> None:
        self.id = id
        self.floor = floor
        self.beds = beds
        self.guestNum = guestNum
        self.price = price

    def __getitem__(self, item: str) -> Any:
        return getattr(self, item)
