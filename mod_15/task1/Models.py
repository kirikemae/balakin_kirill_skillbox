import sqlite3
from Room_info import Room
from task1 import Room_info, Booking


def init_db() -> None:
    with sqlite3.connect("hotel.db") as conn:
        cursor: sqlite3.Cursor = conn.cursor()
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS table_room (
                id INTEGER PRIMARY KEY AUTOINCREMENT, 
                floor INTEGER, 
                beds INTEGER,
                guestNum INTEGER,
                price INTEGER);""")
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS table_booking (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                checkIn DATETIME,
                checkOut DATETIME,
                firstName VARCHAR(255),
                lastName VARCHAR(255),
                roomId INTEGER,
                FOREIGN KEY (roomId) REFERENCES table_room(id))""")


def insert_room_to_bd(room: Room_info):
    try:
        with sqlite3.connect('hotel.db') as conn:
            cursor: sqlite3.Cursor = conn.cursor()
            cursor.execute(
                """INSERT INTO table_room (floor, beds, guestNum, price) 
                VALUES (?, ?, ?, ?)""",
                (room.floor, room.beds, room.guestNum, room.price))
    except sqlite3.Error as e:
        print("An error occurred while inserting room:", e)


def get_rooms(checkIn: str = None, checkOut: str = None):
    with sqlite3.connect('hotel.db') as conn:
        cursor = conn.cursor()
        if checkIn and checkOut:
            cursor.execute("""
                SELECT * FROM table_room
                WHERE id NOT IN (
                    SELECT roomId FROM table_booking
                    WHERE checkIn < ? AND checkOut > ?
                )
            """, (checkOut, checkIn))
        else:
            cursor.execute("SELECT * FROM table_room")
        return [Room(*row) for row in cursor.fetchall()]


def check_room_is_still_booked(book: Booking):
    with sqlite3.connect('hotel.db') as conn:
        cursor: sqlite3.Cursor = conn.cursor()
        cursor.execute("SELECT COUNT(id) FROM table_booking WHERE checkIn >= ? AND checkIn <= ? AND roomId = ?",
                       (book.checkIn, book.checkOut, book.roomId))
        return cursor.fetchone()[0] > 0


def insert_book_to_bd(book: Booking):
    try:
        with sqlite3.connect('hotel.db') as conn:
            cursor: sqlite3.Cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO table_booking (checkIn, checkOut, firstName, lastName, roomId) VALUES (?, ?, ?, ?, ?)",
                (book.checkIn, book.checkOut, book.firstName, book.lastName, book.roomId)
            )
            book_id = cursor.lastrowid
            return book_id
    except sqlite3.Error as e:
        print("An error occurred while inserting booking:", e)
        return None



