from Booking import Book
from Room_info import Room
from Models import get_rooms, init_db, insert_book_to_bd, insert_room_to_bd, \
    check_room_is_still_booked
from datetime import datetime
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/booking', methods=['POST'])
def booking():
    if request.method == "POST":
        data = request.get_json()
        dates = data["bookingDates"]
        check_in = datetime.strptime(str(dates["checkIn"]), "%Y%m%d")
        check_out = datetime.strptime(str(dates["checkOut"]), "%Y%m%d")

        book = Book(
            id=None,
            firstName=data["firstName"],
            lastName=data["lastName"],
            roomId=data["roomId"],
            checkIn=check_in,
            checkOut=check_out
        )

        if check_room_is_still_booked(book):
            return "Room was booked", 409

        room_id = insert_book_to_bd(book)
        return jsonify({"roomId": room_id}), 201


@app.route("/room")
def all_rooms():
    check_in = request.args.get('checkIn')
    check_out = request.args.get('checkOut')
    rooms = get_rooms(check_in, check_out)

    result = {"rooms": []}

    for room in rooms:
        room_data = {
            "roomId": room.id,
            "floor": room.floor,
            "beds": room.beds,
            "guestNum": room.guestNum,
            "price": room.price,
            "bookingDates": {
                "checkIn": check_in,
                "checkOut": check_out,
                "roomId": room.id
            }
        }
        result["rooms"].append(room_data)

    return jsonify(result), 200


@app.route('/add-room', methods=['POST'])
def add_room():
    if request.method != "POST":
        return jsonify({"error": "Method not available"}), 405

    data = request.get_json()

    room = Room(
        id=None,
        floor=data["floor"],
        beds=data["beds"],
        guestNum=data["guestNum"],
        price=data["price"]
    )

    insert_room_to_bd(room)
    return jsonify({"id": room.id}), 201


if __name__ == '__main__':
    init_db()
    app.run(debug=True, host='localhost', port=5000)
