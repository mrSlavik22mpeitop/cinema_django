from typing import List
from django.db.models.query import QuerySet
from django.http.request import HttpRequest
from seat.models import Seat
from screening.models import Screening
from user_information.models import Booking


def create_seat_layout(seats: QuerySet, seat_columns: int) -> List:
    current_column = 0
    seat_layout = []
    seat_row = []
    for seat in seats:
        seat_row.append(seat)
        current_column += 1
        if current_column == seat_columns:
            seat_layout.append(seat_row)
            seat_row = []
            current_column = 0
    return seat_layout




def make_booking(selected_seat: Seat, request: HttpRequest, id):

    map = Screening.objects.get(id=id)

    if selected_seat.available:
        selected_seat.available = False
        selected_seat.save()
        new_booking = Booking(seat=selected_seat, user=request.user, screening = map)
        new_booking.save()
        return True
    return False

