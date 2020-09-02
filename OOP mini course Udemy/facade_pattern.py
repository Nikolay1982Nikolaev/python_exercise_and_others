class TravelOrganizer:
    def __init__(self):
        print("TravelOrganizer: Let me arrange the travel for you!")

    def arrangeTravel(self, destination, type_of_travel):
        print(f"The destination is {destination}")
        self.means_of_transport = Transporter(destination= destination, type_of_travel=type_of_travel)
        self.means_of_transport.book_travel(destination)
        self.means_of_sleeping = Hotelier()
        self.means_of_sleeping.book_room()
        self.means_of_sleeping.arrange_food()


class Transporter:
    def __init__(self, destination, type_of_travel):
        self.destination = destination
        self.type_of_travel = type_of_travel
        print(f"Arranging transport to destination {destination} by means: {type_of_travel}")

    def book_travel(self, destination):
        self.destination = destination
        if self.type_of_travel == "own_car":
            print(f"Nothing to book, the customer uses his/her own car!")
        elif self.type_of_travel == 'plane':
            print(f"Booking seats for gravelling to {self.destination} by plane")
        elif self.type_of_travel == 'bus':
            print(f"Booking seats for gravelling to {self.destination} by bus")


class Hotelier:
    def __init__(self):
        print(f"Arranging room for customers. ---")

    def room_free(self):
        print("Check if there are any rooms left free.")
        return True

    def book_room(self):
        if self.room_free():
            print("Booking room for customer!")

    def arrange_food(self):
        print("Arranging food for the customer!")


class Road_Tripping:
    def __init__(self):
        print(f"Arranging some sightseeing for the customers. ---")

    def arrange_tour(self):
        print(f"Arranging some fancy places to visit!")


class YOU:
    def __init__(self, name):
        print(f"Me: Whoooo we are traveling: {name}")

    def talk_to_agent(self):
        print("Me: asking to arrange this weekend!")
        manager = TravelOrganizer()
        manager.arrangeTravel(destination='Grece', type_of_travel='plane')

    def __del__(self):
        print("Me: Thank you mister manager for arranging us this beatiful weekend")


Me = YOU('Nikolay')
Me.talk_to_agent()
