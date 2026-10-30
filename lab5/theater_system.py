"""
Movie Theater Seat Reservation System.

Supports booking and releasing seats, generating ticket codes,
and saving or loading reservation information.
"""

import json
import hashlib
import os


SHOWS = {
    "SHOW-1": {"title": "Interstellar", "seats": 20, "booked": []},
    "SHOW-2": {"title": "Dangal", "seats": 10, "booked": []}
}


def reserve_seat(show_id, seat_number, system_logs=None):
    """Reserve a seat and record the operation in system logs."""
    if system_logs is None:
        system_logs = []

    show = SHOWS[show_id]

    if seat_number in show["booked"]:
        system_logs.append(
            f"Seat {seat_number} already taken for {show_id}"
        )
        return False

    show["booked"].append(seat_number)
    system_logs.append(f"Reserved seat {seat_number} for {show_id}")
    return True


def release_seat(show_id, seat_number):
    """Release a previously reserved seat."""
    try:
        SHOWS[show_id]["booked"].remove(seat_number)
        return True
    except (KeyError, ValueError):
        return False


def ticket_code(show_id, seat_number):
    """Generate a ticket code for a particular seat."""
    return hashlib.sha256(
        (show_id + str(seat_number)).encode()
    ).hexdigest()[:8]


def dump_reservations(file_path="seats.json"):
    """Save all show reservations to a JSON file."""
    with open(file_path, "w", encoding="utf-8") as file_handle:
        json.dump(SHOWS, file_handle, indent=4)


def load_reservations(file_path="seats.json"):
    """Load reservations from a JSON file."""
    with open(file_path, "r", encoding="utf-8") as file_handle:
        data = json.load(file_handle)

    SHOWS.clear()
    SHOWS.update(data)


def print_seating_summary():
    """Display the available and booked seats for each show."""
    for show in SHOWS.values():
        free = show["seats"] - len(show["booked"])
        print(
            f"{show['title']}: {free} seats free, "
            f"booked = {show['booked']}"
        )


def main():
    """Run the movie theater reservation demonstration."""
    reserve_seat("SHOW-1", 5)
    reserve_seat("SHOW-1", 5)
    reserve_seat("SHOW-1", 25)
    reserve_seat("SHOW-2", -1)
    reserve_seat("SHOW-2", "A7")
    release_seat("SHOW-2", 3)

    print("Ticket code:", ticket_code("SHOW-1", 5))

    seat = input(
        "Seat number to book for SHOW-2 (Enter for 4): "
    ) or "4"

    reserve_seat("SHOW-2", seat)
    dump_reservations()
    load_reservations()
    print_seating_summary()

    os.chmod("seats.json", 0o600)


if __name__ == "__main__":
    main()
