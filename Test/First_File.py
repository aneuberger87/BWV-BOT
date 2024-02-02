class Student:
    __prename__: str = None
    __postname__: str = None
    __clas__: str = None
    __wish1__: str = None
    __wish2__: str = None
    __wish3__: str = None
    __wish4__: str = None
    __wish5__: str = None
    __wish6__: str = None

    def __init__(self) -> None:
        pass

    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x


class Company:
    __id__: int = None
    __comname__: str = None
    __training_occupation__: str = None

    def __init__(self) -> None:
        pass


class Timeplan:
    __timeslots__ = ["A", "B", "C", "D", "E"]
    companylist = list()
