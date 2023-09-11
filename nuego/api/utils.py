def is_seat_booked(seats):
    booked_seats = {
        "Front": {
            "Window": str([1, 4]),
            "Aisle": str([2, 3]),
        },
        "Center": {
            "Window": str([5, 8]),
            "Aisle": str([6, 7]),
        },
        "Back": {
            "Window": str([9, 12]),
            "Aisle": str([10, 11]),
        },
    }
    for preference in seats:
        prefer_row = preference["prefer_row"]
        prefer_seat = preference["prefer_seat"]
        seat_number = preference["seat_number"]

        if prefer_row in booked_seats and prefer_seat in booked_seats[prefer_row]:
            if seat_number in booked_seats[prefer_row][prefer_seat]:
                return True

        return False

# from collections import OrderedDict

# data = OrderedDict([('prefer_row', 'Front'), ('prefer_seat', 'Window'), ('seat_number', '122')])
# for key, value in data.items():
#     print(f"{key}: {value}")


#     for preference in seats.:
#         import pdb;
#         pdb.set_trace()
#         preference
# #     if preference == "prefer_row":
#         prefer_row = data
#     if preference == "prefer_seat":
#         prefer_seat = data
#     if preference == "seat_number":
#         seat_number = data
#
#         if prefer_row in booked_seats and prefer_seat in booked_seats[prefer_row]:
#             if seat_number in booked_seats[prefer_row][prefer_seat]:
#                 return True
#
# return False
