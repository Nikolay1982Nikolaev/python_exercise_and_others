class mono_state:
    __internal_state = {'A': 5, 'B': 6}

    def __init__(self):
        self.__dict__ = self.__internal_state


class mono_state_v2:
    _internal_state = {}

    def __new__(cls, *args, **kwargs):
        obj = super(mono_state_v2, cls).__new__(cls, *args, **kwargs)
        obj.__dict__ = cls._internal_state


A = mono_state()
B = mono_state()
C = mono_state_v2
D = mono_state_v2
A.x = 10
B.x = 20
C.x = 30
D.x = 40

print(f"A object: {A}")
print(f"B object: {B}")
print(f"A object: {C}")
print(f"B object: {D}")

print(f"A object state: {A.__dict__}")
print(f"B object state: {B.__dict__}")
print(f"A object state: {C.__dict__}")
print(f"B object state: {D.__dict__}")
