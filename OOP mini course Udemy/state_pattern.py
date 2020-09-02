from abc import abstractmethod, ABCMeta


class internal_state(metaclass=ABCMeta):
    @abstractmethod
    def change_state(self):
        pass


class turned_on(internal_state):
    def change_state(self):
        print("Turning ON the device!!!")
        return "ON"


class turned_off(internal_state):
    def change_state(self):
        print("Turning OFF the device!!!")
        return "OFF"


class increase_volume(internal_state):
    def change_state(self):
        print("Increasing volume by 10")
        return "+10"


class decrease_volume(internal_state):
    def change_state(self):
        print("Decreasing volume by 10")
        return "-10"

class radio_station(internal_state):
    def __init__(self):
        self.state = None

    def get_state(self):
        return self.state

    def set_state(self, status):
        self.state = status

    def change_state(self):
        self.state = self.state.change_state()


radio =radio_station()
print(f"The radios internal state is currently {radio.get_state()}")

ON = turned_on()
OFF = turned_off()
Louder = increase_volume()
Louder = decrease_volume()

print(f"turning ON the radio!")
radio.set_state(ON)
radio.change_state()
print(f"The radios internal state is current {radio.get_state()}")

print(f"turning OFF the radio!")
radio.set_state(OFF)
radio.change_state()
print(f"The radios internal state is current {radio.get_state()}")

print(f"Increasing the volume")
radio.set_state(Louder)
radio.change_state()

print(f"Decreasing the volume")
radio.set_state(Louder)
radio.change_state()
