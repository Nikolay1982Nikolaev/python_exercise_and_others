class singleton_lazy:
    __instance = None

    def __init__(self):
        if not singleton_lazy.__instance:
            print("I have already got an instance.")
        else:
            print("I do not yet have an instance.")

    @classmethod
    def get_instance(cls):
        if not cls.__instance:
            cls.__instance = singleton_lazy()
        return cls.__instance


class singleton_strict:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(singleton_strict, cls).__new__(cls)
        return cls.instance


sl1 = singleton_lazy()
sl2 = singleton_lazy()
print(f"sl: {sl1.get_instance()}, sl2: {sl2.get_instance()}")
ss1 = singleton_strict()
ss2 = singleton_strict()
print(f"ss: {ss1}, ss2: {ss2}")

