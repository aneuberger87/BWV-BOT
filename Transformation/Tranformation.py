class Wish:
    __timeslot__: str = None
    __company_id__: int = None
    __prio__: int = None
    __suffused__: bool = False

    def __init__(self, timeslot, company_id, prio):
        self.__prio__ = prio
        self.__timeslot__ = timeslot
        self.__company_id__ = company_id

    def setsuffusedTrue(self):
        self.__suffused__ = True

    def gettimeslot(self):
        return self.__timeslot__

    def getCompID(self):
        return self.__company_id__

    def getPrio(self):
        return self.__prio__

    def getsuffused(self):
        return self.__suffused__


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
        for element in wisharray:
            element.split(",")
            newWish = Wish(element[2], element[0], prio)
            temp.append(newWish)
            prio = prio + 1
        self.__wishList__ = temp

    def wishliststring(self) -> str:
        wishsttr = ""
        for wish in self.__wishList__:
            wishsttr = wishsttr + "Comp_ID: " + wish.getCompID() + "|" + "Prio: " + str(
                wish.getPrio()) + "|" + " Timeslot: " + str(wish.gettimeslot()) + ","
        return wishsttr[:-1]

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
    __capacity__: int = None
    __meeting__: [] = None  # enthält einen Timeslot und einen Raum
    __timeslotroomlist__ = list()

    def __init__(self, id, compName, toc, capacity, meeting) -> None:
        self.__id__ = id
        self.__compName__ = compName
        self.__trainingOccupation__ = toc
        self.__capacity__ = capacity
        self.__meeting__ = meeting
        self.setmeeting(self.__meeting__)

    def setmeeting(self, meeting):
        templist = list()
        for element in meeting:
            temp = element.split(",")
            timeslot = Timeslot(temp[0], temp[1])
            templist.append(timeslot)
        self.__timeslotroomlist__ = templist

    def getroomTimeslotlist(self):
        return self.__timeslotroomlist__

    def getToc(self):
        return self.__trainingOccupation__

    def getCapacity(self):
        return self.__capacity__

    def getID(self):
        return self.__id__

    def getName(self):
        return self.__compName__


class Event:
    __eventid__: int = None
    __company__: Company
    __participantlist__ = list()
    __event_topic__: str = None
    __companyid__: int = None
    __company_name__: str = None
    __room__: str = None
    __timeslot__ = str = None

    def __init__(self, company, id, timeslot):
        self.__eventid__ = id
        self.__company__ = company
        self.__timeslot__ = timeslot
        self.setattributs()

    def setattributs(self):
        self.__event_topic__ = self.__company__.getToc()
        self.__companyid__ = self.__company__.getID()
        self.__company_name__ = self.__company__.getName()
        for element in self.__company__.getroomTimeslotlist():
            if self.__timeslot__ == element.gettimeslot():
                self.__room__ = element.getroom()

    def addstudentasparticipant(self, student: Student):
        self.__participantlist__.append(student)

    def toString(self):
        return ("Versanstalltungsid: " + str(self.__eventid__) + " Unternehmens ID: " + str(
            self.__companyid__) + " Unternehmensname: " + self.__company_name__
                + " Thema: " + self.__event_topic__ + " Raum: " + self.__room__ + " Timeslot: " + self.__timeslot__)


class Timeplan:
    __timeslots__ = ["A", "B", "C", "D", "E"]
    __companylist__ = list()
    __studentList__ = list()
    __eventlist__ = list()
    __eventId__: int = 1

    def __init__(self, companylist, studnetlist):
        self.__companylist__ = companylist
        self.__studentList__ = studnetlist
        self.filleventList()
        self.assign_studentstoEvents()
        for event in self.__eventlist__:
            print(event.toString())
            for participent in event.__participantlist__:
                print(participent.__prename__ + " | " +participent.__surname__ + " | " +participent.__schoolClass__)

    def filleventList(self):
        for element in self.__companylist__:
            templist = element.__timeslotroomlist__
            for t in templist:
                temptimeslot = t.gettimeslot()
                event = Event(element, self.__eventId__, temptimeslot)
                self.__eventId__ = self.__eventId__ + 1
                self.__eventlist__.append(event)

    def assign_studentstoEvents(self):
        for student in self.__studentList__:
            for wish in student.__wishList__:
                for event in self.__eventlist__:
                    if int(event.__eventid__) == int(wish.getCompID()) and wish.getsuffused() == False:
                        event.addstudentasparticipant(student)
                        wish.setsuffusedTrue()

    def zuteilung(schueler_liste, event_liste):
        for schueler in schueler_liste:
            for wunsch in schueler.wuensche:
                for event in event_liste:
                    if event.event_id == wunsch:
                        if event.add_teilnehmer(schueler):

                            break

class Timeslot:
    __timeSlot__: str = None
    __room__: str = None

    def __init__(self, timeslot, room):
        self.__timeSlot__ = timeslot
        self.__room__ = room

    def getroom(self):
        return self.__room__

    def gettimeslot(self):
        return self.__timeSlot__


class Transform:
    __stundentList__ = list()
    __companyList__ = list()

    def __init__(self, filepath, filepath2):
        self.load_company(filepath2)
        self.load_student(filepath)
        self.toString()
        t = Timeplan(self.__companyList__, self.__stundentList__)

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


start = Transform("C:/Users/nilsw/PycharmProjects/BWV-BOT/Transformation/studentTest.json",
                  "C:/Users/nilsw/PycharmProjects/BWV-BOT/Transformation/companyTest.json")
