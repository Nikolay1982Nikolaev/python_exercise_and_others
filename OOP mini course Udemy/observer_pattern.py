# base model for subscribe

class Topic:
    def __init__(self):
        self.__client = []

    def register(self, client):
        print(f"New subscriber {client}")
        self.__client.append(client)

    def notify_all(self, *args, **kwargs):
        for client in self.__client:
            client.notify(self,*args, **kwargs)


class Observer:
    def __init__(self, topic):
        topic.register(self)

    def notify(self, *args, **kwargs):
        print(type(self).__name__,"-->Got", args, "From", topic)


class Another_Observer:
    def __init__(self, topic):
        topic.register(self)

    def notify(self, *args, **kwargs):
        print(type(self).__name__,"-->Got", args, "From", topic)


topic = Topic()
Subscribers = []
for i in range(100):
    Subscribers.append(Observer(topic))
Obs_1 = Observer(topic)
Obs_2 = Another_Observer(topic)
topic.notify_all('Notification')
topic.notify_all("thank you for watching this video, please leave a like and subscribe")

