class Wish:
    __wishname__: str = None
    __prio__: int = None
    __suffused__: bool = False

    def __init__(self, wishname, prio):
        self.__wishname__ = wishname
        self.__prio__ = prio

    def setsuffusedTrue(self):
        self.__suffused__ = True

    def getName(self):
        return self.__wishname__

    def getPrio(self):
        return self.__prio__


class Student:
    __prename__: str = None
    __surname__: str = None
    __schoolClass__: str = None
    __wishList__ = list()

    def __init__(self, prename, surname, schoolclass, wishlist) -> None:
        self.__prename__ = prename
        self.__surname__ = surname
        self.__schoolClass__ = schoolclass
        self.fillList(wishlist)

    def fillList(self, wisharray):
        prio = 1
        temp = list()
        for elemenet in wisharray:
            newWish = Wish(elemenet, prio)
            temp.append(newWish)
            prio = prio + 1
        self.__wishList__ = temp

    def wishliststring(self) -> str:
        wishSttr = ""
        for wish in self.__wishList__:
            wishSttr =wishSttr + wish.getName() + " " + str(wish.getPrio()) + ","
        return wishSttr[:-1]

    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x


class Company:
    __id__: int = None
    __compName__: str = None
    __trainingOccupation__: str = None
    __meeting__: [] = None

    def __init__(self) -> None:
        pass


class Timeplan:
    __timeslots__ = ["A", "B", "C", "D", "E"]
    companylist = list()


class Timeslot:
    __timeSlot__: str = None
    __room__: str = None


class Transform:
    __stundentList__ = list()

    def __init__(self, filepath):
        self.load_student(filepath)
        self.toString()

    def load_student(self, filepath) -> None:
        import json
        with open(filepath, 'r') as json_datei:
            data = json.load(json_datei)
            for student_data in data['Stundent']:
                prename = student_data['vorname']
                surname = student_data['nachname']
                wishlist = student_data['wuensche']
                schoolclass = student_data['klasse']
                student = Student(prename, surname, schoolclass, wishlist)
                self.__stundentList__.append(student)

    def toString(self):
        for student in self.__stundentList__:
            print(
                f"Vorname: {student.__prename__}, Nachname: {student.__surname__}, Wünsche: {student.wishliststring()}, Klasse: {student.__schoolClass__}")


start = Transform("C:/Users/nilsw/PycharmProjects/BWV-BOT/Test/studentTest.json")
