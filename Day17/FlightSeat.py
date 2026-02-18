class FlightSeat:
    def __init__(self):
        self.__is_booked = False
    
    def book(self):
        if not self.__is_booked:
            self.__is_booked = True
            return "Booking successful"
        return "Seat already booked"
    
    def status(self):
        if self.__is_booked:
            return "Booked"
        return "Available"

s1 = FlightSeat()
print(s1.book())
print(s1.status())
print(s1.book())
