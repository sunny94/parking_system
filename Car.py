class Car:
    def __init__(self, *args, **kwargs):
        self._reg_no = args[0]
        self._color = args[1]
