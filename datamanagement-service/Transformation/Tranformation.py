class Wish:
    timeslot: str = None
    company_id: int = None
    prio: int = None
    suffused: bool = False

    def __init__(self, timeslot, company_id, prio:int):
        self.prio = prio
        self.__timeslot__ = timeslot
        self.company_id = company_id

    def setsuffused_true(self):
        self.suffused = True

    def gettimeslot(self):
        return self.__timeslot__

    def getCompID(self):
        return self.company_id

    def getPrio(self) -> int:
        return int(self.prio)

    def getsuffused(self):
        return self.suffused

class FreeSpot:
    tSlot = ""
    isfree = False

    def setBlocked(self,tslot):
        self.tSlot = tslot
        self.isfree = True
class Room:
    roomId: str = None
    capacity: int = None
    occupy = list()
    def __init__(self, roomId, cap):
        self.roomId = roomId
        self.capacity = cap
        for _ in range(5):
            m = FreeSpot
            self.occupy.append(m)
class Student:
    prename: str = None
    surname: str = None
    schoolClass: str = None
    wishList = list()
    clacwishList = list()
    toGolist = list()
    timeslots = []

    def __init__(self, prename, surname, schoolclass, wishlist) -> None:
        self.prename = prename
        self.surname = surname
        self.schoolClass = schoolclass
        self.fillList(wishlist)
        self.clacwishList = self.wishList

    def fillList(self, wisharray):
        prio = 1
        tempwish = wisharray
        if wisharray == None:
            tempTimeslot = ""
            prio = 1
            for _ in range(6):
                tempWish = -1
                newWish = Wish(tempTimeslot, tempWish, prio)
                tempwish.append(newWish)
                prio = prio + 1
        if len(tempwish) < 6:
            i:int = len(tempwish)
            while i <6:
                tempTimeslot = ""
                tempWish = -1
                newWish = Wish(tempTimeslot, tempWish, len(tempwish)+1)
                tempwish.append(newWish)
                i = i +1
        self.wishList = tempwish
    def wishliststring(self) -> str:
        wishsttr = ""
        for wish in self.wishList:
            wishsttr = wishsttr + "Comp_ID: " + str(wish.getCompID()) + "|" + "Prio: " + str(
                wish.getPrio()) + "|" + " Timeslot: " + str(wish.gettimeslot()) + ","
        return wishsttr[:-1]
    def gettogoList(self):
        return self.toGolist

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

class SolutionScore:
    realScore: int = None

    def __init__(self,number):
        self.realScore = number
    def output(self):
        temp = {
            'realScore': self.realScore
        }
        return temp
class Company:
    __id__: int = None
    __compName__: str = None
    __trainingOccupation__: str = None
    __capacity__: int = None
    __meeting__: [] = None  # enthält einen Timeslot und einen Raum
    __timeslotroomlist__ = list()
    __room__ : Room =("-1",20)

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
    eventid: int = None
    company: Company
    participantlist = list()
    event_topic: str = None
    company_id: int = None
    company_name: str = None
    room: Room = (-1,20)
    timeslot = str = None
    capacity: int = 20
    amountofmembers: int = 0

    def __init__(self, company, id,timeslot):
        self.eventid = id
        self.company = company
        self.timeslot = timeslot
        self.setattributs()


    def setattributs(self):
        self.event_topic = self.company.getToc()
        self.company_id = self.company.getID()
        self.company_name = self.company.getName()
        for element in self.company.getroomTimeslotlist():
            if self.timeslot == element.gettimeslot():
                self.room = self.company.__room__
    def setcapacity(self,cap : int) -> None:
        self.__capacity = cap
    def addstudentasparticipant(self, student: Student):
        self.participantlist.append(student)
    def getTimeslot(self):
        return self.timeslot
    def getCompID(self):
        return self.company_id
    def toString(self):
        if self.room == None:
            room = "To be done"
        else:
            room = str(self.room)
        return ("Versanstalltungsid: " + str(self.eventid) + " Unternehmens ID: " + str(
            self.company_id) + " Unternehmensname: " + self.company_name
                + " Thema: " + self.event_topic + " Raum: " + room + " Timeslot: " + self.timeslot)

    def participant_to_string(self):
        line = ""
        for participant in self.participantlist:
            line = line + participant.prename + " | " + participant.surname + " | " + str(participant.schoolClass) + "\n"
        return line[:-1]
    def getparticipantlisr(self) -> list:
        return self.participantlist

class Timeplan:
    __timeslots__ = ["A", "B", "C", "D", "E"]
    __companylist__ = list()
    studentList = list()
    __eventlist__ = list()
    __eventId__: int = 1

    def __init__(self, companylist, studnetlist):
        self.__companylist__ = companylist
        self.studentList = studnetlist
        self.filleventList()
        self.assign_studentstoEvents()
        outputjson = self.togo_list_to_json(self.studentList)
        score:SolutionScore = self.clacscore()
        print(str(score.realScore))
        self.postStudents(outputjson)
        self.postScore(score)

    def clacscore(self):
        maxscrore = self.clacMaxScore()
        realscore = 0
        for student in self.studentList:
            for wish in student.clacwishList:
                for togoevent in student.toGolist:
                    wishId = wish.getCompID()
                    if wishId == togoevent.eventid:
                        counter = wish.getPrio()
                        if counter == 1:
                            if wish.getCompID != -1:
                                realscore = realscore + 6
                            else:
                                realscore = realscore + 0
                        elif counter == 2:
                            if wish.getCompID != -1:
                                realscore = realscore + 5
                            else:
                                realscore = realscore + 0
                        elif counter == 3:
                            if wish.getCompID != -1:
                                realscore = realscore + 4
                            else:
                                realscore = realscore + 0
                        elif counter == 4:
                            if wish.getCompID != -1:
                                realscore = realscore + 3
                            else:
                                realscore = realscore + 0
                        else:
                            if wish.getCompID != -1:
                                realscore = realscore + 2
                            else:
                                realscore = realscore + 0
        print(realscore)
        print(maxscrore)
        c = SolutionScore((realscore / maxscrore) *100)
        return c
    def clacMaxScore(self):
        maxcore = 0
        test = 0
        for student in self.studentList:
            test = test + 1
            for wish in student.clacwishList:
                counter = wish.getPrio()
                if counter == 1:
                    if wish.getCompID != -1:
                        maxcore = maxcore + 6
                    else:
                        maxcore = maxcore + 0
                elif counter == 2:
                    if wish.getCompID != -1:
                        maxcore = maxcore + 5
                    else:
                        maxcore = maxcore + 0
                elif counter == 3:
                    if wish.getCompID != -1:
                        maxcore = maxcore + 4
                    else:
                        maxcore = maxcore + 0
                elif counter ==  4:
                    if wish.getCompID != -1:
                        maxcore = maxcore + 3
                    else:
                        maxcore = maxcore + 0
                elif counter == 5:
                    if wish.getCompID != -1:
                        maxcore = maxcore + 2
                    else:
                        maxcore = maxcore + 0
        return maxcore
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
            for student in self.studentList:
                wish = ConcreatWish(student, prio + 1, student.wishList[prio].getCompID())
                concreateWishlist.append(wish)
                for event in self.__eventlist__:
                    eventid = event.eventid
                    temp_particepent_list = list()
                    for element in event.participantlist:
                        temp_particepent_list.append(element)
                    for element in concreateWishlist:
                        suffused = element.__studnet__.wishList[element.__prio__ - 1].getsuffused()
                        wishID = element.get_wish_id()
                        temp_togolist_forStudnets = list()
                        checkgo: bool = False
                        tempStundentsTslot = []
                        for tslot in element.__studnet__.timeslots:
                            tempStundentsTslot.append(tslot)
                        for togoevent in student.toGolist:
                            temp_togolist_forStudnets.append(togoevent)
                        if eventid == wishID and suffused == False:
                            tslotEvent = event.timeslot
                            if int(event.capacity) > int(event.amountofmembers) and tslotEvent not in tempStundentsTslot and len(tempStundentsTslot)<5:
                                if len(temp_togolist_forStudnets) +1 < 6 and tslotEvent not in tempStundentsTslot:
                                    temp_particepent_list.append(element.__studnet__)
                                    element.__studnet__.wishList[element.__prio__ - 1].setsuffused_true()
                                    tempStundentsTslot.append(tslotEvent)
                                    element.__studnet__.timeslots = tempStundentsTslot
                                    temp_togolist_forStudnets.append(event)
                                    student.toGolist = temp_togolist_forStudnets
                                    event.amountofmembers = event.amountofmembers + 1
                    event.participantlist = temp_particepent_list

    #post stundets and Company List
    def postStudents(self,jsonstudents):
        print(jsonstudents)
        import requests
        url = "http://localhost:8080/update/studentsList"
        x = requests.post(url, json=jsonstudents)
    def postScore(self,score):
        import requests
        url = "http://localhost:8080/update/solutionScore"
        post = score.output()
        x = requests.post(url, json=post)

    def company_to_dict(self,prename,surname,sclass,eventlist):
        #{"id": 1, "compName": "Zentis", "trainingOccupation": "Industriekaufleute",
        #"meeting": [{"timeSlot": "A", "room": "null"},
        #temp = {
        #    'prename': prename,
        #    'surname': surname,
        #    'schoolClass': sclass,
        #    'wishList': [{'compId': wish.getCompID(),'timeSlot': wish.getTimeslot()} for wish in eventlist]
        #}
        temp = "to be done"
        return temp
    def student_to_dict(self,prename,surname,sclass,eventlist):
        temp = {
            'prename': prename,
            'surname': surname,
            'schoolClass': sclass,
            'wishList': [{'compId': wish.getCompID(),'timeSlot': wish.getTimeslot()} for wish in eventlist]
        }
        return temp
    def togo_list_to_json(self, studentlist):
        import json
        student_list = [self.student_to_dict(student.prename, student.surname, student.schoolClass, student.gettogoList()) for student in studentlist]
        return {'student':student_list}

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

class MaxcompareCrowd:
    __compID__:int = None
    __crowed__:int = 1
    def __init__(self,id):
        self.__compID__ = id
    def andOne(self):
        self.__crowed__ = self.__crowed__ +1

class Transform:
    __stundentList__ = list()
    __companyList__ = list()
    __roomList__ = list()

    def __init__(self, filepath_students, filepath_company,filepath_rooms):
        self.load_company(filepath_company)
        self.load_student(filepath_students)
        self.load_rooms(filepath_rooms)
        self.handleEmptyWishes()
        t = Timeplan(self.__companyList__, self.__stundentList__)

    def setrooms(self):
        import random
        for company in self.__companyList__:
            length = len(self.__roomList__)
            random_number = random.uniform(0, length)
            company.__room__ = self.__roomList__[random_number]


    def handleEmptyWishes(self):
        crowdList = list()
        for company in self.__companyList__:
            m = MaxcompareCrowd(company.__id__)
            crowdList.append(m)
        for studnet in self.__stundentList__:
            for wish in studnet.wishList:
                for max in crowdList:
                    if wish.getCompID == max.__compID__:
                        max.andOne()
        crowdList.sort(key=lambda x: MaxcompareCrowd.__crowed__, reverse=False)
        low = crowdList
        low.sort(key=lambda x: MaxcompareCrowd.__crowed__,reverse=False)
        counter = 0
        lowdigits = []
        for element in low:
            lowdigits.append(element.__compID__)
            counter = counter +1
            if counter >5:
                break
        for studnet in self.__stundentList__:
            for wish in studnet.wishList:
                if wish.getCompID == -1 and wish.__prio__ == 1:
                    wish.getCompID = lowdigits[0]
                if wish.getCompID == -1 and wish.__prio__ == 2:
                    wish.getCompID = lowdigits[1]
                if wish.getCompID == -1 and wish.__prio__ == 3:
                    wish.getCompID = lowdigits[2]
                if wish.getCompID == -1 and wish.__prio__ == 4:
                    wish.getCompID = lowdigits[3]
                if wish.getCompID == -1 and wish.__prio__ == 5:
                    wish.getCompID = lowdigits[4]
                if wish.getCompID == -1 and wish.__prio__ == 6:
                    wish.getCompID = lowdigits[5]

    def load_student(self, jsonfile) -> None:
        #print(jsonfile)
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
        #print(jsonfile)
        try:
            for company_data in jsonfile.get('company', []):
                id = company_data.get('id', '')
                compName = company_data.get('compName', '')
                cop = company_data.get('trainingOccupation', '')
                meetinglist = list()
                for meeting_data in company_data.get('meeting', []):
                    tslot = meeting_data.get('timeSlot', '')
                    room = meeting_data.get('room', '')
                    timeslot = Timeslot(tslot, room)
                    meetinglist.append(timeslot)
                com = Company(int(id), compName, cop, meetinglist)
                self.__companyList__.append(com)
        except KeyError as e:
            print(f"Schluessel {e} fehlt im Dictionary.")
        except Exception as e:
            print(f"Fehler beim Laden der Company: {e}")
    def load_rooms(self, jsonfile) -> None:
        pass
        try:
            for room_data in jsonfile.get('roomList',[]):
                id = room_data.get('roomId', '')
                cap = room_data.get('capacity', '')
                room = Room(id,int(cap))
                self.__roomList__.append(room)
        except KeyError as e:
            print(f"Schluessel {e} fehlt im Dictionary.")
        except Exception as e:
            print(f"Fehler beim Laden der Company: {e}")
    def toString(self):
        for company in self.__companyList__:
            print(
                f"ID: {company.__id__}, Name: {company.__compName__}, Beruf: {company.__trainingOccupation__}, Kapazität: {str(company.__capacity__)}, Timeslot:{company.__meeting__} ")
        print("\n")
        for student in self.__stundentList__:
            print(
                f"Vorname: {student.prename}, Nachname: {student.surname}, Wünsche: {student.wishliststring()}, Klasse: {student.schoolClass}")

import requests
api_url = "http://localhost:8080" #?companieslist =
response = requests.get(api_url+"/students")
response2 = requests.get(api_url+"/companies")
#print(response.json())
response3 = requests.get(api_url+"/rooms")
#rooms
#{"roomList":[{"roomId":"110","capacity":20},{"roomId":"111","capacity":20},{"roomId":"101","capacity":20},{"roomId":"112","capacity":20},{"roomId":"102","capacity":20},{"roomId":"113","capacity":20},{"roomId":"103","capacity":20},{"roomId":"Aula","capacity":20},{"roomId":"106","capacity":20},{"roomId":"107","capacity":20},{"roomId":"108","capacity":20},{"roomId":"109","capacity":20},{"roomId":"209","capacity":20}],"errorMessage":"null"}
#studnets
#json1:dict={"student":[{"prename":"Andreas","surname":"Haucap","schoolClass":"HöH222","wishList":[{"compId":4,"timeSlot":""},{"compId":22,"timeSlot":""},{"compId":12,"timeSlot":""},{"compId":13,"timeSlot":""},{"compId":14,"timeSlot":""},{"compId":19,"timeSlot":""}]},{"prename":"Malak","surname":"Alikahn","schoolClass":"HÖH221","wishList":[{"compId":10,"timeSlot":""},{"compId":19,"timeSlot":""},{"compId":16,"timeSlot":""},{"compId":9,"timeSlot":""},{"compId":6,"timeSlot":""},{"compId":18,"timeSlot":""}]},{"prename":"Muhieb","surname":"Almuhandez","schoolClass":"HÖH221","wishList":[{"compId":9,"timeSlot":""},{"compId":6,"timeSlot":""},{"compId":17,"timeSlot":""},{"compId":8,"timeSlot":""},{"compId":13,"timeSlot":""},{"compId":10,"timeSlot":""}]},{"prename":"Lea","surname":"Bendels","schoolClass":"HÖH221","wishList":[{"compId":19,"timeSlot":""},{"compId":18,"timeSlot":""},{"compId":20,"timeSlot":""},{"compId":10,"timeSlot":""},{"compId":2,"timeSlot":""},{"compId":11,"timeSlot":""}]},{"prename":"Connor Luca","surname":"Bücken","schoolClass":"HÖH221","wishList":[{"compId":19,"timeSlot":""},{"compId":21,"timeSlot":""},{"compId":5,"timeSlot":""},{"compId":18,"timeSlot":""},{"compId":10,"timeSlot":""},{"compId":6,"timeSlot":""}]},{"prename":"Mariama","surname":"Dah","schoolClass":"HÖH221","wishList":[{"compId":18,"timeSlot":""},{"compId":18,"timeSlot":""},{"compId":21,"timeSlot":""},{"compId":27,"timeSlot":""},{"compId":4,"timeSlot":""},{"compId":13,"timeSlot":""}]},{"prename":"Haschem","surname":"Daher","schoolClass":"HÖH221","wishList":[{"compId":18,"timeSlot":""},{"compId":3,"timeSlot":""},{"compId":14,"timeSlot":""},{"compId":20,"timeSlot":""},{"compId":13,"timeSlot":""},{"compId":19,"timeSlot":""}]},{"prename":"Rojin","surname":"Demir","schoolClass":"HÖH221","wishList":[{"compId":19,"timeSlot":""},{"compId":18,"timeSlot":""},{"compId":17,"timeSlot":""},{"compId":20,"timeSlot":""},{"compId":2,"timeSlot":""},{"compId":25,"timeSlot":""}]},{"prename":"Tolga","surname":"Dindar","schoolClass":"HÖH221","wishList":[{"compId":19,"timeSlot":""},{"compId":16,"timeSlot":""},{"compId":18,"timeSlot":""},{"compId":26,"timeSlot":""},{"compId":9,"timeSlot":""},{"compId":16,"timeSlot":""}]},{"prename":"Jean-Michel","surname":"Gaßn","schoolClass":"HÖH221","wishList":[{"compId":18,"timeSlot":""},{"compId":3,"timeSlot":""},{"compId":14,"timeSlot":""},{"compId":13,"timeSlot":""},{"compId":4,"timeSlot":""},{"compId":19,"timeSlot":""}]},{"prename":"Asmir","surname":"Hasanic","schoolClass":"HÖH221","wishList":[{"compId":10,"timeSlot":""},{"compId":11,"timeSlot":""},{"compId":15,"timeSlot":""},{"compId":26,"timeSlot":""},{"compId":18,"timeSlot":""},{"compId":9,"timeSlot":""}]},{"prename":"Iskender","surname":"Karanlik","schoolClass":"HÖH221","wishList":[{"compId":9,"timeSlot":""},{"compId":19,"timeSlot":""},{"compId":10,"timeSlot":""},{"compId":3,"timeSlot":""}]},{"prename":"Maximilian","surname":"Kaußn","schoolClass":"HÖH221","wishList":[{"compId":14,"timeSlot":""},{"compId":6,"timeSlot":""},{"compId":15,"timeSlot":""},{"compId":3,"timeSlot":""},{"compId":4,"timeSlot":""},{"compId":1,"timeSlot":""}]},{"prename":"Baris","surname":"Kaya","schoolClass":"HÖH221","wishList":[{"compId":3,"timeSlot":""},{"compId":5,"timeSlot":""},{"compId":7,"timeSlot":""},{"compId":12,"timeSlot":""},{"compId":14,"timeSlot":""},{"compId":13,"timeSlot":""}]},{"prename":"Suat","surname":"Kaya","schoolClass":"HÖH221","wishList":[{"compId":22,"timeSlot":""},{"compId":10,"timeSlot":""},{"compId":16,"timeSlot":""},{"compId":9,"timeSlot":""},{"compId":26,"timeSlot":""},{"compId":6,"timeSlot":""}]},{"prename":"Marijana","surname":"Krilcic","schoolClass":"HÖH221","wishList":[{"compId":16,"timeSlot":""},{"compId":24,"timeSlot":""},{"compId":18,"timeSlot":""},{"compId":23,"timeSlot":""},{"compId":15,"timeSlot":""},{"compId":11,"timeSlot":""}]},{"prename":"Espoir","surname":"luwawu","schoolClass":"HÖH221","wishList":[]},{"prename":"Miranda","surname":"Moustahfid","schoolClass":"HÖH221","wishList":[{"compId":19,"timeSlot":""},{"compId":18,"timeSlot":""},{"compId":17,"timeSlot":""},{"compId":6,"timeSlot":""},{"compId":20,"timeSlot":""},{"compId":22,"timeSlot":""}]},{"prename":"Chloe","surname":"Musi","schoolClass":"HÖH221","wishList":[{"compId":1,"timeSlot":""},{"compId":3,"timeSlot":""},{"compId":6,"timeSlot":""},{"compId":17,"timeSlot":""},{"compId":19,"timeSlot":""},{"compId":9,"timeSlot":""}]},{"prename":"Tutku Cansin","surname":"Siebert","schoolClass":"HÖH221","wishList":[{"compId":19,"timeSlot":""},{"compId":18,"timeSlot":""},{"compId":17,"timeSlot":""},{"compId":6,"timeSlot":""},{"compId":15,"timeSlot":""},{"compId":9,"timeSlot":""}]},{"prename":"Klitjan","surname":"Sylshabanaj","schoolClass":"HÖH221","wishList":[{"compId":6,"timeSlot":""},{"compId":26,"timeSlot":""},{"compId":18,"timeSlot":""},{"compId":9,"timeSlot":""},{"compId":16,"timeSlot":""},{"compId":10,"timeSlot":""}]},{"prename":"Said","surname":"Tchacoura","schoolClass":"HÖH221","wishList":[{"compId":19,"timeSlot":""},{"compId":9,"timeSlot":""},{"compId":21,"timeSlot":""},{"compId":6,"timeSlot":""},{"compId":16,"timeSlot":""},{"compId":10,"timeSlot":""}]},{"prename":"Metehan","surname":"Tuncer","schoolClass":"HÖH221","wishList":[{"compId":9,"timeSlot":""},{"compId":19,"timeSlot":""},{"compId":16,"timeSlot":""},{"compId":6,"timeSlot":""},{"compId":17,"timeSlot":""},{"compId":25,"timeSlot":""}]},{"prename":"Anna Elena","surname":"Vancronenburg","schoolClass":"HÖH221","wishList":[{"compId":27,"timeSlot":""},{"compId":5,"timeSlot":""},{"compId":8,"timeSlot":""},{"compId":13,"timeSlot":""},{"compId":18,"timeSlot":""},{"compId":22,"timeSlot":""}]},{"prename":"Valentina","surname":"Vukelic","schoolClass":"HÖH221","wishList":[{"compId":19,"timeSlot":""},{"compId":10,"timeSlot":""},{"compId":22,"timeSlot":""},{"compId":20,"timeSlot":""},{"compId":21,"timeSlot":""},{"compId":16,"timeSlot":""}]},{"prename":"Zilan","surname":"Yildirim","schoolClass":"HÖH221","wishList":[{"compId":19,"timeSlot":""},{"compId":18,"timeSlot":""},{"compId":21,"timeSlot":""},{"compId":17,"timeSlot":""},{"compId":16,"timeSlot":""},{"compId":15,"timeSlot":""}]},{"prename":"Ali Eren","surname":"Bigay","schoolClass":"ASS221","wishList":[{"compId":6,"timeSlot":""},{"compId":18,"timeSlot":""},{"compId":19,"timeSlot":""},{"compId":4,"timeSlot":""},{"compId":14,"timeSlot":""},{"compId":22,"timeSlot":""}]},{"prename":"Lena","surname":"Graf","schoolClass":"ASS221","wishList":[{"compId":16,"timeSlot":""},{"compId":17,"timeSlot":""},{"compId":9,"timeSlot":""},{"compId":18,"timeSlot":""},{"compId":19,"timeSlot":""},{"compId":15,"timeSlot":""}]},{"prename":"Smilla Marie","surname":"Görgen","schoolClass":"ASS221","wishList":[{"compId":20,"timeSlot":""},{"compId":25,"timeSlot":""},{"compId":1,"timeSlot":""},{"compId":15,"timeSlot":""},{"compId":26,"timeSlot":""},{"compId":11,"timeSlot":""}]},{"prename":"Iclal Ece","surname":"Iskender","schoolClass":"ASS221","wishList":[{"compId":10,"timeSlot":""},{"compId":2,"timeSlot":""},{"compId":6,"timeSlot":""},{"compId":16,"timeSlot":""},{"compId":18,"timeSlot":""},{"compId":15,"timeSlot":""}]},{"prename":"Berfin","surname":"Karakas","schoolClass":"ASS221","wishList":[{"compId":2,"timeSlot":""},{"compId":26,"timeSlot":""},{"compId":13,"timeSlot":""},{"compId":15,"timeSlot":""},{"compId":22,"timeSlot":""},{"compId":23,"timeSlot":""}]},{"prename":"Hazal","surname":"Kavak","schoolClass":"ASS221","wishList":[]},{"prename":"Ayo","surname":"Martins","schoolClass":"ASS221","wishList":[{"compId":6,"timeSlot":""},{"compId":16,"timeSlot":""},{"compId":18,"timeSlot":""},{"compId":23,"timeSlot":""},{"compId":24,"timeSlot":""},{"compId":25,"timeSlot":""}]},{"prename":"Zakariah","surname":"Mohammed","schoolClass":"ASS221","wishList":[{"compId":7,"timeSlot":""},{"compId":13,"timeSlot":""},{"compId":14,"timeSlot":""},{"compId":16,"timeSlot":""},{"compId":18,"timeSlot":""},{"compId":26,"timeSlot":""}]},{"prename":"Hai Nam","surname":"Nguyen","schoolClass":"ASS221","wishList":[{"compId":3,"timeSlot":""},{"compId":6,"timeSlot":""},{"compId":14,"timeSlot":""},{"compId":26,"timeSlot":""},{"compId":19,"timeSlot":""},{"compId":22,"timeSlot":""}]},{"prename":"Ruth","surname":"Ntumba Tshikala","schoolClass":"ASS221","wishList":[{"compId":3,"timeSlot":""},{"compId":18,"timeSlot":""},{"compId":23,"timeSlot":""},{"compId":4,"timeSlot":""},{"compId":15,"timeSlot":""},{"compId":16,"timeSlot":""}]},{"prename":"Erik","surname":"Rausch","schoolClass":"ASS221","wishList":[{"compId":3,"timeSlot":""},{"compId":10,"timeSlot":""},{"compId":16,"timeSlot":""},{"compId":17,"timeSlot":""},{"compId":11,"timeSlot":""},{"compId":9,"timeSlot":""}]},{"prename":"Mustafa","surname":"Saltan","schoolClass":"ASS221","wishList":[{"compId":6,"timeSlot":""},{"compId":18,"timeSlot":""},{"compId":19,"timeSlot":""},{"compId":4,"timeSlot":""},{"compId":14,"timeSlot":""},{"compId":22,"timeSlot":""}]},{"prename":"Isabell","surname":"Schott","schoolClass":"ASS221","wishList":[{"compId":15,"timeSlot":""},{"compId":17,"timeSlot":""},{"compId":3,"timeSlot":""},{"compId":18,"timeSlot":""},{"compId":8,"timeSlot":""},{"compId":16,"timeSlot":""}]},{"prename":"Aleyna","surname":"Sengöz","schoolClass":"ASS221","wishList":[{"compId":1,"timeSlot":""},{"compId":2,"timeSlot":""},{"compId":6,"timeSlot":""},{"compId":16,"timeSlot":""},{"compId":23,"timeSlot":""},{"compId":26,"timeSlot":""}]},{"prename":"Ahmad","surname":"Almoukayed","schoolClass":"WG222","wishList":[{"compId":14,"timeSlot":""},{"compId":19,"timeSlot":""},{"compId":26,"timeSlot":""},{"compId":22,"timeSlot":""},{"compId":20,"timeSlot":""},{"compId":3,"timeSlot":""}]},{"prename":"Julian","surname":"Amann","schoolClass":"WG222","wishList":[{"compId":24,"timeSlot":""},{"compId":9,"timeSlot":""},{"compId":13,"timeSlot":""},{"compId":17,"timeSlot":""},{"compId":19,"timeSlot":""},{"compId":6,"timeSlot":""}]},{"prename":"Dominic","surname":"Eich","schoolClass":"WG222","wishList":[{"compId":19,"timeSlot":""},{"compId":18,"timeSlot":""},{"compId":4,"timeSlot":""},{"compId":16,"timeSlot":""},{"compId":26,"timeSlot":""},{"compId":1,"timeSlot":""}]},{"prename":"Tim","surname":"Freialdenhoven","schoolClass":"WG222","wishList":[{"compId":19,"timeSlot":""},{"compId":14,"timeSlot":""},{"compId":10,"timeSlot":""},{"compId":21,"timeSlot":""},{"compId":3,"timeSlot":""},{"compId":27,"timeSlot":""}]},{"prename":"Jonathan","surname":"Grübler","schoolClass":"WG222","wishList":[{"compId":15,"timeSlot":""},{"compId":17,"timeSlot":""},{"compId":4,"timeSlot":""},{"compId":14,"timeSlot":""},{"compId":13,"timeSlot":""},{"compId":16,"timeSlot":""}]},{"prename":"Viyan","surname":"Günaydin","schoolClass":"WG222","wishList":[{"compId":23,"timeSlot":""},{"compId":26,"timeSlot":""},{"compId":3,"timeSlot":""},{"compId":22,"timeSlot":""},{"compId":18,"timeSlot":""},{"compId":25,"timeSlot":""}]},{"prename":"Jonathan Lorenz","surname":"Kober","schoolClass":"WG222","wishList":[{"compId":3,"timeSlot":""},{"compId":19,"timeSlot":""},{"compId":23,"timeSlot":""},{"compId":14,"timeSlot":""},{"compId":6,"timeSlot":""},{"compId":15,"timeSlot":""}]},{"prename":"Thomas","surname":"Kolokythas","schoolClass":"WG222","wishList":[{"compId":26,"timeSlot":""},{"compId":9,"timeSlot":""},{"compId":13,"timeSlot":""},{"compId":3,"timeSlot":""},{"compId":6,"timeSlot":""},{"compId":17,"timeSlot":""}]},{"prename":"Matilda","surname":"Lewandowska","schoolClass":"WG222","wishList":[{"compId":23,"timeSlot":""},{"compId":26,"timeSlot":""},{"compId":3,"timeSlot":""},{"compId":22,"timeSlot":""},{"compId":18,"timeSlot":""},{"compId":25,"timeSlot":""}]},{"prename":"Lino Alexander","surname":"Maassen","schoolClass":"WG222","wishList":[{"compId":19,"timeSlot":""},{"compId":6,"timeSlot":""},{"compId":14,"timeSlot":""},{"compId":18,"timeSlot":""},{"compId":3,"timeSlot":""},{"compId":26,"timeSlot":""}]},{"prename":"Timo","surname":"Meiß","schoolClass":"WG222","wishList":[{"compId":26,"timeSlot":""},{"compId":23,"timeSlot":""},{"compId":12,"timeSlot":""},{"compId":13,"timeSlot":""},{"compId":6,"timeSlot":""},{"compId":1,"timeSlot":""}]},{"prename":"Mohammed","surname":"Salha","schoolClass":"WG222","wishList":[{"compId":9,"timeSlot":""},{"compId":19,"timeSlot":""},{"compId":26,"timeSlot":""},{"compId":18,"timeSlot":""},{"compId":10,"timeSlot":""},{"compId":11,"timeSlot":""}]},{"prename":"Atakhan","surname":"Sari","schoolClass":"WG222","wishList":[{"compId":4,"timeSlot":""},{"compId":6,"timeSlot":""},{"compId":19,"timeSlot":""},{"compId":14,"timeSlot":""},{"compId":18,"timeSlot":""},{"compId":26,"timeSlot":""}]},{"prename":"Robin","surname":"Schneider","schoolClass":"WG222","wishList":[{"compId":1,"timeSlot":""},{"compId":26,"timeSlot":""},{"compId":23,"timeSlot":""},{"compId":12,"timeSlot":""},{"compId":8,"timeSlot":""},{"compId":4,"timeSlot":""}]},{"prename":"Tahir","surname":"Tutumlu","schoolClass":"WG222","wishList":[{"compId":26,"timeSlot":""},{"compId":9,"timeSlot":""},{"compId":13,"timeSlot":""},{"compId":3,"timeSlot":""},{"compId":6,"timeSlot":""},{"compId":17,"timeSlot":""}]},{"prename":"Ann","surname":"Brettner-Alangyima","schoolClass":"WG221","wishList":[{"compId":4,"timeSlot":""},{"compId":6,"timeSlot":""},{"compId":7,"timeSlot":""},{"compId":9,"timeSlot":""},{"compId":12,"timeSlot":""},{"compId":20,"timeSlot":""}]},{"prename":"Jehan Khalaf","surname":"Dawd","schoolClass":"WG221","wishList":[{"compId":19,"timeSlot":""},{"compId":20,"timeSlot":""},{"compId":18,"timeSlot":""},{"compId":14,"timeSlot":""},{"compId":21,"timeSlot":""},{"compId":2,"timeSlot":""}]},{"prename":"Emily","surname":"Groß","schoolClass":"WG221","wishList":[{"compId":9,"timeSlot":""},{"compId":19,"timeSlot":""},{"compId":8,"timeSlot":""},{"compId":6,"timeSlot":""},{"compId":10,"timeSlot":""},{"compId":24,"timeSlot":""}]},{"prename":"Husna","surname":"Kakar","schoolClass":"WG221","wishList":[{"compId":19,"timeSlot":""},{"compId":20,"timeSlot":""},{"compId":18,"timeSlot":""},{"compId":14,"timeSlot":""},{"compId":21,"timeSlot":""},{"compId":2,"timeSlot":""}]},{"prename":"Joel","surname":"Lauffs","schoolClass":"WG221","wishList":[{"compId":23,"timeSlot":""},{"compId":13,"timeSlot":""},{"compId":19,"timeSlot":""},{"compId":6,"timeSlot":""},{"compId":22,"timeSlot":""},{"compId":4,"timeSlot":""}]},{"prename":"Plamedie","surname":"Matipa","schoolClass":"WG221","wishList":[{"compId":14,"timeSlot":""},{"compId":6,"timeSlot":""},{"compId":4,"timeSlot":""},{"compId":1,"timeSlot":""},{"compId":5,"timeSlot":""},{"compId":16,"timeSlot":""}]},{"prename":"Shamsiddin","surname":"Muhammadiqboli","schoolClass":"WG221","wishList":[{"compId":23,"timeSlot":""},{"compId":22,"timeSlot":""},{"compId":14,"timeSlot":""},{"compId":26,"timeSlot":""},{"compId":3,"timeSlot":""},{"compId":7,"timeSlot":""}]},{"prename":"Diler","surname":"Omer","schoolClass":"WG221","wishList":[{"compId":23,"timeSlot":""},{"compId":15,"timeSlot":""},{"compId":26,"timeSlot":""},{"compId":25,"timeSlot":""},{"compId":22,"timeSlot":""},{"compId":19,"timeSlot":""}]},{"prename":"Vladislav","surname":"Petrov","schoolClass":"WG221","wishList":[{"compId":23,"timeSlot":""},{"compId":22,"timeSlot":""},{"compId":24,"timeSlot":""},{"compId":13,"timeSlot":""},{"compId":3,"timeSlot":""},{"compId":7,"timeSlot":""}]},{"prename":"Michelle","surname":"Scheen","schoolClass":"WG221","wishList":[{"compId":26,"timeSlot":""},{"compId":8,"timeSlot":""},{"compId":9,"timeSlot":""},{"compId":6,"timeSlot":""},{"compId":10,"timeSlot":""},{"compId":16,"timeSlot":""}]},{"prename":"Paul","surname":"Schmücker","schoolClass":"WG221","wishList":[{"compId":19,"timeSlot":""},{"compId":2,"timeSlot":""},{"compId":4,"timeSlot":""},{"compId":26,"timeSlot":""},{"compId":22,"timeSlot":""},{"compId":23,"timeSlot":""}]},{"prename":"Leonie","surname":"Schulz","schoolClass":"WG221","wishList":[{"compId":10,"timeSlot":""},{"compId":11,"timeSlot":""},{"compId":15,"timeSlot":""},{"compId":26,"timeSlot":""},{"compId":23,"timeSlot":""},{"compId":21,"timeSlot":""}]},{"prename":"Tim","surname":"Schwartz","schoolClass":"WG221","wishList":[{"compId":14,"timeSlot":""},{"compId":17,"timeSlot":""},{"compId":10,"timeSlot":""},{"compId":1,"timeSlot":""},{"compId":4,"timeSlot":""},{"compId":3,"timeSlot":""}]},{"prename":"Ahmed","surname":"Soliman","schoolClass":"WG221","wishList":[{"compId":14,"timeSlot":""},{"compId":17,"timeSlot":""},{"compId":10,"timeSlot":""},{"compId":1,"timeSlot":""},{"compId":4,"timeSlot":""},{"compId":3,"timeSlot":""}]},{"prename":"Alassane","surname":"Tall","schoolClass":"WG221","wishList":[{"compId":19,"timeSlot":""},{"compId":10,"timeSlot":""},{"compId":20,"timeSlot":""},{"compId":21,"timeSlot":""},{"compId":5,"timeSlot":""},{"compId":26,"timeSlot":""}]},{"prename":"Clemens","surname":"Thier","schoolClass":"WG221","wishList":[{"compId":26,"timeSlot":""},{"compId":19,"timeSlot":""},{"compId":18,"timeSlot":""},{"compId":14,"timeSlot":""},{"compId":23,"timeSlot":""},{"compId":10,"timeSlot":""}]},{"prename":"Serafina","surname":"Tourniaire","schoolClass":"WG221","wishList":[{"compId":9,"timeSlot":""},{"compId":2,"timeSlot":""},{"compId":7,"timeSlot":""},{"compId":12,"timeSlot":""},{"compId":13,"timeSlot":""},{"compId":14,"timeSlot":""}]},{"prename":"Natan Daniel","surname":"Wieczorek","schoolClass":"WG221","wishList":[{"compId":23,"timeSlot":""},{"compId":16,"timeSlot":""},{"compId":15,"timeSlot":""},{"compId":11,"timeSlot":""},{"compId":6,"timeSlot":""},{"compId":3,"timeSlot":""}]},{"prename":"Adonisa","surname":"Ademi","schoolClass":"HÖH224","wishList":[{"compId":26,"timeSlot":""},{"compId":17,"timeSlot":""},{"compId":8,"timeSlot":""},{"compId":13,"timeSlot":""},{"compId":22,"timeSlot":""},{"compId":16,"timeSlot":""}]},{"prename":"Annalena","surname":"Arifi","schoolClass":"HÖH224","wishList":[{"compId":3,"timeSlot":""},{"compId":6,"timeSlot":""},{"compId":8,"timeSlot":""},{"compId":12,"timeSlot":""},{"compId":15,"timeSlot":""},{"compId":17,"timeSlot":""}]},{"prename":"Iclal","surname":"Erol","schoolClass":"HÖH224","wishList":[{"compId":18,"timeSlot":""},{"compId":2,"timeSlot":""},{"compId":14,"timeSlot":""},{"compId":17,"timeSlot":""},{"compId":15,"timeSlot":""},{"compId":21,"timeSlot":""}]},{"prename":"Volkan Burak","surname":"Erten","schoolClass":"HÖH224","wishList":[{"compId":19,"timeSlot":""},{"compId":9,"timeSlot":""},{"compId":13,"timeSlot":""},{"compId":2,"timeSlot":""},{"compId":6,"timeSlot":""},{"compId":18,"timeSlot":""}]},{"prename":"Zilan","surname":"Ezen","schoolClass":"HÖH224","wishList":[{"compId":26,"timeSlot":""},{"compId":17,"timeSlot":""},{"compId":8,"timeSlot":""},{"compId":13,"timeSlot":""},{"compId":22,"timeSlot":""},{"compId":16,"timeSlot":""}]},{"prename":"Andre","surname":"Grenz","schoolClass":"HÖH224","wishList":[{"compId":20,"timeSlot":""},{"compId":12,"timeSlot":""},{"compId":13,"timeSlot":""},{"compId":14,"timeSlot":""},{"compId":5,"timeSlot":""},{"compId":4,"timeSlot":""}]},{"prename":"Koray","surname":"Gümez","schoolClass":"HÖH224","wishList":[{"compId":8,"timeSlot":""},{"compId":14,"timeSlot":""},{"compId":17,"timeSlot":""},{"compId":3,"timeSlot":""},{"compId":9,"timeSlot":""},{"compId":10,"timeSlot":""}]},{"prename":"Canan Melek","surname":"Kafadar","schoolClass":"HÖH224","wishList":[{"compId":25,"timeSlot":""},{"compId":22,"timeSlot":""},{"compId":20,"timeSlot":""},{"compId":21,"timeSlot":""},{"compId":2,"timeSlot":""},{"compId":1,"timeSlot":""}]},{"prename":"Pelsin","surname":"Korkut","schoolClass":"HÖH224","wishList":[{"compId":2,"timeSlot":""},{"compId":18,"timeSlot":""},{"compId":15,"timeSlot":""},{"compId":3,"timeSlot":""},{"compId":6,"timeSlot":""},{"compId":9,"timeSlot":""}]},{"prename":"Jan","surname":"Kosciukiewicz","schoolClass":"HÖH224","wishList":[{"compId":22,"timeSlot":""},{"compId":26,"timeSlot":""},{"compId":19,"timeSlot":""},{"compId":3,"timeSlot":""},{"compId":14,"timeSlot":""},{"compId":10,"timeSlot":""}]},{"prename":"Rania","surname":"Mahrouk","schoolClass":"HÖH224","wishList":[{"compId":26,"timeSlot":""},{"compId":19,"timeSlot":""},{"compId":16,"timeSlot":""},{"compId":13,"timeSlot":""},{"compId":10,"timeSlot":""},{"compId":22,"timeSlot":""}]},{"prename":"Celina","surname":"Mambor","schoolClass":"HÖH224","wishList":[{"compId":3,"timeSlot":""},{"compId":19,"timeSlot":""},{"compId":13,"timeSlot":""},{"compId":2,"timeSlot":""},{"compId":17,"timeSlot":""},{"compId":6,"timeSlot":""}]},{"prename":"Domenik","surname":"Mang","schoolClass":"HÖH224","wishList":[{"compId":18,"timeSlot":""},{"compId":19,"timeSlot":""},{"compId":14,"timeSlot":""},{"compId":11,"timeSlot":""},{"compId":20,"timeSlot":""},{"compId":17,"timeSlot":""}]},{"prename":"Ahmet Semih","surname":"Okur","schoolClass":"HÖH224","wishList":[{"compId":13,"timeSlot":""},{"compId":1,"timeSlot":""},{"compId":2,"timeSlot":""},{"compId":9,"timeSlot":""},{"compId":16,"timeSlot":""},{"compId":6,"timeSlot":""}]},{"prename":"Aria","surname":"Omar","schoolClass":"HÖH224","wishList":[{"compId":26,"timeSlot":""},{"compId":16,"timeSlot":""},{"compId":13,"timeSlot":""},{"compId":17,"timeSlot":""},{"compId":8,"timeSlot":""},{"compId":19,"timeSlot":""}]},{"prename":"Iman","surname":"Saad","schoolClass":"HÖH224","wishList":[{"compId":9,"timeSlot":""},{"compId":10,"timeSlot":""},{"compId":18,"timeSlot":""},{"compId":21,"timeSlot":""},{"compId":16,"timeSlot":""},{"compId":19,"timeSlot":""}]},{"prename":"Joel-Lucas","surname":"Stengler","schoolClass":"HÖH224","wishList":[{"compId":18,"timeSlot":""},{"compId":6,"timeSlot":""},{"compId":10,"timeSlot":""},{"compId":9,"timeSlot":""},{"compId":16,"timeSlot":""},{"compId":3,"timeSlot":""}]},{"prename":"Zaid","surname":"Talbi","schoolClass":"HÖH224","wishList":[{"compId":14,"timeSlot":""},{"compId":8,"timeSlot":""},{"compId":13,"timeSlot":""},{"compId":6,"timeSlot":""},{"compId":17,"timeSlot":""},{"compId":9,"timeSlot":""}]},{"prename":"Furkan Emre","surname":"Tasdemir","schoolClass":"HÖH224","wishList":[{"compId":19,"timeSlot":""},{"compId":20,"timeSlot":""},{"compId":6,"timeSlot":""},{"compId":21,"timeSlot":""},{"compId":5,"timeSlot":""},{"compId":14,"timeSlot":""}]},{"prename":"Ton Ly David","surname":"Trac","schoolClass":"HÖH224","wishList":[{"compId":2,"timeSlot":""},{"compId":1,"timeSlot":""},{"compId":13,"timeSlot":""},{"compId":9,"timeSlot":""},{"compId":10,"timeSlot":""},{"compId":3,"timeSlot":""}]},{"prename":"Samira","surname":"Ait Oufquir","schoolClass":"HÖH222","wishList":[{"compId":19,"timeSlot":""},{"compId":18,"timeSlot":""},{"compId":6,"timeSlot":""},{"compId":13,"timeSlot":""},{"compId":10,"timeSlot":""},{"compId":14,"timeSlot":""}]},{"prename":"Ayse Nur","surname":"Arslan","schoolClass":"HÖH222","wishList":[{"compId":22,"timeSlot":""},{"compId":19,"timeSlot":""},{"compId":18,"timeSlot":""},{"compId":10,"timeSlot":""},{"compId":1,"timeSlot":""},{"compId":26,"timeSlot":""}]},{"prename":"Rayan","surname":"Benamar","schoolClass":"HÖH222","wishList":[{"compId":18,"timeSlot":""},{"compId":10,"timeSlot":""},{"compId":11,"timeSlot":""},{"compId":22,"timeSlot":""},{"compId":8,"timeSlot":""},{"compId":19,"timeSlot":""}]},{"prename":"Melvin","surname":"Bisevac","schoolClass":"HÖH222","wishList":[{"compId":22,"timeSlot":""},{"compId":19,"timeSlot":""},{"compId":13,"timeSlot":""},{"compId":26,"timeSlot":""},{"compId":18,"timeSlot":""},{"compId":9,"timeSlot":""}]},{"prename":"Deniz","surname":"Bolz","schoolClass":"HÖH222","wishList":[{"compId":16,"timeSlot":""},{"compId":6,"timeSlot":""},{"compId":24,"timeSlot":""},{"compId":19,"timeSlot":""},{"compId":9,"timeSlot":""},{"compId":11,"timeSlot":""}]},{"prename":"Laurin","surname":"Brandt","schoolClass":"HÖH222","wishList":[{"compId":18,"timeSlot":""},{"compId":22,"timeSlot":""},{"compId":19,"timeSlot":""},{"compId":26,"timeSlot":""},{"compId":4,"timeSlot":""},{"compId":6,"timeSlot":""}]},{"prename":"Raul","surname":"Gryszko","schoolClass":"HÖH222","wishList":[{"compId":4,"timeSlot":""},{"compId":5,"timeSlot":""},{"compId":12,"timeSlot":""},{"compId":13,"timeSlot":""},{"compId":14,"timeSlot":""},{"compId":19,"timeSlot":""}]},{"prename":"Fabian","surname":"Hermanns","schoolClass":"HÖH222","wishList":[{"compId":6,"timeSlot":""},{"compId":8,"timeSlot":""},{"compId":14,"timeSlot":""},{"compId":19,"timeSlot":""},{"compId":26,"timeSlot":""},{"compId":2,"timeSlot":""}]},{"prename":"Joel-Luis","surname":"Jöpgen","schoolClass":"HÖH222","wishList":[{"compId":18,"timeSlot":""},{"compId":6,"timeSlot":""},{"compId":19,"timeSlot":""},{"compId":17,"timeSlot":""},{"compId":12,"timeSlot":""},{"compId":14,"timeSlot":""}]},{"prename":"Rohail-Ahmed","surname":"Khan","schoolClass":"HÖH222","wishList":[{"compId":14,"timeSlot":""},{"compId":6,"timeSlot":""},{"compId":15,"timeSlot":""},{"compId":8,"timeSlot":""},{"compId":26,"timeSlot":""},{"compId":1,"timeSlot":""}]},{"prename":"Hicham","surname":"Koubaa","schoolClass":"HÖH222","wishList":[{"compId":18,"timeSlot":""},{"compId":19,"timeSlot":""},{"compId":8,"timeSlot":""},{"compId":3,"timeSlot":""},{"compId":12,"timeSlot":""},{"compId":27,"timeSlot":""}]},{"prename":"Shoshana","surname":"Meuthrath","schoolClass":"HÖH222","wishList":[{"compId":20,"timeSlot":""},{"compId":26,"timeSlot":""},{"compId":7,"timeSlot":""},{"compId":5,"timeSlot":""},{"compId":15,"timeSlot":""},{"compId":11,"timeSlot":""}]},{"prename":"Ezdin","surname":"Miho","schoolClass":"HÖH222","wishList":[{"compId":5,"timeSlot":""},{"compId":12,"timeSlot":""},{"compId":13,"timeSlot":""},{"compId":18,"timeSlot":""},{"compId":19,"timeSlot":""},{"compId":1,"timeSlot":""}]},{"prename":"Rania Katharina","surname":"Najib","schoolClass":"HÖH222","wishList":[{"compId":19,"timeSlot":""},{"compId":14,"timeSlot":""},{"compId":18,"timeSlot":""},{"compId":10,"timeSlot":""},{"compId":16,"timeSlot":""},{"compId":4,"timeSlot":""}]},{"prename":"Aisha","surname":"Rana","schoolClass":"HÖH222","wishList":[{"compId":2,"timeSlot":""},{"compId":27,"timeSlot":""},{"compId":3,"timeSlot":""},{"compId":8,"timeSlot":""},{"compId":7,"timeSlot":""},{"compId":9,"timeSlot":""}]},{"prename":"Nehir Zehra","surname":"Sarigü","schoolClass":"HÖH222","wishList":[{"compId":18,"timeSlot":""},{"compId":19,"timeSlot":""},{"compId":21,"timeSlot":""},{"compId":4,"timeSlot":""},{"compId":20,"timeSlot":""},{"compId":10,"timeSlot":""}]},{"prename":"Alina","surname":"Selimbasic","schoolClass":"HÖH222","wishList":[{"compId":19,"timeSlot":""},{"compId":18,"timeSlot":""},{"compId":16,"timeSlot":""},{"compId":6,"timeSlot":""},{"compId":14,"timeSlot":""},{"compId":3,"timeSlot":""}]},{"prename":"Taha","surname":"Sweiti","schoolClass":"HÖH222","wishList":[{"compId":6,"timeSlot":""},{"compId":19,"timeSlot":""},{"compId":20,"timeSlot":""},{"compId":15,"timeSlot":""},{"compId":3,"timeSlot":""},{"compId":14,"timeSlot":""}]},{"prename":"Bela Maximilian","surname":"Urbanke","schoolClass":"HÖH222","wishList":[{"compId":27,"timeSlot":""},{"compId":4,"timeSlot":""},{"compId":7,"timeSlot":""},{"compId":12,"timeSlot":""},{"compId":14,"timeSlot":""},{"compId":13,"timeSlot":""}]},{"prename":"Oluwaseyi Kehinde","surname":"Adeosun","schoolClass":"HÖH223","wishList":[{"compId":2,"timeSlot":""},{"compId":19,"timeSlot":""},{"compId":24,"timeSlot":""},{"compId":23,"timeSlot":""},{"compId":27,"timeSlot":""},{"compId":1,"timeSlot":""}]},{"prename":"Angelina","surname":"Adolf","schoolClass":"HÖH223","wishList":[{"compId":3,"timeSlot":""},{"compId":6,"timeSlot":""},{"compId":1,"timeSlot":""},{"compId":10,"timeSlot":""},{"compId":15,"timeSlot":""},{"compId":9,"timeSlot":""}]},{"prename":"Lilian","surname":"Ali","schoolClass":"HÖH223","wishList":[{"compId":6,"timeSlot":""},{"compId":10,"timeSlot":""},{"compId":11,"timeSlot":""},{"compId":2,"timeSlot":""},{"compId":27,"timeSlot":""},{"compId":1,"timeSlot":""}]},{"prename":"Catalin-Gabriel","surname":"Ana","schoolClass":"HÖH223","wishList":[{"compId":6,"timeSlot":""},{"compId":3,"timeSlot":""},{"compId":27,"timeSlot":""},{"compId":15,"timeSlot":""},{"compId":13,"timeSlot":""},{"compId":7,"timeSlot":""}]},{"prename":"Zanya","surname":"Aygün","schoolClass":"HÖH223","wishList":[{"compId":10,"timeSlot":""},{"compId":11,"timeSlot":""},{"compId":13,"timeSlot":""},{"compId":2,"timeSlot":""},{"compId":27,"timeSlot":""},{"compId":1,"timeSlot":""}]},{"prename":"Edlisa Gymifua","surname":"Bediako","schoolClass":"HÖH223","wishList":[{"compId":10,"timeSlot":""},{"compId":11,"timeSlot":""},{"compId":9,"timeSlot":""},{"compId":3,"timeSlot":""},{"compId":13,"timeSlot":""},{"compId":6,"timeSlot":""}]},{"prename":"Ahmet Hezdar","surname":"Demir","schoolClass":"HÖH223","wishList":[{"compId":10,"timeSlot":""},{"compId":9,"timeSlot":""},{"compId":11,"timeSlot":""},{"compId":14,"timeSlot":""},{"compId":7,"timeSlot":""},{"compId":13,"timeSlot":""}]},{"prename":"Khalil","surname":"Dirki","schoolClass":"HÖH223","wishList":[{"compId":2,"timeSlot":""},{"compId":4,"timeSlot":""},{"compId":13,"timeSlot":""},{"compId":25,"timeSlot":""},{"compId":26,"timeSlot":""},{"compId":27,"timeSlot":""}]},{"prename":"Anouar","surname":"Dohri","schoolClass":"HÖH223","wishList":[{"compId":26,"timeSlot":""},{"compId":14,"timeSlot":""},{"compId":19,"timeSlot":""},{"compId":18,"timeSlot":""},{"compId":22,"timeSlot":""},{"compId":8,"timeSlot":""}]},{"prename":"Quincy","surname":"Ediawe Agunbiade","schoolClass":"HÖH223","wishList":[{"compId":19,"timeSlot":""},{"compId":3,"timeSlot":""},{"compId":1,"timeSlot":""},{"compId":6,"timeSlot":""},{"compId":7,"timeSlot":""},{"compId":14,"timeSlot":""}]},{"prename":"Jihan","surname":"El Sayed","schoolClass":"HÖH223","wishList":[{"compId":25,"timeSlot":""},{"compId":19,"timeSlot":""},{"compId":18,"timeSlot":""},{"compId":22,"timeSlot":""},{"compId":21,"timeSlot":""},{"compId":13,"timeSlot":""}]},{"prename":"Oleksandra","surname":"Glazkova","schoolClass":"HÖH223","wishList":[{"compId":9,"timeSlot":""},{"compId":19,"timeSlot":""},{"compId":18,"timeSlot":""},{"compId":17,"timeSlot":""},{"compId":15,"timeSlot":""},{"compId":4,"timeSlot":""}]},{"prename":"Ela Nur","surname":"GÖcesin","schoolClass":"HÖH223","wishList":[{"compId":9,"timeSlot":""},{"compId":10,"timeSlot":""},{"compId":11,"timeSlot":""},{"compId":3,"timeSlot":""},{"compId":13,"timeSlot":""},{"compId":12,"timeSlot":""}]},{"prename":"Anna","surname":"Hampeter","schoolClass":"HÖH223","wishList":[{"compId":3,"timeSlot":""},{"compId":1,"timeSlot":""},{"compId":27,"timeSlot":""},{"compId":2,"timeSlot":""},{"compId":7,"timeSlot":""},{"compId":8,"timeSlot":""}]},{"prename":"Hawin","surname":"Kisoglu","schoolClass":"HÖH223","wishList":[{"compId":1,"timeSlot":""},{"compId":19,"timeSlot":""},{"compId":3,"timeSlot":""},{"compId":20,"timeSlot":""},{"compId":27,"timeSlot":""},{"compId":2,"timeSlot":""}]},{"prename":"Rojin","surname":"Kisoglu","schoolClass":"HÖH223","wishList":[{"compId":2,"timeSlot":""},{"compId":6,"timeSlot":""},{"compId":9,"timeSlot":""},{"compId":10,"timeSlot":""},{"compId":1,"timeSlot":""},{"compId":2,"timeSlot":""}]},{"prename":"Bryan","surname":"Malambu","schoolClass":"HÖH223","wishList":[{"compId":17,"timeSlot":""},{"compId":18,"timeSlot":""},{"compId":19,"timeSlot":""},{"compId":16,"timeSlot":""},{"compId":15,"timeSlot":""},{"compId":14,"timeSlot":""}]},{"prename":"Tom","surname":"Mohren","schoolClass":"HÖH223","wishList":[{"compId":7,"timeSlot":""},{"compId":18,"timeSlot":""},{"compId":14,"timeSlot":""},{"compId":19,"timeSlot":""},{"compId":12,"timeSlot":""},{"compId":13,"timeSlot":""}]},{"prename":"Arman","surname":"Rozafshan","schoolClass":"HÖH223","wishList":[{"compId":7,"timeSlot":""},{"compId":22,"timeSlot":""},{"compId":25,"timeSlot":""},{"compId":26,"timeSlot":""},{"compId":3,"timeSlot":""},{"compId":20,"timeSlot":""}]},{"prename":"Anton Wilem","surname":"Rumor","schoolClass":"HÖH223","wishList":[{"compId":17,"timeSlot":""},{"compId":18,"timeSlot":""},{"compId":19,"timeSlot":""},{"compId":16,"timeSlot":""},{"compId":15,"timeSlot":""},{"compId":4,"timeSlot":""}]},{"prename":"Omer","surname":"Selim","schoolClass":"HÖH223","wishList":[{"compId":10,"timeSlot":""},{"compId":11,"timeSlot":""},{"compId":25,"timeSlot":""},{"compId":26,"timeSlot":""},{"compId":24,"timeSlot":""}]},{"prename":"Clotilde","surname":"Tchimbalanga","schoolClass":"HÖH223","wishList":[{"compId":10,"timeSlot":""},{"compId":17,"timeSlot":""},{"compId":18,"timeSlot":""},{"compId":16,"timeSlot":""},{"compId":9,"timeSlot":""},{"compId":11,"timeSlot":""}]},{"prename":"Ilyas","surname":"Tetik","schoolClass":"HÖH223","wishList":[{"compId":10,"timeSlot":""},{"compId":18,"timeSlot":""},{"compId":14,"timeSlot":""},{"compId":12,"timeSlot":""},{"compId":7,"timeSlot":""},{"compId":6,"timeSlot":""}]}],"errorMessage":"null"}
#compaies
#json2:dict={"company":[{"id":1,"compName":"Zentis","trainingOccupation":"Industriekaufleute","meeting":[{"timeSlot":"A","room":"null"},{"timeSlot":"B","room":"null"},{"timeSlot":"C","room":"null"},{"timeSlot":"D","room":"null"},{"timeSlot":"E","room":"null"}],"numberOfMembers":20},{"id":2,"compName":"Babor Kosmetik ","trainingOccupation":"Industriekaufleute","meeting":[{"timeSlot":"A","room":"null"},{"timeSlot":"B","room":"null"},{"timeSlot":"C","room":"null"},{"timeSlot":"D","room":"null"},{"timeSlot":"E","room":"null"}],"numberOfMembers":20},{"id":3,"compName":"EVA (Stawag, RegioIt, Aseag..)","trainingOccupation":"Industriekaufleute","meeting":[{"timeSlot":"A","room":"null"},{"timeSlot":"B","room":"null"},{"timeSlot":"C","room":"null"},{"timeSlot":"D","room":"null"},{"timeSlot":"E","room":"null"}],"numberOfMembers":20},{"id":4,"compName":"Grünenthal","trainingOccupation":"Industriekaufleute, BWL Plus (Industriekfm. Plus BWL-Studium), Kaufleute für Büromanagement                                  ","meeting":[{"timeSlot":"A","room":"null"},{"timeSlot":"B","room":"null"},{"timeSlot":"C","room":"null"},{"timeSlot":"D","room":"null"},{"timeSlot":"E","room":"null"}],"numberOfMembers":20},{"id":5,"compName":"RWTH Aachen","trainingOccupation":"Kaufleute für Büromanagement","meeting":[{"timeSlot":"A","room":"null"},{"timeSlot":"B","room":"null"},{"timeSlot":"C","room":"null"},{"timeSlot":"D","room":"null"},{"timeSlot":"E","room":"null"}],"numberOfMembers":20},{"id":6,"compName":"Aldi ","trainingOccupation":"Einzelhandelskaufleute","meeting":[{"timeSlot":"A","room":"null"},{"timeSlot":"B","room":"null"},{"timeSlot":"C","room":"null"},{"timeSlot":"D","room":"null"},{"timeSlot":"E","room":"null"}],"numberOfMembers":20},{"id":7,"compName":"Bauhaus","trainingOccupation":"Einzelhandelskaufleute, Handelsfachwirte, Duales Studium","meeting":[{"timeSlot":"A","room":"null"},{"timeSlot":"B","room":"null"},{"timeSlot":"C","room":"null"},{"timeSlot":"D","room":"null"},{"timeSlot":"E","room":"null"}],"numberOfMembers":20},{"id":8,"compName":"Sparkasse Aachen ","trainingOccupation":"Bankkaufleute","meeting":[{"timeSlot":"A","room":"null"},{"timeSlot":"B","room":"null"},{"timeSlot":"C","room":"null"},{"timeSlot":"D","room":"null"},{"timeSlot":"E","room":"null"}],"numberOfMembers":20},{"id":9,"compName":"Aachener Bank ","trainingOccupation":"Bankkaufleute","meeting":[{"timeSlot":"A","room":"null"},{"timeSlot":"B","room":"null"},{"timeSlot":"C","room":"null"},{"timeSlot":"D","room":"null"},{"timeSlot":"E","room":"null"}],"numberOfMembers":20},{"id":10,"compName":"Debeka","trainingOccupation":"Kaufleute für Versicherungen und Finanzen ","meeting":[{"timeSlot":"A","room":"null"},{"timeSlot":"B","room":"null"},{"timeSlot":"C","room":"null"},{"timeSlot":"D","room":"null"},{"timeSlot":"E","room":"null"}],"numberOfMembers":20},{"id":11,"compName":"Steuerberaterkammer Köln ","trainingOccupation":"Steuerfachangestellte","meeting":[{"timeSlot":"A","room":"null"},{"timeSlot":"B","room":"null"},{"timeSlot":"C","room":"null"},{"timeSlot":"D","room":"null"},{"timeSlot":"E","room":"null"}],"numberOfMembers":20},{"id":12,"compName":"Rechtsanwaltberufe","trainingOccupation":"Rechtsanwaltsfachangestellte","meeting":[{"timeSlot":"A","room":"null"},{"timeSlot":"B","room":"null"},{"timeSlot":"C","room":"null"},{"timeSlot":"D","room":"null"},{"timeSlot":"E","room":"null"}],"numberOfMembers":20},{"id":13,"compName":"Notarberufe","trainingOccupation":"Notarfachangestellte","meeting":[{"timeSlot":"A","room":"null"},{"timeSlot":"B","room":"null"},{"timeSlot":"C","room":"null"},{"timeSlot":"D","room":"null"},{"timeSlot":"E","room":"null"}],"numberOfMembers":20},{"id":14,"compName":"Spedition Hammer","trainingOccupation":"Kaufleute für Spedition und Lagerlogistik, Kaufleute für Büromanagement                         ","meeting":[{"timeSlot":"A","room":"null"},{"timeSlot":"B","room":"null"},{"timeSlot":"C","room":"null"},{"timeSlot":"D","room":"null"},{"timeSlot":"E","room":"null"}],"numberOfMembers":20},{"id":15,"compName":"Inform","trainingOccupation":"Kaufmann/-frau für Büromanagement ","meeting":[{"timeSlot":"A","room":"null"},{"timeSlot":"B","room":"null"},{"timeSlot":"C","room":"null"},{"timeSlot":"D","room":"null"},{"timeSlot":"E","room":"null"}],"numberOfMembers":20},{"id":16,"compName":"Inform","trainingOccupation":"Duales Studium Wirtschaftsinformatik ","meeting":[{"timeSlot":"A","room":"null"},{"timeSlot":"B","room":"null"},{"timeSlot":"C","room":"null"},{"timeSlot":"D","room":"null"},{"timeSlot":"E","room":"null"}],"numberOfMembers":20},{"id":17,"compName":"StädteRegion Aachen ","trainingOccupation":"Verwaltungsfachangestellte und Duales Studium Bachelor of Laws/Arts","meeting":[{"timeSlot":"A","room":"null"},{"timeSlot":"B","room":"null"},{"timeSlot":"C","room":"null"},{"timeSlot":"D","room":"null"},{"timeSlot":"E","room":"null"}],"numberOfMembers":20},{"id":18,"compName":"Finanzamt","trainingOccupation":"duales Studium Dipl. Finanzwirt/-in ","meeting":[{"timeSlot":"A","room":"null"},{"timeSlot":"B","room":"null"},{"timeSlot":"C","room":"null"},{"timeSlot":"D","room":"null"},{"timeSlot":"E","room":"null"}],"numberOfMembers":20},{"id":19,"compName":"Finanzamt ","trainingOccupation":"Ausbildung Finanzwirt/-in ","meeting":[{"timeSlot":"A","room":"null"},{"timeSlot":"B","room":"null"},{"timeSlot":"C","room":"null"},{"timeSlot":"D","room":"null"},{"timeSlot":"E","room":"null"}],"numberOfMembers":20},{"id":20,"compName":"Justizvollzugsanstalt","trainingOccupation":"Beamter im allgemeinen Vollzugsdienst, Dipl-Verwaltungswirt (FH)","meeting":[{"timeSlot":"A","room":"null"},{"timeSlot":"B","room":"null"},{"timeSlot":"C","room":"null"},{"timeSlot":"D","room":"null"},{"timeSlot":"E","room":"null"}],"numberOfMembers":20},{"id":21,"compName":"Zoll Aachen","trainingOccupation":"Beamter im mittleren und gehobenen Dienst ","meeting":[{"timeSlot":"A","room":"null"},{"timeSlot":"B","room":"null"},{"timeSlot":"C","room":"null"},{"timeSlot":"D","room":"null"},{"timeSlot":"E","room":"null"}],"numberOfMembers":20},{"id":22,"compName":"Polizei","trainingOccupation":"Polizeikommisar*in ","meeting":[{"timeSlot":"A","room":"null"},{"timeSlot":"B","room":"null"},{"timeSlot":"C","room":"null"},{"timeSlot":"D","room":"null"},{"timeSlot":"E","room":"null"}],"numberOfMembers":25},{"id":23,"compName":"FH Aachen - Studienberatung","trainingOccupation":"","meeting":[{"timeSlot":"A","room":"null"},{"timeSlot":"B","room":"null"},{"timeSlot":"C","room":"null"},{"timeSlot":"D","room":"null"},{"timeSlot":"E","room":"null"}],"numberOfMembers":20},{"id":24,"compName":"RWTH Aachen - Studienberatung","trainingOccupation":"Hinweis: Studium hier nur mit Abitur möglich","meeting":[{"timeSlot":"A","room":"null"},{"timeSlot":"B","room":"null"},{"timeSlot":"C","room":"null"},{"timeSlot":"D","room":"null"},{"timeSlot":"E","room":"null"}],"numberOfMembers":20},{"id":25,"compName":"Wirtschaftsrecht FH-Aachen","trainingOccupation":"","meeting":[{"timeSlot":"A","room":"null"},{"timeSlot":"B","room":"null"},{"timeSlot":"C","room":"null"},{"timeSlot":"D","room":"null"},{"timeSlot":"E","room":"null"}],"numberOfMembers":20},{"id":26,"compName":"Soziale Arbeit ","trainingOccupation":"","meeting":[{"timeSlot":"A","room":"null"},{"timeSlot":"B","room":"null"},{"timeSlot":"C","room":"null"},{"timeSlot":"D","room":"null"},{"timeSlot":"E","room":"null"}],"numberOfMembers":20},{"id":27,"compName":"Lehramt Berufskolleg","trainingOccupation":"","meeting":[{"timeSlot":"A","room":"null"},{"timeSlot":"B","room":"null"},{"timeSlot":"C","room":"null"},{"timeSlot":"D","room":"null"},{"timeSlot":"E","room":"null"}],"numberOfMembers":20}],"errorMessage":"null"}
start = Transform(response.json(),response2.json(),response3.json())
