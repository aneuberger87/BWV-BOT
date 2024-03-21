class Wish:
    __timeslot__: str = None
    __company_id__: int = None
    __prio__: int = None
    __suffused__: bool = False

    def __init__(self, timeslot, company_id, prio):
        self.__prio__ = prio
        self.__timeslot__ = timeslot
        self.__company_id__ = company_id

    def setsuffused_true(self):
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
    __toGolist__ = list()

    def __init__(self, prename, surname, schoolclass, wishlist) -> None:
        self.__prename__ = prename
        self.__surname__ = surname
        self.__schoolClass__ = schoolclass
        self.fillList(wishlist)

    def fillList(self, wisharray):
        prio = 1
        tempwish = wisharray
        if wisharray == None:
            tempTimeslot = ["A","B","C","D","E","A","B"]
            prio = 1
            for _ in range(6):
                tempSlot = tempTimeslot[_]
                tempWish = -1
                newWish = Wish(tempTimeslot, tempWish, prio)
                tempwish.append(newWish)
                prio = prio + 1
        if len(tempwish) < 6:
            i = len(tempwish)
            i: int
            for i in range(6):
                tempTimeslot = ["A", "B", "C", "D", "E", "A", "B"]
                tempSlot = tempTimeslot[i]
                tempWish = -1
                newWish = Wish(tempTimeslot, tempWish, len(tempwish)+1)
                tempwish.append(newWish)
        self.__wishList__ = tempwish
    def wishliststring(self) -> str:
        wishsttr = ""
        for wish in self.__wishList__:
            wishsttr = wishsttr + "Comp_ID: " + str(wish.getCompID()) + "|" + "Prio: " + str(
                wish.getPrio()) + "|" + " Timeslot: " + str(wish.gettimeslot()) + ","
        return wishsttr[:-1]

    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x


class ConcreatWish:
    __studnet__: Student(None, None, None, list())
    __prio__: int = None
    __wishID__: int = None

    def __init__(self, stundent: Student, prio: int, wishID: int):
        self.__studnet__ = stundent
        self.__prio__ = prio
        self.__wishID__ = wishID
    def get_wish_id(self)-> int:
        return int(self.__wishID__)


class Company:
    __id__: int = None
    __compName__: str = None
    __trainingOccupation__: str = None
    __capacity__: int = None
    __meeting__: [] = None  # enthält einen Timeslot und einen Raum
    __timeslotroomlist__ = list()

    def __init__(self, id, compName, toc, meeting) -> None:
        self.__id__ = id
        self.__compName__ = compName
        self.__trainingOccupation__ = toc

        self.__meeting__ = meeting
        self.setmeeting(self.__meeting__)

    def setmeeting(self, meeting):
        self.__timeslotroomlist__ = meeting

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
    __capacity__: int = 20
    __amountofmembers__: int = 0

    def __init__(self, company, id,timeslot):
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
    def setcapacity(self,cap : int) -> None:
        self.__capacity = cap
    def addstudentasparticipant(self, student: Student):
        self.__participantlist__.append(student)

    def toString(self):
        if self.__room__ == None:
            room = "To be done"
        else:
            room = str(self.__room__)
        return ("Versanstalltungsid: " + str(self.__eventid__) + " Unternehmens ID: " + str(
            self.__companyid__) + " Unternehmensname: " + self.__company_name__
                + " Thema: " + self.__event_topic__ + " Raum: " + room + " Timeslot: " + self.__timeslot__)

    def participant_to_string(self):
        line = ""
        for participant in self.__participantlist__:
            line = line + participant.prename + " | " + participant.surname + " | " + str(participant.schoolClass) + "\n"
        return line[:-1]
    def getparticipantlisr(self) -> list:
        return self.__participantlist__

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
            print(event.participant_to_string())
        self.createTimeplanforStudents()

    def filleventList(self):
        for element in self.__companylist__:
            templist = element.__timeslotroomlist__
            for t in templist:
                temptimeslot = t.gettimeslot()
                event = Event(element, self.__eventId__, temptimeslot)
                self.__eventlist__.append(event)
            self.__eventId__ = self.__eventId__ + 1
    def assign_studentstoEvents(self):
        concreateWishlist = list()
        prio = 0
        for prio in range(6):
            for student in self.__studentList__:
                wish = ConcreatWish(student, prio + 1, student.wishList[prio].getCompID())
                concreateWishlist.append(wish)
            for event in self.__eventlist__:
                eventid = event.eventid
                temp_particepent_list = list()
                for element in event.participantlist:
                    temp_particepent_list.append(element)
                for element in concreateWishlist:
                    suffused = element.__studnet__.__wishList__[element.__prio__ - 1].getsuffused()
                    wishID = element.get_wish_id()
                    temp_togolist_forStudnets = list()
                    for togoevent in student.toGolist:
                        temp_togolist_forStudnets.append(togoevent)
                    if eventid == wishID and suffused == False:
                        tslotEvent = event.timeslot
                        checkgo: bool = False
                        for goevent in temp_togolist_forStudnets:
                            if goevent.timeslot == tslotWish:
                                checkgo = True
                        if event.capacity > event.amountofmembers and checkgo != True:
                            temp_particepent_list.append(element.__studnet__)
                            element.__studnet__.__wishList__[element.__prio__ - 1].setsuffused_true()
                            temp_togolist_forStudnets.append(event)
                            event.amountofmembers = event.amountofmembers + 1
                event.participantlist = temp_particepent_list
                temp_togolist_forStudnets.append(event)
                element.__studnet__.__toGolist__ = temp_togolist_forStudnets
        print(" ")

    def createTimeplanforStudents(self):
        perfixfilename = "Laufzettel_für_den_Schueler_ "
        postfixfilename = "_Klasse_"
        api_url = "http://localhost:8080/update/timetableList"
        data = []
        for stundent in self.__studentList__:
            temptoGolist = stundent.toGolist
            prename = stundent.prename
            surname = stundent.surname
            sclass = stundent.schoolClass
            tempjson = self.togo_list_to_json(prename,surname,sclass,temptoGolist)
            data.append(tempjson)
        print("PostRequest with data: ")
        print(data)


    def togo_list_to_json(self,prename:str,surname:str,sclass:str,toGO_liste):
        schueler_json = []
        print("test")
        schueler_data = {
            "prename": prename,
            "surname": surname,
            "schoolclass": sclass,
            "Events": []
        }
        for togoevent in toGO_liste:
            veranstaltung_data = {
                "ID": togoevent.__id__,
                "compName": togoevent.company_name,
                "topic": togoevent.event_topic,
                "timeslot": togoevent.timeslot,
                "room": togoevent.room
            }
        schueler_data["Events"].append(veranstaltung_data)
        return schueler_data
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

    def __init__(self, filepath_students, filepath_company):
        self.load_company(filepath_company)
        self.load_student(filepath_students)
        self.toString()
        t = Timeplan(self.__companyList__, self.__stundentList__)

    def load_student(self, jsonfile) -> None:
        print(jsonfile)
        try:
            for student_data in jsonfile.get('student', []):
                vorname = student_data.get('prename', '')
                nachname = student_data.get('surname', '')
                klasse = student_data.get('schoolClass', '')
                wunschliste = list()
                prio = 1
                for wish_data in student_data.get('wishList', []):
                    tslot = wish_data.get('timeSlot', '')
                    compid = wish_data.get('compId', '')
                    wish = Wish(tslot,compid,prio)
                    wunschliste.append(wish)
                    prio = prio +1
                student = Student(vorname, nachname, klasse, wunschliste)
                self.__stundentList__.append(student)
        except KeyError as e:
            print(f"Schluessel {e} fehlt im Dictionary.")

        except Exception as e:
            print(f"Fehler beim Laden des Schuelers: {e}")

    def load_company(self, jsonfile) -> None:
        print(jsonfile)
        try:
            for company_data in jsonfile.get('company',[]):
                id = company_data.get('id', '')
                compName = company_data.get('compName', '')
                cop = company_data.get('trainingOccupation', '')
                meetinglist = list()
                for meeting_data in company_data.get('meeting', []):
                    tslot = meeting_data.get('timeSlot', '')
                    room = meeting_data.get('room','')
                    timeslot = Timeslot(tslot,room)
                    meetinglist.append(timeslot)
                com = Company(int(id),compName,cop,meetinglist)
                self.__companyList__.append(com)
        except KeyError as e:
            print(f"Schluessel {e} fehlt im Dictionary.")
        except Exception as e:
            print(f"Fehler beim Laden der Company: {e}")

    def toString(self):
        for company in self.__companyList__:
            print(
                f"ID: {company.__id__}, Name: {company.__compName__}, Beruf: {company.__trainingOccupation__}, Kapazität: {company.capacity}, Timeslot:{company.__meeting__} ")
        print("\n")
        for student in self.__stundentList__:
            print(
                f"Vorname: {student.prename}, Nachname: {student.surname}, Wünsche: {student.wishliststring()}, Klasse: {student.schoolClass}")

import requests
api_url = "http://localhost:8080" #?companieslist =
response = requests.get(api_url+"/students")
response2 = requests.get(api_url+"/companies")
response3 = requests.get(api_url+"/rooms")
#rooms
#{"roomList":[{"roomId":"110","capacity":20},{"roomId":"111","capacity":20},{"roomId":"101","capacity":20},{"roomId":"112","capacity":20},{"roomId":"102","capacity":20},{"roomId":"113","capacity":20},{"roomId":"103","capacity":20},{"roomId":"Aula","capacity":20},{"roomId":"106","capacity":20},{"roomId":"107","capacity":20},{"roomId":"108","capacity":20},{"roomId":"109","capacity":20},{"roomId":"209","capacity":20}],"errorMessage":null}
#studnets
#{"student":[{"prename":"Andreas","surname":"Haucap","schoolClass":"HöH222","wishList":[{"compId":4,"timeSlot":""},{"compId":5,"timeSlot":""},{"compId":12,"timeSlot":""},{"compId":13,"timeSlot":""},{"compId":14,"timeSlot":""},{"compId":19,"timeSlot":""}]},{"prename":"Malak","surname":"Alikahn","schoolClass":"HÖH221","wishList":[{"compId":10,"timeSlot":""},{"compId":19,"timeSlot":""},{"compId":16,"timeSlot":""},{"compId":9,"timeSlot":""},{"compId":6,"timeSlot":""},{"compId":18,"timeSlot":""}]},{"prename":"Muhieb","surname":"Almuhandez","schoolClass":"HÖH221","wishList":[{"compId":9,"timeSlot":""},{"compId":6,"timeSlot":""},{"compId":17,"timeSlot":""},{"compId":8,"timeSlot":""},{"compId":13,"timeSlot":""},{"compId":10,"timeSlot":""}]},{"prename":"Lea","surname":"Bendels","schoolClass":"HÖH221","wishList":[{"compId":19,"timeSlot":""},{"compId":18,"timeSlot":""},{"compId":20,"timeSlot":""},{"compId":10,"timeSlot":""},{"compId":2,"timeSlot":""},{"compId":11,"timeSlot":""}]},{"prename":"Connor Luca","surname":"Bücken","schoolClass":"HÖH221","wishList":[{"compId":19,"timeSlot":""},{"compId":21,"timeSlot":""},{"compId":5,"timeSlot":""},{"compId":18,"timeSlot":""},{"compId":10,"timeSlot":""},{"compId":6,"timeSlot":""}]},{"prename":"Mariama","surname":"Dah","schoolClass":"HÖH221","wishList":[{"compId":18,"timeSlot":""},{"compId":18,"timeSlot":""},{"compId":21,"timeSlot":""},{"compId":27,"timeSlot":""},{"compId":4,"timeSlot":""},{"compId":13,"timeSlot":""}]},{"prename":"Haschem","surname":"Daher","schoolClass":"HÖH221","wishList":[{"compId":18,"timeSlot":""},{"compId":3,"timeSlot":""},{"compId":14,"timeSlot":""},{"compId":20,"timeSlot":""},{"compId":13,"timeSlot":""},{"compId":19,"timeSlot":""}]},{"prename":"Rojin","surname":"Demir","schoolClass":"HÖH221","wishList":[{"compId":19,"timeSlot":""},{"compId":18,"timeSlot":""},{"compId":17,"timeSlot":""},{"compId":20,"timeSlot":""},{"compId":2,"timeSlot":""},{"compId":25,"timeSlot":""}]},{"prename":"Tolga","surname":"Dindar","schoolClass":"HÖH221","wishList":[{"compId":19,"timeSlot":""},{"compId":16,"timeSlot":""},{"compId":18,"timeSlot":""},{"compId":26,"timeSlot":""},{"compId":9,"timeSlot":""},{"compId":16,"timeSlot":""}]},{"prename":"Jean-Michel","surname":"Gaßn","schoolClass":"HÖH221","wishList":[{"compId":18,"timeSlot":""},{"compId":3,"timeSlot":""},{"compId":14,"timeSlot":""},{"compId":13,"timeSlot":""},{"compId":4,"timeSlot":""},{"compId":19,"timeSlot":""}]},{"prename":"Asmir","surname":"Hasanic","schoolClass":"HÖH221","wishList":[{"compId":10,"timeSlot":""},{"compId":11,"timeSlot":""},{"compId":15,"timeSlot":""},{"compId":26,"timeSlot":""},{"compId":18,"timeSlot":""},{"compId":9,"timeSlot":""}]},{"prename":"Iskender","surname":"Karanlik","schoolClass":"HÖH221","wishList":[{"compId":9,"timeSlot":""},{"compId":19,"timeSlot":""},{"compId":10,"timeSlot":""},{"compId":3,"timeSlot":""}]},{"prename":"Maximilian","surname":"Kaußn","schoolClass":"HÖH221","wishList":[{"compId":14,"timeSlot":""},{"compId":6,"timeSlot":""},{"compId":15,"timeSlot":""},{"compId":3,"timeSlot":""},{"compId":4,"timeSlot":""},{"compId":1,"timeSlot":""}]},{"prename":"Baris","surname":"Kaya","schoolClass":"HÖH221","wishList":[{"compId":3,"timeSlot":""},{"compId":5,"timeSlot":""},{"compId":7,"timeSlot":""},{"compId":12,"timeSlot":""},{"compId":14,"timeSlot":""},{"compId":13,"timeSlot":""}]},{"prename":"Suat","surname":"Kaya","schoolClass":"HÖH221","wishList":[{"compId":22,"timeSlot":""},{"compId":10,"timeSlot":""},{"compId":16,"timeSlot":""},{"compId":9,"timeSlot":""},{"compId":26,"timeSlot":""},{"compId":6,"timeSlot":""}]},{"prename":"Marijana","surname":"Krilcic","schoolClass":"HÖH221","wishList":[{"compId":16,"timeSlot":""},{"compId":24,"timeSlot":""},{"compId":18,"timeSlot":""},{"compId":23,"timeSlot":""},{"compId":15,"timeSlot":""},{"compId":11,"timeSlot":""}]},{"prename":"Espoir","surname":"luwawu","schoolClass":"HÖH221","wishList":[]},{"prename":"Miranda","surname":"Moustahfid","schoolClass":"HÖH221","wishList":[{"compId":19,"timeSlot":""},{"compId":18,"timeSlot":""},{"compId":17,"timeSlot":""},{"compId":6,"timeSlot":""},{"compId":20,"timeSlot":""},{"compId":22,"timeSlot":""}]},{"prename":"Chloe","surname":"Musi","schoolClass":"HÖH221","wishList":[{"compId":1,"timeSlot":""},{"compId":3,"timeSlot":""},{"compId":6,"timeSlot":""},{"compId":17,"timeSlot":""},{"compId":19,"timeSlot":""},{"compId":9,"timeSlot":""}]},{"prename":"Tutku Cansin","surname":"Siebert","schoolClass":"HÖH221","wishList":[{"compId":19,"timeSlot":""},{"compId":18,"timeSlot":""},{"compId":17,"timeSlot":""},{"compId":6,"timeSlot":""},{"compId":15,"timeSlot":""},{"compId":9,"timeSlot":""}]},{"prename":"Klitjan","surname":"Sylshabanaj","schoolClass":"HÖH221","wishList":[{"compId":6,"timeSlot":""},{"compId":26,"timeSlot":""},{"compId":18,"timeSlot":""},{"compId":9,"timeSlot":""},{"compId":16,"timeSlot":""},{"compId":10,"timeSlot":""}]},{"prename":"Said","surname":"Tchacoura","schoolClass":"HÖH221","wishList":[{"compId":19,"timeSlot":""},{"compId":9,"timeSlot":""},{"compId":21,"timeSlot":""},{"compId":6,"timeSlot":""},{"compId":16,"timeSlot":""},{"compId":10,"timeSlot":""}]},{"prename":"Metehan","surname":"Tuncer","schoolClass":"HÖH221","wishList":[{"compId":9,"timeSlot":""},{"compId":19,"timeSlot":""},{"compId":16,"timeSlot":""},{"compId":6,"timeSlot":""},{"compId":17,"timeSlot":""},{"compId":25,"timeSlot":""}]},{"prename":"Anna Elena","surname":"Vancronenburg","schoolClass":"HÖH221","wishList":[{"compId":27,"timeSlot":""},{"compId":5,"timeSlot":""},{"compId":8,"timeSlot":""},{"compId":13,"timeSlot":""},{"compId":18,"timeSlot":""},{"compId":22,"timeSlot":""}]},{"prename":"Valentina","surname":"Vukelic","schoolClass":"HÖH221","wishList":[{"compId":19,"timeSlot":""},{"compId":10,"timeSlot":""},{"compId":22,"timeSlot":""},{"compId":20,"timeSlot":""},{"compId":21,"timeSlot":""},{"compId":16,"timeSlot":""}]},{"prename":"Zilan","surname":"Yildirim","schoolClass":"HÖH221","wishList":[{"compId":19,"timeSlot":""},{"compId":18,"timeSlot":""},{"compId":21,"timeSlot":""},{"compId":17,"timeSlot":""},{"compId":16,"timeSlot":""},{"compId":15,"timeSlot":""}]},{"prename":"Ali Eren","surname":"Bigay","schoolClass":"ASS221","wishList":[{"compId":6,"timeSlot":""},{"compId":18,"timeSlot":""},{"compId":19,"timeSlot":""},{"compId":4,"timeSlot":""},{"compId":14,"timeSlot":""},{"compId":22,"timeSlot":""}]},{"prename":"Lena","surname":"Graf","schoolClass":"ASS221","wishList":[{"compId":16,"timeSlot":""},{"compId":17,"timeSlot":""},{"compId":9,"timeSlot":""},{"compId":18,"timeSlot":""},{"compId":19,"timeSlot":""},{"compId":15,"timeSlot":""}]},{"prename":"Smilla Marie","surname":"Görgen","schoolClass":"ASS221","wishList":[{"compId":20,"timeSlot":""},{"compId":25,"timeSlot":""},{"compId":1,"timeSlot":""},{"compId":15,"timeSlot":""},{"compId":26,"timeSlot":""},{"compId":11,"timeSlot":""}]},{"prename":"Iclal Ece","surname":"Iskender","schoolClass":"ASS221","wishList":[{"compId":10,"timeSlot":""},{"compId":2,"timeSlot":""},{"compId":6,"timeSlot":""},{"compId":16,"timeSlot":""},{"compId":18,"timeSlot":""},{"compId":15,"timeSlot":""}]},{"prename":"Berfin","surname":"Karakas","schoolClass":"ASS221","wishList":[{"compId":2,"timeSlot":""},{"compId":26,"timeSlot":""},{"compId":13,"timeSlot":""},{"compId":15,"timeSlot":""},{"compId":22,"timeSlot":""},{"compId":23,"timeSlot":""}]},{"prename":"Hazal","surname":"Kavak","schoolClass":"ASS221","wishList":[]},{"prename":"Ayo","surname":"Martins","schoolClass":"ASS221","wishList":[{"compId":6,"timeSlot":""},{"compId":16,"timeSlot":""},{"compId":18,"timeSlot":""},{"compId":23,"timeSlot":""},{"compId":24,"timeSlot":""},{"compId":25,"timeSlot":""}]},{"prename":"Zakariah","surname":"Mohammed","schoolClass":"ASS221","wishList":[{"compId":7,"timeSlot":""},{"compId":13,"timeSlot":""},{"compId":14,"timeSlot":""},{"compId":16,"timeSlot":""},{"compId":18,"timeSlot":""},{"compId":26,"timeSlot":""}]},{"prename":"Hai Nam","surname":"Nguyen","schoolClass":"ASS221","wishList":[{"compId":3,"timeSlot":""},{"compId":6,"timeSlot":""},{"compId":14,"timeSlot":""},{"compId":26,"timeSlot":""},{"compId":19,"timeSlot":""},{"compId":22,"timeSlot":""}]},{"prename":"Ruth","surname":"Ntumba Tshikala","schoolClass":"ASS221","wishList":[{"compId":3,"timeSlot":""},{"compId":18,"timeSlot":""},{"compId":23,"timeSlot":""},{"compId":4,"timeSlot":""},{"compId":15,"timeSlot":""},{"compId":16,"timeSlot":""}]},{"prename":"Erik","surname":"Rausch","schoolClass":"ASS221","wishList":[{"compId":3,"timeSlot":""},{"compId":10,"timeSlot":""},{"compId":16,"timeSlot":""},{"compId":17,"timeSlot":""},{"compId":11,"timeSlot":""},{"compId":9,"timeSlot":""}]},{"prename":"Mustafa","surname":"Saltan","schoolClass":"ASS221","wishList":[{"compId":6,"timeSlot":""},{"compId":18,"timeSlot":""},{"compId":19,"timeSlot":""},{"compId":4,"timeSlot":""},{"compId":14,"timeSlot":""},{"compId":22,"timeSlot":""}]},{"prename":"Isabell","surname":"Schott","schoolClass":"ASS221","wishList":[{"compId":15,"timeSlot":""},{"compId":17,"timeSlot":""},{"compId":3,"timeSlot":""},{"compId":18,"timeSlot":""},{"compId":8,"timeSlot":""},{"compId":16,"timeSlot":""}]},{"prename":"Aleyna","surname":"Sengöz","schoolClass":"ASS221","wishList":[{"compId":1,"timeSlot":""},{"compId":2,"timeSlot":""},{"compId":6,"timeSlot":""},{"compId":16,"timeSlot":""},{"compId":23,"timeSlot":""},{"compId":26,"timeSlot":""}]},{"prename":"Ahmad","surname":"Almoukayed","schoolClass":"WG222","wishList":[{"compId":14,"timeSlot":""},{"compId":19,"timeSlot":""},{"compId":26,"timeSlot":""},{"compId":22,"timeSlot":""},{"compId":20,"timeSlot":""},{"compId":3,"timeSlot":""}]},{"prename":"Julian","surname":"Amann","schoolClass":"WG222","wishList":[{"compId":24,"timeSlot":""},{"compId":9,"timeSlot":""},{"compId":13,"timeSlot":""},{"compId":17,"timeSlot":""},{"compId":19,"timeSlot":""},{"compId":6,"timeSlot":""}]},{"prename":"Dominic","surname":"Eich","schoolClass":"WG222","wishList":[{"compId":19,"timeSlot":""},{"compId":18,"timeSlot":""},{"compId":4,"timeSlot":""},{"compId":16,"timeSlot":""},{"compId":26,"timeSlot":""},{"compId":1,"timeSlot":""}]},{"prename":"Tim","surname":"Freialdenhoven","schoolClass":"WG222","wishList":[{"compId":19,"timeSlot":""},{"compId":14,"timeSlot":""},{"compId":10,"timeSlot":""},{"compId":21,"timeSlot":""},{"compId":3,"timeSlot":""},{"compId":27,"timeSlot":""}]},{"prename":"Jonathan","surname":"Grübler","schoolClass":"WG222","wishList":[{"compId":15,"timeSlot":""},{"compId":17,"timeSlot":""},{"compId":4,"timeSlot":""},{"compId":14,"timeSlot":""},{"compId":13,"timeSlot":""},{"compId":16,"timeSlot":""}]},{"prename":"Viyan","surname":"Günaydin","schoolClass":"WG222","wishList":[{"compId":23,"timeSlot":""},{"compId":26,"timeSlot":""},{"compId":3,"timeSlot":""},{"compId":22,"timeSlot":""},{"compId":18,"timeSlot":""},{"compId":25,"timeSlot":""}]},{"prename":"Jonathan Lorenz","surname":"Kober","schoolClass":"WG222","wishList":[{"compId":3,"timeSlot":""},{"compId":19,"timeSlot":""},{"compId":23,"timeSlot":""},{"compId":14,"timeSlot":""},{"compId":6,"timeSlot":""},{"compId":15,"timeSlot":""}]},{"prename":"Thomas","surname":"Kolokythas","schoolClass":"WG222","wishList":[{"compId":26,"timeSlot":""},{"compId":9,"timeSlot":""},{"compId":13,"timeSlot":""},{"compId":3,"timeSlot":""},{"compId":6,"timeSlot":""},{"compId":17,"timeSlot":""}]},{"prename":"Matilda","surname":"Lewandowska","schoolClass":"WG222","wishList":[{"compId":23,"timeSlot":""},{"compId":26,"timeSlot":""},{"compId":3,"timeSlot":""},{"compId":22,"timeSlot":""},{"compId":18,"timeSlot":""},{"compId":25,"timeSlot":""}]},{"prename":"Lino Alexander","surname":"Maassen","schoolClass":"WG222","wishList":[{"compId":19,"timeSlot":""},{"compId":6,"timeSlot":""},{"compId":14,"timeSlot":""},{"compId":18,"timeSlot":""},{"compId":3,"timeSlot":""},{"compId":26,"timeSlot":""}]},{"prename":"Timo","surname":"Meiß","schoolClass":"WG222","wishList":[{"compId":26,"timeSlot":""},{"compId":23,"timeSlot":""},{"compId":12,"timeSlot":""},{"compId":13,"timeSlot":""},{"compId":6,"timeSlot":""},{"compId":1,"timeSlot":""}]},{"prename":"Mohammed","surname":"Salha","schoolClass":"WG222","wishList":[{"compId":9,"timeSlot":""},{"compId":19,"timeSlot":""},{"compId":26,"timeSlot":""},{"compId":18,"timeSlot":""},{"compId":10,"timeSlot":""},{"compId":11,"timeSlot":""}]},{"prename":"Atakhan","surname":"Sari","schoolClass":"WG222","wishList":[{"compId":4,"timeSlot":""},{"compId":6,"timeSlot":""},{"compId":19,"timeSlot":""},{"compId":14,"timeSlot":""},{"compId":18,"timeSlot":""},{"compId":26,"timeSlot":""}]},{"prename":"Robin","surname":"Schneider","schoolClass":"WG222","wishList":[{"compId":1,"timeSlot":""},{"compId":26,"timeSlot":""},{"compId":23,"timeSlot":""},{"compId":12,"timeSlot":""},{"compId":8,"timeSlot":""},{"compId":4,"timeSlot":""}]},{"prename":"Tahir","surname":"Tutumlu","schoolClass":"WG222","wishList":[{"compId":26,"timeSlot":""},{"compId":9,"timeSlot":""},{"compId":13,"timeSlot":""},{"compId":3,"timeSlot":""},{"compId":6,"timeSlot":""},{"compId":17,"timeSlot":""}]},{"prename":"Ann","surname":"Brettner-Alangyima","schoolClass":"WG221","wishList":[{"compId":4,"timeSlot":""},{"compId":6,"timeSlot":""},{"compId":7,"timeSlot":""},{"compId":9,"timeSlot":""},{"compId":12,"timeSlot":""},{"compId":20,"timeSlot":""}]},{"prename":"Jehan Khalaf","surname":"Dawd","schoolClass":"WG221","wishList":[{"compId":19,"timeSlot":""},{"compId":20,"timeSlot":""},{"compId":18,"timeSlot":""},{"compId":14,"timeSlot":""},{"compId":21,"timeSlot":""},{"compId":2,"timeSlot":""}]},{"prename":"Emily","surname":"Groß","schoolClass":"WG221","wishList":[{"compId":9,"timeSlot":""},{"compId":19,"timeSlot":""},{"compId":8,"timeSlot":""},{"compId":6,"timeSlot":""},{"compId":10,"timeSlot":""},{"compId":24,"timeSlot":""}]},{"prename":"Husna","surname":"Kakar","schoolClass":"WG221","wishList":[{"compId":19,"timeSlot":""},{"compId":20,"timeSlot":""},{"compId":18,"timeSlot":""},{"compId":14,"timeSlot":""},{"compId":21,"timeSlot":""},{"compId":2,"timeSlot":""}]},{"prename":"Joel","surname":"Lauffs","schoolClass":"WG221","wishList":[{"compId":23,"timeSlot":""},{"compId":13,"timeSlot":""},{"compId":19,"timeSlot":""},{"compId":6,"timeSlot":""},{"compId":22,"timeSlot":""},{"compId":4,"timeSlot":""}]},{"prename":"Plamedie","surname":"Matipa","schoolClass":"WG221","wishList":[{"compId":14,"timeSlot":""},{"compId":6,"timeSlot":""},{"compId":4,"timeSlot":""},{"compId":1,"timeSlot":""},{"compId":5,"timeSlot":""},{"compId":16,"timeSlot":""}]},{"prename":"Shamsiddin","surname":"Muhammadiqboli","schoolClass":"WG221","wishList":[{"compId":23,"timeSlot":""},{"compId":22,"timeSlot":""},{"compId":14,"timeSlot":""},{"compId":26,"timeSlot":""},{"compId":3,"timeSlot":""},{"compId":7,"timeSlot":""}]},{"prename":"Diler","surname":"Omer","schoolClass":"WG221","wishList":[{"compId":23,"timeSlot":""},{"compId":15,"timeSlot":""},{"compId":26,"timeSlot":""},{"compId":25,"timeSlot":""},{"compId":22,"timeSlot":""},{"compId":19,"timeSlot":""}]},{"prename":"Vladislav","surname":"Petrov","schoolClass":"WG221","wishList":[{"compId":23,"timeSlot":""},{"compId":22,"timeSlot":""},{"compId":24,"timeSlot":""},{"compId":13,"timeSlot":""},{"compId":3,"timeSlot":""},{"compId":7,"timeSlot":""}]},{"prename":"Michelle","surname":"Scheen","schoolClass":"WG221","wishList":[{"compId":26,"timeSlot":""},{"compId":8,"timeSlot":""},{"compId":9,"timeSlot":""},{"compId":6,"timeSlot":""},{"compId":10,"timeSlot":""},{"compId":16,"timeSlot":""}]},{"prename":"Paul","surname":"Schmücker","schoolClass":"WG221","wishList":[{"compId":19,"timeSlot":""},{"compId":2,"timeSlot":""},{"compId":4,"timeSlot":""},{"compId":26,"timeSlot":""},{"compId":22,"timeSlot":""},{"compId":23,"timeSlot":""}]},{"prename":"Leonie","surname":"Schulz","schoolClass":"WG221","wishList":[{"compId":10,"timeSlot":""},{"compId":11,"timeSlot":""},{"compId":15,"timeSlot":""},{"compId":26,"timeSlot":""},{"compId":23,"timeSlot":""},{"compId":21,"timeSlot":""}]},{"prename":"Tim","surname":"Schwartz","schoolClass":"WG221","wishList":[{"compId":14,"timeSlot":""},{"compId":17,"timeSlot":""},{"compId":10,"timeSlot":""},{"compId":1,"timeSlot":""},{"compId":4,"timeSlot":""},{"compId":3,"timeSlot":""}]},{"prename":"Ahmed","surname":"Soliman","schoolClass":"WG221","wishList":[{"compId":14,"timeSlot":""},{"compId":17,"timeSlot":""},{"compId":10,"timeSlot":""},{"compId":1,"timeSlot":""},{"compId":4,"timeSlot":""},{"compId":3,"timeSlot":""}]},{"prename":"Alassane","surname":"Tall","schoolClass":"WG221","wishList":[{"compId":19,"timeSlot":""},{"compId":10,"timeSlot":""},{"compId":20,"timeSlot":""},{"compId":21,"timeSlot":""},{"compId":5,"timeSlot":""},{"compId":26,"timeSlot":""}]},{"prename":"Clemens","surname":"Thier","schoolClass":"WG221","wishList":[{"compId":26,"timeSlot":""},{"compId":19,"timeSlot":""},{"compId":18,"timeSlot":""},{"compId":14,"timeSlot":""},{"compId":23,"timeSlot":""},{"compId":10,"timeSlot":""}]},{"prename":"Serafina","surname":"Tourniaire","schoolClass":"WG221","wishList":[{"compId":9,"timeSlot":""},{"compId":2,"timeSlot":""},{"compId":7,"timeSlot":""},{"compId":12,"timeSlot":""},{"compId":13,"timeSlot":""},{"compId":14,"timeSlot":""}]},{"prename":"Natan Daniel","surname":"Wieczorek","schoolClass":"WG221","wishList":[{"compId":23,"timeSlot":""},{"compId":16,"timeSlot":""},{"compId":15,"timeSlot":""},{"compId":11,"timeSlot":""},{"compId":6,"timeSlot":""},{"compId":3,"timeSlot":""}]},{"prename":"Adonisa","surname":"Ademi","schoolClass":"HÖH224","wishList":[{"compId":26,"timeSlot":""},{"compId":17,"timeSlot":""},{"compId":8,"timeSlot":""},{"compId":13,"timeSlot":""},{"compId":22,"timeSlot":""},{"compId":16,"timeSlot":""}]},{"prename":"Annalena","surname":"Arifi","schoolClass":"HÖH224","wishList":[{"compId":3,"timeSlot":""},{"compId":6,"timeSlot":""},{"compId":8,"timeSlot":""},{"compId":12,"timeSlot":""},{"compId":15,"timeSlot":""},{"compId":17,"timeSlot":""}]},{"prename":"Iclal","surname":"Erol","schoolClass":"HÖH224","wishList":[{"compId":18,"timeSlot":""},{"compId":2,"timeSlot":""},{"compId":14,"timeSlot":""},{"compId":17,"timeSlot":""},{"compId":15,"timeSlot":""},{"compId":21,"timeSlot":""}]},{"prename":"Volkan Burak","surname":"Erten","schoolClass":"HÖH224","wishList":[{"compId":19,"timeSlot":""},{"compId":9,"timeSlot":""},{"compId":13,"timeSlot":""},{"compId":2,"timeSlot":""},{"compId":6,"timeSlot":""},{"compId":18,"timeSlot":""}]},{"prename":"Zilan","surname":"Ezen","schoolClass":"HÖH224","wishList":[{"compId":26,"timeSlot":""},{"compId":17,"timeSlot":""},{"compId":8,"timeSlot":""},{"compId":13,"timeSlot":""},{"compId":22,"timeSlot":""},{"compId":16,"timeSlot":""}]},{"prename":"Andre","surname":"Grenz","schoolClass":"HÖH224","wishList":[{"compId":20,"timeSlot":""},{"compId":12,"timeSlot":""},{"compId":13,"timeSlot":""},{"compId":14,"timeSlot":""},{"compId":5,"timeSlot":""},{"compId":4,"timeSlot":""}]},{"prename":"Koray","surname":"Gümez","schoolClass":"HÖH224","wishList":[{"compId":8,"timeSlot":""},{"compId":14,"timeSlot":""},{"compId":17,"timeSlot":""},{"compId":3,"timeSlot":""},{"compId":9,"timeSlot":""},{"compId":10,"timeSlot":""}]},{"prename":"Canan Melek","surname":"Kafadar","schoolClass":"HÖH224","wishList":[{"compId":25,"timeSlot":""},{"compId":22,"timeSlot":""},{"compId":20,"timeSlot":""},{"compId":21,"timeSlot":""},{"compId":2,"timeSlot":""},{"compId":1,"timeSlot":""}]},{"prename":"Pelsin","surname":"Korkut","schoolClass":"HÖH224","wishList":[{"compId":2,"timeSlot":""},{"compId":18,"timeSlot":""},{"compId":15,"timeSlot":""},{"compId":3,"timeSlot":""},{"compId":6,"timeSlot":""},{"compId":9,"timeSlot":""}]},{"prename":"Jan","surname":"Kosciukiewicz","schoolClass":"HÖH224","wishList":[{"compId":22,"timeSlot":""},{"compId":26,"timeSlot":""},{"compId":19,"timeSlot":""},{"compId":3,"timeSlot":""},{"compId":14,"timeSlot":""},{"compId":10,"timeSlot":""}]},{"prename":"Rania","surname":"Mahrouk","schoolClass":"HÖH224","wishList":[{"compId":26,"timeSlot":""},{"compId":19,"timeSlot":""},{"compId":16,"timeSlot":""},{"compId":13,"timeSlot":""},{"compId":10,"timeSlot":""},{"compId":22,"timeSlot":""}]},{"prename":"Celina","surname":"Mambor","schoolClass":"HÖH224","wishList":[{"compId":3,"timeSlot":""},{"compId":19,"timeSlot":""},{"compId":13,"timeSlot":""},{"compId":2,"timeSlot":""},{"compId":17,"timeSlot":""},{"compId":6,"timeSlot":""}]},{"prename":"Domenik","surname":"Mang","schoolClass":"HÖH224","wishList":[{"compId":18,"timeSlot":""},{"compId":19,"timeSlot":""},{"compId":14,"timeSlot":""},{"compId":11,"timeSlot":""},{"compId":20,"timeSlot":""},{"compId":17,"timeSlot":""}]},{"prename":"Ahmet Semih","surname":"Okur","schoolClass":"HÖH224","wishList":[{"compId":13,"timeSlot":""},{"compId":1,"timeSlot":""},{"compId":2,"timeSlot":""},{"compId":9,"timeSlot":""},{"compId":16,"timeSlot":""},{"compId":6,"timeSlot":""}]},{"prename":"Aria","surname":"Omar","schoolClass":"HÖH224","wishList":[{"compId":26,"timeSlot":""},{"compId":16,"timeSlot":""},{"compId":13,"timeSlot":""},{"compId":17,"timeSlot":""},{"compId":8,"timeSlot":""},{"compId":19,"timeSlot":""}]},{"prename":"Iman","surname":"Saad","schoolClass":"HÖH224","wishList":[{"compId":9,"timeSlot":""},{"compId":10,"timeSlot":""},{"compId":18,"timeSlot":""},{"compId":21,"timeSlot":""},{"compId":16,"timeSlot":""},{"compId":19,"timeSlot":""}]},{"prename":"Joel-Lucas","surname":"Stengler","schoolClass":"HÖH224","wishList":[{"compId":18,"timeSlot":""},{"compId":6,"timeSlot":""},{"compId":10,"timeSlot":""},{"compId":9,"timeSlot":""},{"compId":16,"timeSlot":""},{"compId":3,"timeSlot":""}]},{"prename":"Zaid","surname":"Talbi","schoolClass":"HÖH224","wishList":[{"compId":14,"timeSlot":""},{"compId":8,"timeSlot":""},{"compId":13,"timeSlot":""},{"compId":6,"timeSlot":""},{"compId":17,"timeSlot":""},{"compId":9,"timeSlot":""}]},{"prename":"Furkan Emre","surname":"Tasdemir","schoolClass":"HÖH224","wishList":[{"compId":19,"timeSlot":""},{"compId":20,"timeSlot":""},{"compId":6,"timeSlot":""},{"compId":21,"timeSlot":""},{"compId":5,"timeSlot":""},{"compId":14,"timeSlot":""}]},{"prename":"Ton Ly David","surname":"Trac","schoolClass":"HÖH224","wishList":[{"compId":2,"timeSlot":""},{"compId":1,"timeSlot":""},{"compId":13,"timeSlot":""},{"compId":9,"timeSlot":""},{"compId":10,"timeSlot":""},{"compId":3,"timeSlot":""}]},{"prename":"Samira","surname":"Ait Oufquir","schoolClass":"HÖH222","wishList":[{"compId":19,"timeSlot":""},{"compId":18,"timeSlot":""},{"compId":6,"timeSlot":""},{"compId":13,"timeSlot":""},{"compId":10,"timeSlot":""},{"compId":14,"timeSlot":""}]},{"prename":"Ayse Nur","surname":"Arslan","schoolClass":"HÖH222","wishList":[{"compId":22,"timeSlot":""},{"compId":19,"timeSlot":""},{"compId":18,"timeSlot":""},{"compId":10,"timeSlot":""},{"compId":1,"timeSlot":""},{"compId":26,"timeSlot":""}]},{"prename":"Rayan","surname":"Benamar","schoolClass":"HÖH222","wishList":[{"compId":18,"timeSlot":""},{"compId":10,"timeSlot":""},{"compId":11,"timeSlot":""},{"compId":22,"timeSlot":""},{"compId":8,"timeSlot":""},{"compId":19,"timeSlot":""}]},{"prename":"Melvin","surname":"Bisevac","schoolClass":"HÖH222","wishList":[{"compId":22,"timeSlot":""},{"compId":19,"timeSlot":""},{"compId":13,"timeSlot":""},{"compId":26,"timeSlot":""},{"compId":18,"timeSlot":""},{"compId":9,"timeSlot":""}]},{"prename":"Deniz","surname":"Bolz","schoolClass":"HÖH222","wishList":[{"compId":16,"timeSlot":""},{"compId":6,"timeSlot":""},{"compId":24,"timeSlot":""},{"compId":19,"timeSlot":""},{"compId":9,"timeSlot":""},{"compId":11,"timeSlot":""}]},{"prename":"Laurin","surname":"Brandt","schoolClass":"HÖH222","wishList":[{"compId":18,"timeSlot":""},{"compId":22,"timeSlot":""},{"compId":19,"timeSlot":""},{"compId":26,"timeSlot":""},{"compId":4,"timeSlot":""},{"compId":6,"timeSlot":""}]},{"prename":"Raul","surname":"Gryszko","schoolClass":"HÖH222","wishList":[{"compId":4,"timeSlot":""},{"compId":5,"timeSlot":""},{"compId":12,"timeSlot":""},{"compId":13,"timeSlot":""},{"compId":14,"timeSlot":""},{"compId":19,"timeSlot":""}]},{"prename":"Fabian","surname":"Hermanns","schoolClass":"HÖH222","wishList":[{"compId":6,"timeSlot":""},{"compId":8,"timeSlot":""},{"compId":14,"timeSlot":""},{"compId":19,"timeSlot":""},{"compId":26,"timeSlot":""},{"compId":2,"timeSlot":""}]},{"prename":"Joel-Luis","surname":"Jöpgen","schoolClass":"HÖH222","wishList":[{"compId":18,"timeSlot":""},{"compId":6,"timeSlot":""},{"compId":19,"timeSlot":""},{"compId":17,"timeSlot":""},{"compId":12,"timeSlot":""},{"compId":14,"timeSlot":""}]},{"prename":"Rohail-Ahmed","surname":"Khan","schoolClass":"HÖH222","wishList":[{"compId":14,"timeSlot":""},{"compId":6,"timeSlot":""},{"compId":15,"timeSlot":""},{"compId":8,"timeSlot":""},{"compId":26,"timeSlot":""},{"compId":1,"timeSlot":""}]},{"prename":"Hicham","surname":"Koubaa","schoolClass":"HÖH222","wishList":[{"compId":18,"timeSlot":""},{"compId":19,"timeSlot":""},{"compId":8,"timeSlot":""},{"compId":3,"timeSlot":""},{"compId":12,"timeSlot":""},{"compId":27,"timeSlot":""}]},{"prename":"Shoshana","surname":"Meuthrath","schoolClass":"HÖH222","wishList":[{"compId":20,"timeSlot":""},{"compId":26,"timeSlot":""},{"compId":7,"timeSlot":""},{"compId":5,"timeSlot":""},{"compId":15,"timeSlot":""},{"compId":11,"timeSlot":""}]},{"prename":"Ezdin","surname":"Miho","schoolClass":"HÖH222","wishList":[{"compId":5,"timeSlot":""},{"compId":12,"timeSlot":""},{"compId":13,"timeSlot":""},{"compId":18,"timeSlot":""},{"compId":19,"timeSlot":""},{"compId":1,"timeSlot":""}]},{"prename":"Rania Katharina","surname":"Najib","schoolClass":"HÖH222","wishList":[{"compId":19,"timeSlot":""},{"compId":14,"timeSlot":""},{"compId":18,"timeSlot":""},{"compId":10,"timeSlot":""},{"compId":16,"timeSlot":""},{"compId":4,"timeSlot":""}]},{"prename":"Aisha","surname":"Rana","schoolClass":"HÖH222","wishList":[{"compId":2,"timeSlot":""},{"compId":27,"timeSlot":""},{"compId":3,"timeSlot":""},{"compId":8,"timeSlot":""},{"compId":7,"timeSlot":""},{"compId":9,"timeSlot":""}]},{"prename":"Nehir Zehra","surname":"Sarigü","schoolClass":"HÖH222","wishList":[{"compId":18,"timeSlot":""},{"compId":19,"timeSlot":""},{"compId":21,"timeSlot":""},{"compId":4,"timeSlot":""},{"compId":20,"timeSlot":""},{"compId":10,"timeSlot":""}]},{"prename":"Alina","surname":"Selimbasic","schoolClass":"HÖH222","wishList":[{"compId":19,"timeSlot":""},{"compId":18,"timeSlot":""},{"compId":16,"timeSlot":""},{"compId":6,"timeSlot":""},{"compId":14,"timeSlot":""},{"compId":3,"timeSlot":""}]},{"prename":"Taha","surname":"Sweiti","schoolClass":"HÖH222","wishList":[{"compId":6,"timeSlot":""},{"compId":19,"timeSlot":""},{"compId":20,"timeSlot":""},{"compId":15,"timeSlot":""},{"compId":3,"timeSlot":""},{"compId":14,"timeSlot":""}]},{"prename":"Bela Maximilian","surname":"Urbanke","schoolClass":"HÖH222","wishList":[{"compId":27,"timeSlot":""},{"compId":4,"timeSlot":""},{"compId":7,"timeSlot":""},{"compId":12,"timeSlot":""},{"compId":14,"timeSlot":""},{"compId":13,"timeSlot":""}]},{"prename":"Oluwaseyi Kehinde","surname":"Adeosun","schoolClass":"HÖH223","wishList":[{"compId":2,"timeSlot":""},{"compId":19,"timeSlot":""},{"compId":24,"timeSlot":""},{"compId":23,"timeSlot":""},{"compId":27,"timeSlot":""},{"compId":1,"timeSlot":""}]},{"prename":"Angelina","surname":"Adolf","schoolClass":"HÖH223","wishList":[{"compId":3,"timeSlot":""},{"compId":6,"timeSlot":""},{"compId":1,"timeSlot":""},{"compId":10,"timeSlot":""},{"compId":15,"timeSlot":""},{"compId":9,"timeSlot":""}]},{"prename":"Lilian","surname":"Ali","schoolClass":"HÖH223","wishList":[{"compId":6,"timeSlot":""},{"compId":10,"timeSlot":""},{"compId":11,"timeSlot":""},{"compId":2,"timeSlot":""},{"compId":27,"timeSlot":""},{"compId":1,"timeSlot":""}]},{"prename":"Catalin-Gabriel","surname":"Ana","schoolClass":"HÖH223","wishList":[{"compId":6,"timeSlot":""},{"compId":3,"timeSlot":""},{"compId":27,"timeSlot":""},{"compId":15,"timeSlot":""},{"compId":13,"timeSlot":""},{"compId":7,"timeSlot":""}]},{"prename":"Zanya","surname":"Aygün","schoolClass":"HÖH223","wishList":[{"compId":10,"timeSlot":""},{"compId":11,"timeSlot":""},{"compId":13,"timeSlot":""},{"compId":2,"timeSlot":""},{"compId":27,"timeSlot":""},{"compId":1,"timeSlot":""}]},{"prename":"Edlisa Gymifua","surname":"Bediako","schoolClass":"HÖH223","wishList":[{"compId":10,"timeSlot":""},{"compId":11,"timeSlot":""},{"compId":9,"timeSlot":""},{"compId":3,"timeSlot":""},{"compId":13,"timeSlot":""},{"compId":6,"timeSlot":""}]},{"prename":"Ahmet Hezdar","surname":"Demir","schoolClass":"HÖH223","wishList":[{"compId":10,"timeSlot":""},{"compId":9,"timeSlot":""},{"compId":11,"timeSlot":""},{"compId":14,"timeSlot":""},{"compId":7,"timeSlot":""},{"compId":13,"timeSlot":""}]},{"prename":"Khalil","surname":"Dirki","schoolClass":"HÖH223","wishList":[{"compId":2,"timeSlot":""},{"compId":4,"timeSlot":""},{"compId":13,"timeSlot":""},{"compId":25,"timeSlot":""},{"compId":26,"timeSlot":""},{"compId":27,"timeSlot":""}]},{"prename":"Anouar","surname":"Dohri","schoolClass":"HÖH223","wishList":[{"compId":26,"timeSlot":""},{"compId":14,"timeSlot":""},{"compId":19,"timeSlot":""},{"compId":18,"timeSlot":""},{"compId":22,"timeSlot":""},{"compId":8,"timeSlot":""}]},{"prename":"Quincy","surname":"Ediawe Agunbiade","schoolClass":"HÖH223","wishList":[{"compId":19,"timeSlot":""},{"compId":3,"timeSlot":""},{"compId":1,"timeSlot":""},{"compId":6,"timeSlot":""},{"compId":7,"timeSlot":""},{"compId":14,"timeSlot":""}]},{"prename":"Jihan","surname":"El Sayed","schoolClass":"HÖH223","wishList":[{"compId":25,"timeSlot":""},{"compId":19,"timeSlot":""},{"compId":18,"timeSlot":""},{"compId":22,"timeSlot":""},{"compId":21,"timeSlot":""},{"compId":13,"timeSlot":""}]},{"prename":"Oleksandra","surname":"Glazkova","schoolClass":"HÖH223","wishList":[{"compId":9,"timeSlot":""},{"compId":19,"timeSlot":""},{"compId":18,"timeSlot":""},{"compId":17,"timeSlot":""},{"compId":15,"timeSlot":""},{"compId":4,"timeSlot":""}]},{"prename":"Ela Nur","surname":"GÖcesin","schoolClass":"HÖH223","wishList":[{"compId":9,"timeSlot":""},{"compId":10,"timeSlot":""},{"compId":11,"timeSlot":""},{"compId":3,"timeSlot":""},{"compId":13,"timeSlot":""},{"compId":12,"timeSlot":""}]},{"prename":"Anna","surname":"Hampeter","schoolClass":"HÖH223","wishList":[{"compId":3,"timeSlot":""},{"compId":1,"timeSlot":""},{"compId":27,"timeSlot":""},{"compId":2,"timeSlot":""},{"compId":7,"timeSlot":""},{"compId":8,"timeSlot":""}]},{"prename":"Hawin","surname":"Kisoglu","schoolClass":"HÖH223","wishList":[{"compId":1,"timeSlot":""},{"compId":19,"timeSlot":""},{"compId":3,"timeSlot":""},{"compId":20,"timeSlot":""},{"compId":27,"timeSlot":""},{"compId":2,"timeSlot":""}]},{"prename":"Rojin","surname":"Kisoglu","schoolClass":"HÖH223","wishList":[{"compId":2,"timeSlot":""},{"compId":6,"timeSlot":""},{"compId":9,"timeSlot":""},{"compId":10,"timeSlot":""},{"compId":1,"timeSlot":""},{"compId":2,"timeSlot":""}]},{"prename":"Bryan","surname":"Malambu","schoolClass":"HÖH223","wishList":[{"compId":17,"timeSlot":""},{"compId":18,"timeSlot":""},{"compId":19,"timeSlot":""},{"compId":16,"timeSlot":""},{"compId":15,"timeSlot":""},{"compId":14,"timeSlot":""}]},{"prename":"Tom","surname":"Mohren","schoolClass":"HÖH223","wishList":[{"compId":7,"timeSlot":""},{"compId":18,"timeSlot":""},{"compId":14,"timeSlot":""},{"compId":19,"timeSlot":""},{"compId":12,"timeSlot":""},{"compId":13,"timeSlot":""}]},{"prename":"Arman","surname":"Rozafshan","schoolClass":"HÖH223","wishList":[{"compId":7,"timeSlot":""},{"compId":22,"timeSlot":""},{"compId":25,"timeSlot":""},{"compId":26,"timeSlot":""},{"compId":3,"timeSlot":""},{"compId":20,"timeSlot":""}]},{"prename":"Anton Wilem","surname":"Rumor","schoolClass":"HÖH223","wishList":[{"compId":17,"timeSlot":""},{"compId":18,"timeSlot":""},{"compId":19,"timeSlot":""},{"compId":16,"timeSlot":""},{"compId":15,"timeSlot":""},{"compId":4,"timeSlot":""}]},{"prename":"Omer","surname":"Selim","schoolClass":"HÖH223","wishList":[{"compId":10,"timeSlot":""},{"compId":11,"timeSlot":""},{"compId":25,"timeSlot":""},{"compId":26,"timeSlot":""},{"compId":24,"timeSlot":""}]},{"prename":"Clotilde","surname":"Tchimbalanga","schoolClass":"HÖH223","wishList":[{"compId":10,"timeSlot":""},{"compId":17,"timeSlot":""},{"compId":18,"timeSlot":""},{"compId":16,"timeSlot":""},{"compId":9,"timeSlot":""},{"compId":11,"timeSlot":""}]},{"prename":"Ilyas","surname":"Tetik","schoolClass":"HÖH223","wishList":[{"compId":10,"timeSlot":""},{"compId":18,"timeSlot":""},{"compId":14,"timeSlot":""},{"compId":12,"timeSlot":""},{"compId":7,"timeSlot":""},{"compId":6,"timeSlot":""}]}],"errorMessage":null}
#compaies
#{"company":[{"id":1,"compName":"Zentis","trainingOccupation":"Industriekaufleute","meeting":[{"timeSlot":"A","room":null},{"timeSlot":"B","room":null},{"timeSlot":"C","room":null},{"timeSlot":"D","room":null},{"timeSlot":"E","room":null}],"numberOfMembers":20},{"id":2,"compName":"Babor Kosmetik ","trainingOccupation":"Industriekaufleute","meeting":[{"timeSlot":"A","room":null},{"timeSlot":"B","room":null},{"timeSlot":"C","room":null},{"timeSlot":"D","room":null},{"timeSlot":"E","room":null}],"numberOfMembers":20},{"id":3,"compName":"EVA (Stawag, RegioIt, Aseag..)","trainingOccupation":"Industriekaufleute","meeting":[{"timeSlot":"A","room":null},{"timeSlot":"B","room":null},{"timeSlot":"C","room":null},{"timeSlot":"D","room":null},{"timeSlot":"E","room":null}],"numberOfMembers":20},{"id":4,"compName":"Grünenthal","trainingOccupation":"Industriekaufleute, BWL Plus (Industriekfm. Plus BWL-Studium), Kaufleute für Büromanagement                                  ","meeting":[{"timeSlot":"A","room":null},{"timeSlot":"B","room":null},{"timeSlot":"C","room":null},{"timeSlot":"D","room":null},{"timeSlot":"E","room":null}],"numberOfMembers":20},{"id":5,"compName":"RWTH Aachen","trainingOccupation":"Kaufleute für Büromanagement","meeting":[{"timeSlot":"A","room":null},{"timeSlot":"B","room":null},{"timeSlot":"C","room":null},{"timeSlot":"D","room":null},{"timeSlot":"E","room":null}],"numberOfMembers":20},{"id":6,"compName":"Aldi ","trainingOccupation":"Einzelhandelskaufleute","meeting":[{"timeSlot":"A","room":null},{"timeSlot":"B","room":null},{"timeSlot":"C","room":null},{"timeSlot":"D","room":null},{"timeSlot":"E","room":null}],"numberOfMembers":20},{"id":7,"compName":"Bauhaus","trainingOccupation":"Einzelhandelskaufleute, Handelsfachwirte, Duales Studium","meeting":[{"timeSlot":"A","room":null},{"timeSlot":"B","room":null},{"timeSlot":"C","room":null},{"timeSlot":"D","room":null},{"timeSlot":"E","room":null}],"numberOfMembers":20},{"id":8,"compName":"Sparkasse Aachen ","trainingOccupation":"Bankkaufleute","meeting":[{"timeSlot":"A","room":null},{"timeSlot":"B","room":null},{"timeSlot":"C","room":null},{"timeSlot":"D","room":null},{"timeSlot":"E","room":null}],"numberOfMembers":20},{"id":9,"compName":"Aachener Bank ","trainingOccupation":"Bankkaufleute","meeting":[{"timeSlot":"A","room":null},{"timeSlot":"B","room":null},{"timeSlot":"C","room":null},{"timeSlot":"D","room":null},{"timeSlot":"E","room":null}],"numberOfMembers":20},{"id":10,"compName":"Debeka","trainingOccupation":"Kaufleute für Versicherungen und Finanzen ","meeting":[{"timeSlot":"A","room":null},{"timeSlot":"B","room":null},{"timeSlot":"C","room":null},{"timeSlot":"D","room":null},{"timeSlot":"E","room":null}],"numberOfMembers":20},{"id":11,"compName":"Steuerberaterkammer Köln ","trainingOccupation":"Steuerfachangestellte","meeting":[{"timeSlot":"A","room":null},{"timeSlot":"B","room":null},{"timeSlot":"C","room":null},{"timeSlot":"D","room":null},{"timeSlot":"E","room":null}],"numberOfMembers":20},{"id":12,"compName":"Rechtsanwaltberufe","trainingOccupation":"Rechtsanwaltsfachangestellte","meeting":[{"timeSlot":"A","room":null},{"timeSlot":"B","room":null},{"timeSlot":"C","room":null},{"timeSlot":"D","room":null},{"timeSlot":"E","room":null}],"numberOfMembers":20},{"id":13,"compName":"Notarberufe","trainingOccupation":"Notarfachangestellte","meeting":[{"timeSlot":"A","room":null},{"timeSlot":"B","room":null},{"timeSlot":"C","room":null},{"timeSlot":"D","room":null},{"timeSlot":"E","room":null}],"numberOfMembers":20},{"id":14,"compName":"Spedition Hammer","trainingOccupation":"Kaufleute für Spedition und Lagerlogistik, Kaufleute für Büromanagement                         ","meeting":[{"timeSlot":"A","room":null},{"timeSlot":"B","room":null},{"timeSlot":"C","room":null},{"timeSlot":"D","room":null},{"timeSlot":"E","room":null}],"numberOfMembers":20},{"id":15,"compName":"Inform","trainingOccupation":"Kaufmann/-frau für Büromanagement ","meeting":[{"timeSlot":"A","room":null},{"timeSlot":"B","room":null},{"timeSlot":"C","room":null},{"timeSlot":"D","room":null},{"timeSlot":"E","room":null}],"numberOfMembers":20},{"id":16,"compName":"Inform","trainingOccupation":"Duales Studium Wirtschaftsinformatik ","meeting":[{"timeSlot":"A","room":null},{"timeSlot":"B","room":null},{"timeSlot":"C","room":null},{"timeSlot":"D","room":null},{"timeSlot":"E","room":null}],"numberOfMembers":20},{"id":17,"compName":"StädteRegion Aachen ","trainingOccupation":"Verwaltungsfachangestellte und Duales Studium Bachelor of Laws/Arts","meeting":[{"timeSlot":"A","room":null},{"timeSlot":"B","room":null},{"timeSlot":"C","room":null},{"timeSlot":"D","room":null},{"timeSlot":"E","room":null}],"numberOfMembers":20},{"id":18,"compName":"Finanzamt","trainingOccupation":"duales Studium Dipl. Finanzwirt/-in ","meeting":[{"timeSlot":"A","room":null},{"timeSlot":"B","room":null},{"timeSlot":"C","room":null},{"timeSlot":"D","room":null},{"timeSlot":"E","room":null}],"numberOfMembers":20},{"id":19,"compName":"Finanzamt ","trainingOccupation":"Ausbildung Finanzwirt/-in ","meeting":[{"timeSlot":"A","room":null},{"timeSlot":"B","room":null},{"timeSlot":"C","room":null},{"timeSlot":"D","room":null},{"timeSlot":"E","room":null}],"numberOfMembers":20},{"id":20,"compName":"Justizvollzugsanstalt","trainingOccupation":"Beamter im allgemeinen Vollzugsdienst, Dipl-Verwaltungswirt (FH)","meeting":[{"timeSlot":"A","room":null},{"timeSlot":"B","room":null},{"timeSlot":"C","room":null},{"timeSlot":"D","room":null},{"timeSlot":"E","room":null}],"numberOfMembers":20},{"id":21,"compName":"Zoll Aachen","trainingOccupation":"Beamter im mittleren und gehobenen Dienst ","meeting":[{"timeSlot":"A","room":null},{"timeSlot":"B","room":null},{"timeSlot":"C","room":null},{"timeSlot":"D","room":null},{"timeSlot":"E","room":null}],"numberOfMembers":20},{"id":22,"compName":"Polizei","trainingOccupation":"Polizeikommisar*in ","meeting":[{"timeSlot":"A","room":null},{"timeSlot":"B","room":null},{"timeSlot":"C","room":null},{"timeSlot":"D","room":null},{"timeSlot":"E","room":null}],"numberOfMembers":25},{"id":23,"compName":"FH Aachen - Studienberatung","trainingOccupation":"","meeting":[{"timeSlot":"A","room":null},{"timeSlot":"B","room":null},{"timeSlot":"C","room":null},{"timeSlot":"D","room":null},{"timeSlot":"E","room":null}],"numberOfMembers":20},{"id":24,"compName":"RWTH Aachen - Studienberatung","trainingOccupation":"Hinweis: Studium hier nur mit Abitur möglich","meeting":[{"timeSlot":"A","room":null},{"timeSlot":"B","room":null},{"timeSlot":"C","room":null},{"timeSlot":"D","room":null},{"timeSlot":"E","room":null}],"numberOfMembers":20},{"id":25,"compName":"Wirtschaftsrecht FH-Aachen","trainingOccupation":"","meeting":[{"timeSlot":"A","room":null},{"timeSlot":"B","room":null},{"timeSlot":"C","room":null},{"timeSlot":"D","room":null},{"timeSlot":"E","room":null}],"numberOfMembers":20},{"id":26,"compName":"Soziale Arbeit ","trainingOccupation":"","meeting":[{"timeSlot":"A","room":null},{"timeSlot":"B","room":null},{"timeSlot":"C","room":null},{"timeSlot":"D","room":null},{"timeSlot":"E","room":null}],"numberOfMembers":20},{"id":27,"compName":"Lehramt Berufskolleg","trainingOccupation":"","meeting":[{"timeSlot":"A","room":null},{"timeSlot":"B","room":null},{"timeSlot":"C","room":null},{"timeSlot":"D","room":null},{"timeSlot":"E","room":null}],"numberOfMembers":20}],"errorMessage":null}
start = Transform(response.json(),response2.json())
