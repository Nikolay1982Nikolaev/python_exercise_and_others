from random import randint


class Player:
    def __init__(self, name):
        self.name = name
        self.price = randint(100000, 900000)
        self.training = False
        self.vacation = False

    def on_training(self):
        self.training = True
        return self.training

    def on_vacation(self):
        self.vacation = True
        return self.vacation

    def get_price(self):
        return self.price

    def status(self):
        return (self.vacation or self.training)


class Manager:
    def __init__(self, player):
        self.managed_player = player
        print(f"Managing player: {self.managed_player.name}")

    def send_player(self, typee):
        if typee in ['vacation', 'training']:
            if typee == 'vacation':
                print(f"Sending player on {self.managed_player.name} vacation.")
                self.managed_player.on_vacation()
            else:
                print(f"Sending player on {self.managed_player.name} training.")
                self.managed_player.on_training()
        else:
            print(f"Can't send player on: {typee}, it's not a valid option!")

    def sell_player(self, offer):
        print(f"The price of the player is {self.managed_player.get_price()}")
        if offer > self.managed_player.get_price():
            print(f'Saying goodbye to {self.managed_player.name}')
        else:
            print(f"Saying No to offer.")




if __name__ == "__main__":
    fballer = Player('Nikolay')
    mgr = Manager(fballer)
    mgr.send_player('vacation')
    mgr.send_player(90000000)

