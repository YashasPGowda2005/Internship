class RoyalMessenger:
    def deliver(self, message):
        return "Delivered: " + message

class UrgentMessenger(RoyalMessenger):
    def deliver(self, message):
        return "URGENT: Delivered: " + message

royal = RoyalMessenger()
urgent = UrgentMessenger()
print(royal.deliver("Your taxes are due."))
print(urgent.deliver("Enemy at the gates!"))
