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
        wishsttr = ""
        for wish in self.__wishList__:
            wishsttr = wishsttr + wish.getName() + " " + str(wish.getPrio()) + ","
        return wishsttr[:-1]

    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x

class Event:
    __nr__: int = None
class Company:
    __id__: int = None
    __compName__: str = None
    __trainingOccupation__: str = None
    __capacity__: int = None
    __meeting__: [] = None #enthält einen Timeslot und einen Raum


    def __init__(self,id,compName,toc,capacity,meeting) -> None:
        self.__id__ = id
        self.__compName__ = compName
        self.__trainingOccupation__ = toc
        self.__capacity__ = capacity
        self.__meeting__ = meeting

    def setmeeting(self,meeting):
        for element in meeting:
            temp = element.split(",")
            timeslot = Timeslot(temp[0],temp[1])


class Timeplan:
    __timeslots__ = ["A", "B", "C", "D", "E"]
    companylist = list()


class Timeslot:
    __timeSlot__: str = None
    __room__: str = None

    def __init__(self,timeslot,room):
        self.__timeSlot__ = timeslot
        self.__room__ = room

class Transform:
    __stundentList__ = list()
    __companyList__ = list()

    def __init__(self, filepath,filepath2):
        self.load_company(filepath2)
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
    def load_company(self, filepath) -> None:
        import json
        with open(filepath, 'r') as json_datei:
            data = json.load(json_datei)
            for company_data in data['companies']:
                id = company_data['id']
                compname = company_data['compName']
                toc = company_data['trainingOccupation']
                capacity = company_data['capacity']
                meeting = company_data['meeting']
                company = Company(id, compname, toc, capacity, meeting)
                self.__companyList__.append(company)

    def toString(self):
        for company in self.__companyList__:
            print(
                f"ID: {company.__id__}, Name: {company.__compName__}, Beruf: {company.__trainingOccupation__}, Kapazität: {company.__capacity__}, Timeslot:{company.__meeting__} ")
        print("\n")
        for student in self.__stundentList__:
            print(
                f"Vorname: {student.__prename__}, Nachname: {student.__surname__}, Wünsche: {student.wishliststring()}, Klasse: {student.__schoolClass__}")


start = Transform("C:/Users/nilsw/PycharmProjects/BWV-BOT/Transformation/studentTest.json","C:/Users/nilsw/PycharmProjects/BWV-BOT/Transformation/companyTest.json")
