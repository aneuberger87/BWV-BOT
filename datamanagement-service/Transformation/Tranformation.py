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
    eventlist = list()
    __eventId__: int = 1

    def __init__(self, companylist, studnetlist):
        self.__companylist__ = companylist
        self.studentList = studnetlist
        self.filleventList()
        self.assign_studentstoEvents()
        self.handleEmptyclaculation()
        outputjson = self.togo_list_to_json(self.studentList)
        print("Python Json: ")
        print(outputjson)
        score:SolutionScore = self.clacscore()
        print(str(score.realScore))
        self.postStudents(outputjson)
        self.postScore(score)
    def handleEmptyclaculation(self):
        check = False
        for student in self.studentList:
            if len(student.toGolist) < 5:
                compidArray = []
                for event in student.toGolist:
                    compidArray.append(event.company_id)
                counter = len(student.toGolist)
                for counter in range(5):
                    print("counter: "+str(counter))
                    for event in self.eventlist:
                        if event.amountofmembers < 20 and str(event.timeslot) not in student.timeslots and event.company_id not in compidArray:
                            student.toGolist.append(event)
                            student.timeslots.append(event.timeslot)
                            compidArray.append(event.company_id)
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
                self.eventlist.append(event)
            self.__eventId__ = self.__eventId__ + 1
    def assign_studentstoEvents(self):
        concreateWishlist = list()
        prio = 0
        for prio in range(6):
            for student in self.studentList:
                wish = ConcreatWish(student, prio + 1, student.wishList[prio].getCompID())
                concreateWishlist.append(wish)
                for event in self.eventlist:
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
api_url = "http://localhost:8080"
response = requests.get(api_url+"/students")
response2 = requests.get(api_url+"/companies")

response3 = requests.get(api_url+"/rooms")
start = Transform(response.json(),response2.json(),response3.json())
