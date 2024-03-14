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
            line = line + participant.__prename__ + " | " + participant.__surname__ + " | " + str(participant.__schoolClass__) + "\n"
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
                wish = ConcreatWish(student, prio + 1, student.__wishList__[prio].getCompID())
                concreateWishlist.append(wish)
            for event in self.__eventlist__:
                eventid = event.__eventid__
                temp_particepent_list = list()
                for element in event.__participantlist__:
                    temp_particepent_list.append(element)
                for element in concreateWishlist:
                    suffused = element.__studnet__.__wishList__[element.__prio__ - 1].getsuffused()
                    wishID = element.get_wish_id()
                    temp_togolist_forStudnets = list()
                    for togoevent in student.__toGolist__:
                        temp_togolist_forStudnets.append(togoevent)
                    if eventid == wishID and suffused == False:
                        temp_particepent_list.append(element.__studnet__)
                        element.__studnet__.__wishList__[element.__prio__ - 1].setsuffused_true()
                        temp_togolist_forStudnets.append(event)
                event.__participantlist__ = temp_particepent_list
                temp_togolist_forStudnets.append(event)
                element.__studnet__.__toGolist__ = temp_togolist_forStudnets
        print(" ")

    def createTimeplanforStudents(self):
        perfixfilename = "Laufzettel_für_den_Schueler_ "
        postfixfilename = "_Klasse_"
        for stundent in self.__studentList__:
            filename = perfixfilename + stundent.__surname__ + "_" + stundent.__prename__ + postfixfilename + str(stundent.__schoolClass__)
            headline = "Schueler: " + stundent.__surname__ + " , " + stundent.__prename__ + " Klasse: " + str(stundent.__schoolClass__) +"\n"
            tempgolist = stundent.__toGolist__
            eventlist= list()
            eventString = ""
            for event in tempgolist:
                eventString = eventString+ "Zeitpunkt " +event.__timeslot__ + " Veranstalltung: " +event.__company_name__+ "Thema: " +event.__event_topic__ +"in Raum: "+ str(event.__room__) +"\n"
                eventlist.append(eventlist)
            #with open("C:/Users/nilsw/PycharmProjects/BWV-BOT/Transformation/trahdata/"+filename+".txt", 'w') as file:
            #    file.writelines(headline)
            #    for line in eventlist:
            #        file.writelines(str(line))
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
        #import json
        #data = json.load(jsonfile)
        #for student_data in data['Stundent']:
        #    prename = student_data['vorname']
        #    surname = student_data['nachname']
        #    wishlist = student_data['wuensche']
        #    schoolclass = student_data['klasse']
        #    student = Student(prename, surname, schoolclass, wishlist)
        #    self.__stundentList__.append(student)

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

        #import json
        #data = json.load(jsonfile)
        #for company_data in data['companies']:
        #    id = company_data['id']
        #    compname = company_data['compName']
        #    toc = company_data['trainingOccupation']
        #    capacity = company_data['capacity']
        #    meeting = company_data['meeting']
        #    company = Company(id, compname, toc, meeting)
        #    self.__companyList__.append(company)
        #{'student': [{'prename': 'Tyler', 'surname': 'Meyer', 'schoolClass': 'LightBlue4', 'wishList': []}, {'prename': 'Joseph', 'surname': 'Chapman', 'schoolClass': 'LightBlue3', 'wishList': []}, {'prename': 'Jesse', 'surname': 'Anderson', 'schoolClass': 'Gray4', 'wishList': []}, {'prename': 'Aaron', 'surname': 'Cruz', 'schoolClass': 'Gray3', 'wishList': []}, {'prename': 'Gregory', 'surname': 'Phillips', 'schoolClass': 'Wheat5', 'wishList': []}, {'prename': 'Christy', 'surname': 'Smith', 'schoolClass': 'Aqua5', 'wishList': []}, {'prename': 'Mario', 'surname': 'Mason', 'schoolClass': 'Aqua5', 'wishList': []}, {'prename': 'Paul', 'surname': 'Evans', 'schoolClass': 'Aqua4', 'wishList': []}, {'prename': 'Alicia', 'surname': 'Warner', 'schoolClass': 'Aqua4', 'wishList': []}, {'prename': 'Amber', 'surname': 'Marks', 'schoolClass': 'SkyBlue3', 'wishList': []}, {'prename': 'Michael', 'surname': 'Vaughan', 'schoolClass': 'MintCream3', 'wishList': []}, {'prename': 'Regina', 'surname': 'Murillo', 'schoolClass': 'DarkTurquoise4', 'wishList': []}, {'prename': 'Chloe', 'surname': 'Stone', 'schoolClass': 'DarkTurquoise5', 'wishList': []}, {'prename': 'Brenda', 'surname': 'Beard', 'schoolClass': 'DarkOrange5', 'wishList': []}, {'prename': 'Sean', 'surname': 'Wallae', 'schoolClass': 'PeachPuff4', 'wishList': []}, {'prename': 'Roy', 'surname': 'Li', 'schoolClass': 'PeachPuff5', 'wishList': []}, {'prename': 'Michelle', 'surname': 'Bowman', 'schoolClass': 'LightYellow4', 'wishList': []}, {'prename': 'Nicholas', 'surname': 'Brown', 'schoolClass': 'LightYellow4', 'wishList': []}, {'prename': 'Wendy', 'surname': 'Pety', 'schoolClass': 'DarkOliveGreen4', 'wishList': []}, {'prename': 'Gary', 'surname': 'Hansen', 'schoolClass': 'DodgerBlue3', 'wishList': []}, {'prename': 'Olivia', 'surname': 'Daniels', 'schoolClass': 'DodgerBlue3', 'wishList': []}, {'prename': 'Jonathan', 'surname': 'Gibbs', 'schoolClass': 'MidnightBlue5', 'wishList': []}, {'prename': 'Lisa', 'surname': 'Lee', 'schoolClass': 'Olive5', 'wishList': []}, {'prename': 'Dorothy', 'surname': 'Rich', 'schoolClass': 'OldLace5', 'wishList': []}, {'prename': 'Kelly', 'surname': 'Pearson', 'schoolClass': 'MidnightBlue4', 'wishList': []}, {'prename': 'William', 'surname': 'Cervantes', 'schoolClass': 'MidnightBlue4', 'wishList': []}, {'prename': 'Karen', 'surname': 'Lambert', 'schoolClass': 'PaleGreen3', 'wishList': []}, {'prename': 'Daniel', 'surname': 'Wells', 'schoolClass': 'Olive3', 'wishList': []}, {'prename': 'Xavier', 'surname': 'Murray', 'schoolClass': 'OldLace3', 'wishList': []}, {'prename': 'Jennifer', 'surname': 'Davidson', 'schoolClass': 'White3', 'wishList': []}, {'prename': 'James', 'surname': 'Ramirez', 'schoolClass': 'White3', 'wishList': []}, {'prename': 'Benjamin', 'surname': 'Williams', 'schoolClass': 'White5', 'wishList': []}, {'prename': 'Thomas', 'surname': 'Hogan', 'schoolClass': 'White5', 'wishList': []}, {'prename': 'Jake', 'surname': 'Hobbs', 'schoolClass': 'Green3', 'wishList': []}, {'prename': 'Tiffany', 'surname': 'Shepard', 'schoolClass': 'Blue4', 'wishList': []}, {'prename': 'Abigail', 'surname': 'Miller', 'schoolClass': 'Green5', 'wishList': []}, {'prename': 'Samantha', 'surname': 'Cruz', 'schoolClass': 'LawnGreen4', 'wishList': []}, {'prename': 'Cody', 'surname': 'Sexton', 'schoolClass': 'PaleGreen5', 'wishList': []}, {'prename': 'Jennifer', 'surname': 'Tucker', 'schoolClass': 'Linen5', 'wishList': []}, {'prename': 'Christopher', 'surname': 'Dyer', 'schoolClass': 'Snow4', 'wishList': []}, {'prename': 'Alex', 'surname': 'Cook', 'schoolClass': 'Snow3', 'wishList': []}, {'prename': 'Richard', 'surname': 'Marshall', 'schoolClass': 'MediumTurquoise3', 'wishList': []}, {'prename': 'Alex', 'surname': 'Aguirre', 'schoolClass': 'DeepPink3', 'wishList': []}, {'prename': 'Ryan', 'surname': 'Johnson', 'schoolClass': 'SeaGreen5', 'wishList': []}, {'prename': 'Brandon', 'surname': 'Wilson', 'schoolClass': 'SeaGreen5', 'wishList': []}, {'prename': 'Nicholas', 'surname': 'Alvarado', 'schoolClass': 'DarkSlateGray4', 'wishList': []}, {'prename': 'Ricky', 'surname': 'Nelson', 'schoolClass': 'DarkSlateGray5', 'wishList': []}, {'prename': 'Casey', 'surname': 'Miller', 'schoolClass': 'DarkSeaGreen5', 'wishList': []}, {'prename': 'Renee', 'surname': 'Myers', 'schoolClass': 'DarkGreen3', 'wishList': []}, {'prename': 'Tammy', 'surname': 'Glenn', 'schoolClass': 'DarkGreen4', 'wishList': []}, {'prename': 'Ivan', 'surname': 'Porter', 'schoolClass': 'LightSeaGreen5', 'wishList': []}, {'prename': 'Catherine', 'surname': 'Walker', 'schoolClass': 'FloralWhite3', 'wishList': []}, {'prename': 'Debra', 'surname': 'Jenkins', 'schoolClass': 'FloralWhite3', 'wishList': []}, {'prename': 'Cassandra', 'surname': 'Johnson', 'schoolClass': 'Aquamarine3', 'wishList': []}, {'prename': 'Michelle', 'surname': 'Sampson', 'schoolClass': 'Aquamarine3', 'wishList': []}, {'prename': 'John', 'surname': 'Campbell', 'schoolClass': 'Silver5', 'wishList': []}, {'prename': 'John', 'surname': 'Dickerson', 'schoolClass': 'DarkBlue5', 'wishList': []}, {'prename': 'Melissa', 'surname': 'Ford', 'schoolClass': 'DarkBlue5', 'wishList': []}, {'prename': 'Katherine', 'surname': 'Munoz', 'schoolClass': 'YellowGreen4', 'wishList': []}, {'prename': 'Kelly', 'surname': 'Parks', 'schoolClass': 'YellowGreen3', 'wishList': []}, {'prename': 'Heather', 'surname': 'Mason', 'schoolClass': 'WhiteSmoke4', 'wishList': []}, {'prename': 'Richard', 'surname': 'Carr', 'schoolClass': 'WhiteSmoke5', 'wishList': []}, {'prename': 'Eric', 'surname': 'Anderson', 'schoolClass': 'YellowGreen5', 'wishList': []}, {'prename': 'Amy', 'surname': 'Cook', 'schoolClass': 'Silver3', 'wishList': []}, {'prename': 'Claudia', 'surname': 'Jenkins', 'schoolClass': 'Navy3', 'wishList': []}, {'prename': 'James', 'surname': 'Olsen', 'schoolClass': 'Navy3', 'wishList': []}, {'prename': 'Troy', 'surname': 'Henderson', 'schoolClass': 'Navy3', 'wishList': []}, {'prename': 'Kenneth', 'surname': 'Li', 'schoolClass': 'RosyBrown3', 'wishList': []}, {'prename': 'Sydney', 'surname': 'Ayala', 'schoolClass': 'Navy5', 'wishList': []}, {'prename': 'Lauren', 'surname': 'Brown', 'schoolClass': 'RosyBrown4', 'wishList': []}, {'prename': 'Crystal', 'surname': 'Rivera', 'schoolClass': 'Navy4', 'wishList': []}, {'prename': 'Kevin', 'surname': 'Bradley', 'schoolClass': 'HoneyDew5', 'wishList': []}, {'prename': 'Eric', 'surname': 'Chaney', 'schoolClass': 'Tomato4', 'wishList': []}, {'prename': 'Heather', 'surname': 'Murray', 'schoolClass': 'DarkSalmon5', 'wishList': []}, {'prename': 'Destiny', 'surname': 'Myers', 'schoolClass': 'MediumBlue3', 'wishList': []}, {'prename': 'Adrienne', 'surname': 'Mendoza', 'schoolClass': 'Turquoise5', 'wishList': []}, {'prename': 'Crystal', 'surname': 'Johnson', 'schoolClass': 'Turquoise5', 'wishList': []}, {'prename': 'William', 'surname': 'Arnold', 'schoolClass': 'Bisque3', 'wishList': []}, {'prename': 'Jimmy', 'surname': 'Lowery', 'schoolClass': 'Khaki5', 'wishList': []}, {'prename': 'Daniel', 'surname': 'Contreras', 'schoolClass': 'SpringGreen5', 'wishList': []}, {'prename': 'Emily', 'surname': 'Thompson', 'schoolClass': 'DarkKhaki3', 'wishList': []}, {'prename': 'Tanya', 'surname': 'Carr', 'schoolClass': 'DarkSalmon3', 'wishList': []}, {'prename': 'Christine', 'surname': 'Hogan', 'schoolClass': 'BlanchedAlmond3', 'wishList': []}, {'prename': 'Sandra', 'surname': 'Coleman', 'schoolClass': 'BlanchedAlmond3', 'wishList': []}, {'prename': 'Tina', 'surname': 'Davidson', 'schoolClass': 'PaleGoldenRod3', 'wishList': []}, {'prename': 'Joseph', 'surname': 'Hill', 'schoolClass': 'DarkKhaki4', 'wishList': []}, {'prename': 'Shannon', 'surname': 'Johnson', 'schoolClass': 'BlanchedAlmond4', 'wishList': []}, {'prename': 'Jeffrey', 'surname': 'Atkins', 'schoolClass': 'Lime5', 'wishList': []}, {'prename': 'Danielle', 'surname': 'Bray', 'schoolClass': 'GreenYellow5', 'wishList': []}, {'prename': 'Scott', 'surname': 'Case', 'schoolClass': 'GreenYellow5', 'wishList': []}, {'prename': 'Jeffery', 'surname': 'Hernandez', 'schoolClass': 'LightGoldenRodYellow3', 'wishList': []}, {'prename': 'Tracy', 'surname': 'Smith', 'schoolClass': 'LightGoldenRodYellow3', 'wishList': []}, {'prename': 'Matthew', 'surname': 'Valenzuela', 'schoolClass': 'LightGoldenRodYellow3', 'wishList': []}, {'prename': 'Lance', 'surname': 'Dudley', 'schoolClass': 'GreenYellow4', 'wishList': []}, {'prename': 'Kevin', 'surname': 'Jimenez', 'schoolClass': 'Thistle5', 'wishList': []}, {'prename': 'Jimmy', 'surname': 'Martin', 'schoolClass': 'PowderBlue4', 'wishList': []}, {'prename': 'Joseph', 'surname': 'Brooks', 'schoolClass': 'DarkGray5', 'wishList': []}, {'prename': 'Robert', 'surname': 'Chan', 'schoolClass': 'Thistle4', 'wishList': []}, {'prename': 'Erik', 'surname': 'Williams', 'schoolClass': 'Black5', 'wishList': []}, {'prename': 'Elizabeth', 'surname': 'Williams', 'schoolClass': 'MediumPurple5', 'wishList': []}, {'prename': 'Brandon', 'surname': 'Adams', 'schoolClass': 'Black3', 'wishList': []}, {'prename': 'James', 'surname': 'Shepherd', 'schoolClass': 'Indigo4', 'wishList': []}, {'prename': 'Courtney', 'surname': 'Cooley', 'schoolClass': 'NavajoWhite3', 'wishList': []}, {'prename': 'Shannon', 'surname': 'Johnson', 'schoolClass': 'NavajoWhite3', 'wishList': []}, {'prename': 'Anna', 'surname': 'Jacobs', 'schoolClass': 'AliceBlue5', 'wishList': []}, {'prename': 'Andrea', 'surname': 'Bates', 'schoolClass': 'MediumPurple3', 'wishList': []}, {'prename': 'Jillian', 'surname': 'Wilkins', 'schoolClass': 'Peru3', 'wishList': []}, {'prename': 'Laura', 'surname': 'Martinez', 'schoolClass': 'Ivory3', 'wishList': []}, {'prename': 'Angelica', 'surname': 'Robertson', 'schoolClass': 'Ivory3', 'wishList': []}, {'prename': 'Dustin', 'surname': 'Booth', 'schoolClass': 'Beige3', 'wishList': []}, {'prename': 'Brooke', 'surname': 'Mccarty', 'schoolClass': 'LightGoldenRodYellow5', 'wishList': []}, {'prename': 'Vicki', 'surname': 'Chavez', 'schoolClass': 'Indigo3', 'wishList': []}, {'prename': 'Alexandra', 'surname': 'Sloan', 'schoolClass': 'Beige4', 'wishList': []}, {'prename': 'John', 'surname': 'Williams', 'schoolClass': 'GoldenRod4', 'wishList': []}, {'prename': 'Sherry', 'surname': 'Thomas', 'schoolClass': 'GoldenRod4', 'wishList': []}, {'prename': 'Debra', 'surname': 'Rhodes', 'schoolClass': 'Beige5', 'wishList': []}, {'prename': 'John', 'surname': 'Richards', 'schoolClass': 'LightSteelBlue3', 'wishList': []}, {'prename': 'Ana', 'surname': 'Scott', 'schoolClass': 'Plum4', 'wishList': []}, {'prename': 'Karen', 'surname': 'Randall', 'schoolClass': 'LightSteelBlue5', 'wishList': []}, {'prename': 'Kelly', 'surname': 'Lozano', 'schoolClass': 'LightSteelBlue5', 'wishList': []}, {'prename': 'Sandra', 'surname': 'Chase', 'schoolClass': 'Gainsboro5', 'wishList': []}, {'prename': 'Joshua', 'surname': 'Riley', 'schoolClass': 'SaddleBrown5', 'wishList': []}, {'prename': 'Richard', 'surname': 'Wallace', 'schoolClass': 'MediumSeaGreen3', 'wishList': []}, {'prename': 'Ana', 'surname': 'Osborn', 'schoolClass': 'LightPink5', 'wishList': []}, {'prename': 'Daniel', 'surname': 'Alvarado', 'schoolClass': 'Chocolate5', 'wishList': []}, {'prename': 'Tara', 'surname': 'King', 'schoolClass': 'Chocolate5', 'wishList': []}, {'prename': 'Donna', 'surname': 'Ibarra', 'schoolClass': 'ForestGreen3', 'wishList': []}, {'prename': 'Scott', 'surname': 'Stephenson', 'schoolClass': 'Yellow4', 'wishList': []}, {'prename': 'Heather', 'surname': 'Thompson', 'schoolClass': 'Gold5', 'wishList': []}, {'prename': 'Michael', 'surname': 'Lowery', 'schoolClass': 'MediumAquaMarine5', 'wishList': []}, {'prename': 'Sandra', 'surname': 'Brown', 'schoolClass': 'SteelBlue5', 'wishList': []}, {'prename': 'Richard', 'surname': 'Campbell', 'schoolClass': 'PapayaWhip3', 'wishList': []}, {'prename': 'Chad', 'surname': 'Hodge', 'schoolClass': 'PapayaWhip3', 'wishList': []}, {'prename': 'Jessica', 'surname': 'Scott', 'schoolClass': 'Magenta5', 'wishList': []}, {'prename': 'Sandra', 'surname': 'Washington', 'schoolClass': 'GhostWhite5', 'wishList': []}, {'prename': 'Kathleen', 'surname': 'Wright', 'schoolClass': 'GhostWhite3', 'wishList': []}, {'prename': 'Bryan', 'surname': 'Calderon', 'schoolClass': 'Magenta3', 'wishList': []}, {'prename': 'William', 'surname': 'Yoder', 'schoolClass': 'Cyan3', 'wishList': []}, {'prename': 'Daniel', 'surname': 'Lambert', 'schoolClass': 'LightCoral4', 'wishList': []}, {'prename': 'Arthur', 'surname': 'White', 'schoolClass': 'Orange4', 'wishList': []}, {'prename': 'Hector', 'surname': 'Blake', 'schoolClass': 'Orange4', 'wishList': []}, {'prename': 'David', 'surname': 'Smith', 'schoolClass': 'LightSkyBlue5', 'wishList': []}, {'prename': 'Sharon', 'surname': 'Short', 'schoolClass': 'OliveDrab5', 'wishList': []}, {'prename': 'Denise', 'surname': 'Goodman', 'schoolClass': 'LightCyan3', 'wishList': []}, {'prename': 'Sarah', 'surname': 'Goodman', 'schoolClass': 'DarkMagenta4', 'wishList': []}, {'prename': 'Jacob', 'surname': 'Wilson', 'schoolClass': 'Purple3', 'wishList': []}, {'prename': 'Steven', 'surname': 'Hernandez', 'schoolClass': 'DarkMagenta3', 'wishList': []}, {'prename': 'Donna', 'surname': 'Bishop', 'schoolClass': 'Brown4', 'wishList': []}, {'prename': 'Kelly', 'surname': 'Rodriguez', 'schoolClass': 'LightSlateGray5', 'wishList': []}, {'prename': 'Kathleen', 'surname': 'Rogers', 'schoolClass': 'LightSlateGray5', 'wishList': []}, {'prename': 'Corey', 'surname': 'Norris', 'schoolClass': 'LightCyan5', 'wishList': []}, {'prename': 'Paul', 'surname': 'Rodriguez', 'schoolClass': 'LightGray3', 'wishList': []}, {'prename': 'John', 'surname': 'Russo', 'schoolClass': 'LightGray5', 'wishList': []}, {'prename': 'Brenda', 'surname': 'Hurley', 'schoolClass': 'LightGreen5', 'wishList': []}, {'prename': 'Amanda', 'surname': 'George', 'schoolClass': 'LightGreen5', 'wishList': []}, {'prename': 'Jeffrey', 'surname': 'Herring', 'schoolClass': 'LimeGreen4', 'wishList': []}, {'prename': 'Barbara', 'surname': 'Zuniga', 'schoolClass': 'SeaShell3', 'wishList': []}, {'prename': 'John', 'surname': 'Montgomery', 'schoolClass': 'LightGreen3', 'wishList': []}, {'prename': 'George', 'surname': 'Martinez', 'schoolClass': 'LightGreen4', 'wishList': []}, {'prename': 'Teresa', 'surname': 'Howell', 'schoolClass': 'Coral5', 'wishList': []}, {'prename': 'Sara', 'surname': 'Bond', 'schoolClass': 'HotPink4', 'wishList': []}, {'prename': 'Anthony', 'surname': 'Morris', 'schoolClass': 'Maroon3', 'wishList': []}, {'prename': 'Austin', 'surname': 'Parker', 'schoolClass': 'DarkRed3', 'wishList': []}, {'prename': 'Gwendolyn', 'surname': 'Holloway', 'schoolClass': 'Orchid4', 'wishList': []}, {'prename': 'Renee', 'surname': 'Lewis', 'schoolClass': 'IndianRed4', 'wishList': []}, {'prename': 'Clayton', 'surname': 'Wilson', 'schoolClass': 'SlateGray4', 'wishList': []}, {'prename': 'Gloria', 'surname': 'Miller', 'schoolClass': 'LavenderBlush3', 'wishList': []}, {'prename': 'Donna', 'surname': 'Martinez', 'schoolClass': 'SlateGray5', 'wishList': []}, {'prename': 'Crystal', 'surname': 'Kelley', 'schoolClass': 'Cornsilk5', 'wishList': []}, {'prename': 'Benjamin', 'surname': 'Anderson', 'schoolClass': 'Cornsilk5', 'wishList': []}, {'prename': 'Christopher', 'surname': 'Taylor', 'schoolClass': 'DarkSlateBlue4', 'wishList': []}, {'prename': 'Alex', 'surname': 'Wise', 'schoolClass': 'DarkSlateBlue3', 'wishList': []}, {'prename': 'Phillip', 'surname': 'Reed', 'schoolClass': 'DimGray5', 'wishList': []}, {'prename': 'Connie', 'surname': 'Allen', 'schoolClass': 'Fuchsia4', 'wishList': []}, {'prename': 'Luke', 'surname': 'Mclaughlin', 'schoolClass': 'DarkCyan5', 'wishList': []}, {'prename': 'Eric', 'surname': 'Burns', 'schoolClass': 'Chartreuse3', 'wishList': []}, {'prename': 'Justin', 'surname': 'Ramos', 'schoolClass': 'Chartreuse3', 'wishList': []}, {'prename': 'Emily', 'surname': 'Miller', 'schoolClass': 'Cornsilk4', 'wishList': []}, {'prename': 'Joshua', 'surname': 'Freeman', 'schoolClass': 'DarkCyan4', 'wishList': []}, {'prename': 'Derek', 'surname': 'Ellison', 'schoolClass': 'MistyRose5', 'wishList': []}], 'errorMessage': None}

    def toString(self):
        for company in self.__companyList__:
            print(
                f"ID: {company.__id__}, Name: {company.__compName__}, Beruf: {company.__trainingOccupation__}, Kapazität: {company.__capacity__}, Timeslot:{company.__meeting__} ")
        print("\n")
        for student in self.__stundentList__:
            print(
                f"Vorname: {student.__prename__}, Nachname: {student.__surname__}, Wünsche: {student.wishliststring()}, Klasse: {student.__schoolClass__}")

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
