from datetime import datetime


class Book:
    def __init__(self, id: int, checkIn: datetime, checkOut: datetime, firstName: str, lastName: str, roomId: int):
        self.id = id
        self.checkIn: datetime = checkIn
        self.checkOut: datetime = checkOut
        self.firstname = firstName
        self.lastName = lastName
        self.roomId = roomId