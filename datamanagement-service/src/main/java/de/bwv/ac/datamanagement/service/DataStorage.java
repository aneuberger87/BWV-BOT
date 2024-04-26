package de.bwv.ac.datamanagement.service;

import de.bwv.ac.datamanagement.data.CompaniesList;
import de.bwv.ac.datamanagement.data.RoomList;
import de.bwv.ac.datamanagement.data.SolutionScore;
import de.bwv.ac.datamanagement.data.StudentsList;
import de.bwv.ac.datamanagement.data.export.EventsAttendanceList;
import de.bwv.ac.datamanagement.data.export.TimetableList;
import de.bwv.ac.datamanagement.data.storage.StudentStorageDatamodel;
import lombok.Getter;
import lombok.Setter;
import lombok.extern.slf4j.Slf4j;

import java.util.*;
import java.util.function.Function;

@Slf4j
public class DataStorage {

    private final Map<Integer, CompaniesList.Company> companiesCache = new HashMap<>();
    private final Map<String, List<String>> studentsPerClass = new HashMap<>();
    private final Map<String, StudentStorageDatamodel> studentsMap = new HashMap<>();
    private final Map<String, RoomList.Room> roomMap = new HashMap<>();

    @Setter
    @Getter
    private SolutionScore realScore;


    public CompaniesList getCompaniesList() {
        CompaniesList result = new CompaniesList();
        if (companiesCache.isEmpty()) {
            result.setErrorMessage("Es wurden keine Veranstaltungen eingelesen. Entweder war die Datei leer/fehlerhaft oder es wurde noch keine Datei hochgeladen!");
            return result;
        }
        List<CompaniesList.Company> companies = new ArrayList<>();
        companiesCache.forEach((id, company) -> companies.add(company));
        result.setCompany(companies);
        return result;
    }

    public StudentsList getStudentsWishList() {
        StudentsList result = getStudentList(studentStorageDatamodel -> studentStorageDatamodel.getStudent().getWishList());
        if (result.getStudent().isEmpty()) {
            result.setErrorMessage("Es wurden keine Schüler eingelesen. Entweder war die Schüler-Datei leer/fehlerhaft oder es wurde noch keine Datei hochgeladen!");
        }
        return result;
    }

    public StudentsList getStudentsAllocationList() {
        StudentsList result = getStudentList(StudentStorageDatamodel::getAllocation);
        if (result.getStudent().isEmpty()) {
            result.setErrorMessage("Es wurde noch keine Zuteilung erstellt!");
        }
        return result;
    }

    private StudentsList getStudentList(Function<StudentStorageDatamodel, List<StudentsList.Wish>> wishListForStudent) {
        StudentsList result = new StudentsList();
        List<StudentsList.Student> studentList = new ArrayList<>();
        studentsPerClass.forEach((classId, studentIds) -> {
            for (String studentId : studentIds) {
                StudentStorageDatamodel studentStorageDatamodel = studentsMap.get(studentId);
                StudentsList.Student student = getStudent(studentStorageDatamodel, wishListForStudent.apply(studentStorageDatamodel));
                studentList.add(student);
            }
        });
        result.setStudent(studentList);
        return result;
    }


    private StudentsList.Student getStudent(StudentStorageDatamodel studentStorageDatamodel, List<StudentsList.Wish> wishList) {
        StudentsList.Student studentFromStorage = studentStorageDatamodel.getStudent();
        return new StudentsList.Student(studentFromStorage.getPrename(), studentFromStorage.getSurname(), studentFromStorage.getSchoolClass(), wishList);
    }

    public void setStudentsWishesList(StudentsList studentsList) {
        studentsMap.clear();
        realScore = null;
        studentsPerClass.clear();
        studentsList.getStudent().stream().filter(Objects::nonNull).forEach(this::addStudent);
    }

    private void addStudent(StudentsList.Student student) {
        String schoolClass = student.getSchoolClass();
        List<String> studentsInClass = studentsPerClass.getOrDefault(schoolClass, new ArrayList<>());
        String studentId = StudentStorageDatamodel.getId(student);
        studentsInClass.add(studentId.trim());
        studentsPerClass.put(schoolClass, studentsInClass);
        StudentStorageDatamodel studentStorageDatamodel = new StudentStorageDatamodel(student, new ArrayList<>());
        studentsMap.put(studentId, studentStorageDatamodel);
    }

    public void setStudentsAllocationList(StudentsList studentsList) {
        studentsList.getStudent().stream().filter(Objects::nonNull).forEach(this::updateStudent);
    }

    private void updateStudent(StudentsList.Student student) {
        StudentStorageDatamodel studentStorageDatamodel = studentsMap.get(StudentStorageDatamodel.getId(student));
        if (studentStorageDatamodel == null) {
            log.warn("Es existiert kein Datensatz für den Schüler {} {} in der Klasse {}!", student.getPrename(), student.getSurname(), student.getSchoolClass());
            return;
        }
        studentStorageDatamodel.setAllocation(student.getWishList());
    }

    public void setCompanies(CompaniesList companiesList) {
        companiesCache.clear();
        realScore = null;
        companiesList.getCompany().stream().filter(Objects::nonNull).forEach(this::addCompany);
    }

    private void addCompany(CompaniesList.Company company) {
        companiesCache.put(company.getId(), company);
    }

    public void clearStorage() {
        studentsPerClass.clear();
        studentsMap.clear();
        roomMap.clear();
        companiesCache.clear();
        realScore = null;
    }

    public void setRoomList(RoomList rooms) {
        this.roomMap.clear();
        for (RoomList.Room room : rooms.getRoomList()) {
            roomMap.put(room.getRoomId().trim(), room);
        }
    }

    public RoomList getRoomList() {
        RoomList result = new RoomList();
        result.setRoomList(roomMap.values().stream().toList());
        return result;
    }

    public EventsAttendanceList calculateEventsAttendenceList() {
        List<EventsAttendanceList.AttendanceListsPerCompany> attendanceListsPerCompanyList = new ArrayList<>();
        for (Integer compId : companiesCache.keySet()) {
            List<EventsAttendanceList.AttendanceList> attendanceLists = new ArrayList<>();
            EventsAttendanceList.AttendanceListsPerCompany attendanceListsPerCompany = new EventsAttendanceList.AttendanceListsPerCompany();
            CompaniesList.Company company = companiesCache.get(compId);
            attendanceListsPerCompany.setCompanyName(company.getCompName().trim());
            attendanceListsPerCompany.setCompanyId(compId);
            for (CompaniesList.Meeting meeting : company.getMeeting()) {
                if(meeting.getRoom() != null){
                    attendanceLists.add(new EventsAttendanceList.AttendanceList(meeting, getStudentsForMeeting(compId, meeting.getTimeSlot())));
                }
            }
            attendanceListsPerCompany.setAttendanceList(attendanceLists);
            attendanceListsPerCompanyList.add(attendanceListsPerCompany);
        }
        return new EventsAttendanceList(attendanceListsPerCompanyList, null);
    }

    private List<StudentsList.Student> getStudentsForMeeting(int compId, String timeSlot) {
        List<StudentsList.Student> result = new ArrayList<>();
        for (String schoolClass : studentsPerClass.keySet()) {
            List<StudentsList.Student> studentsFromClass = getStudentsFromClass(schoolClass, StudentStorageDatamodel::getAllocation);
            for (StudentsList.Student student : studentsFromClass) {
                for (int i = 0; i < student.getWishList().size(); i++) {
                    StudentsList.Wish wish = student.getWishList().get(i);
                    if (wish.getCompId() == compId && timeSlot.equals(wish.getTimeSlot())) {
                        result.add(student);
                        break;
                    }
                }
            }
        }
        return result;
    }

    private List<StudentsList.Student> getStudentsFromClass(String schoolClass, Function<StudentStorageDatamodel, List<StudentsList.Wish>> wishForStudent) {
        List<StudentsList.Student> students = new ArrayList<>();
        List<String> studentIds = studentsPerClass.get(schoolClass);
        studentIds.forEach(id -> {
            StudentStorageDatamodel studentStorageDatamodel = studentsMap.get(id.trim());
            StudentsList.Student storedStudent = studentStorageDatamodel.getStudent();
            StudentsList.Student student = new StudentsList.Student();
            student.setSchoolClass(storedStudent.getSchoolClass());
            student.setPrename(storedStudent.getPrename().trim());
            student.setSurname(storedStudent.getSurname().trim());
            student.setWishList(wishForStudent.apply(studentStorageDatamodel));
            students.add(student);
        });
        return students;
    }

    public TimetableList calculateTimeTableList() {
        TimetableList timeTableList = new TimetableList();
        List<TimetableList.TimetableOfStudentsFromClass> timeTablesOfClasses = new ArrayList<>();
        for (String schoolClass : studentsPerClass.keySet()) {
            TimetableList.TimetableOfStudentsFromClass timetableOfStudentsFromClass = new TimetableList.TimetableOfStudentsFromClass();
            List<TimetableList.StudentsAllocation> studentsAllocations = new ArrayList<>();
            List<StudentsList.Student> studentsFromClass = getStudentsFromClass(schoolClass, StudentStorageDatamodel::getAllocation);
            for (StudentsList.Student student : studentsFromClass) {
                TimetableList.StudentsAllocation allocation = new TimetableList.StudentsAllocation();
                allocation.setPrename(student.getPrename().trim());
                allocation.setSurname(student.getSurname().trim());
                TimetableList.TimeTable timetable = getTimeTable(student);
                allocation.setTimeTable(timetable);
                studentsAllocations.add(allocation);
            }
            timetableOfStudentsFromClass.setStudentsAllocationList(studentsAllocations);
            timetableOfStudentsFromClass.setSchoolClass(schoolClass);
            timeTablesOfClasses.add(timetableOfStudentsFromClass);
        }
        timeTableList.setTimetables(timeTablesOfClasses);
        return timeTableList;
    }


    private final List<String> timeSlots = List.of("A", "B", "C", "D", "E");

    private TimetableList.TimeTable getTimeTable(StudentsList.Student student) {
        TimetableList.TimeTable timeTable = new TimetableList.TimeTable();
        List<TimetableList.TimeTable.Rows> rows = new ArrayList<>();
        student.getWishList().sort((a, b) -> {
            int testA = a.getTimeSlot().charAt(0);
            int testB = b.getTimeSlot().charAt(0);
            return Integer.compare(testA, testB);
        });
        for (String timeSlot : timeSlots) {
            StudentsList.Wish wish = getWish(student, timeSlot);
            if (wish != null && wish.getCompId() >= 0) {
                TimetableList.TimeTable.Rows row = new TimetableList.TimeTable.Rows();
                CompaniesList.Company company = companiesCache.get(wish.getCompId());
                row.setMeeting(getMeetingOfTimeSlot(company.getMeeting(), timeSlot));
                row.setCompanyName(company.getCompName());
                row.setCompanyEvent(company.getTrainingOccupation());
                row.setNumberWish(getNumberOfWish(wish, student));
                rows.add(row);
            }
        }
        timeTable.setRows(rows);
        return timeTable;
    }

    private String getNumberOfWish(StudentsList.Wish wish, StudentsList.Student student) {
        List<StudentsList.Student> students = getStudentsFromClass(student.getSchoolClass(), studentStorageDatamodel -> studentStorageDatamodel.getStudent().getWishList());
        for (StudentsList.Student s : students) {
            if (sameStudent(s, student)) {
                for (int i = 0; i < student.getWishList().size(); i++) {
                    if (wish.equals(student.getWishList().get(i))) {
                        return "" + (i+1);
                    }
                }
            }
        }
        return "-";
    }

    private boolean sameStudent(StudentsList.Student s, StudentsList.Student student) {
        return s.getPrename().equals(student.getPrename()) &&
                s.getSurname().equals(student.getSurname()) &&
                s.getSchoolClass().equals(student.getSchoolClass());
    }

    private CompaniesList.Meeting getMeetingOfTimeSlot(List<CompaniesList.Meeting> meetingList, String timeSlot) {
        for (CompaniesList.Meeting meeting : meetingList) {
            if (meeting.getTimeSlot().equals(timeSlot)) {
                return meeting;
            }
        }
        return null;
    }

    private StudentsList.Wish getWish(StudentsList.Student student, String timeSlot) {
        for (StudentsList.Wish wish : student.getWishList()) {
            if (wish.getTimeSlot().trim().equals(timeSlot.trim())) {
                return wish;
            }
        }
        return null;
    }

    public void changeRoomForCompanyAndTimeSlot(String companyId, String timeslot, String room) {
        try {
            int compId = Integer.parseInt(companyId.trim());
            CompaniesList.Company company = companiesCache.get(compId);
            if (company == null) {
                log.warn("Es existiert keine Veranstaltung mit der ID: {}", compId);
                return;
            }
            if (timeslot == null || timeslot.isBlank() || !timeSlots.contains(timeslot.trim())) {
                log.warn("Der TimeSlot ist nicht gesetzt oder hat ein ungültiges Format: {}", timeslot);
                return;
            }
            CompaniesList.Meeting meetingOfTimeSlot = getMeetingOfTimeSlot(company.getMeeting(), timeslot);
            if (meetingOfTimeSlot == null) {
                log.warn("Die Veranstaltung mit der ID: {} läuft nicht im Zeitslot: {}", compId, timeslot.trim());
                return;
            }
            if (room == null || room.isBlank() || roomMap.get(room.trim()) == null) {
                log.warn("Der Raum: {} ist unbekannt", room);
                return;
            }
            String oldRoom = "";
            if (meetingOfTimeSlot.getRoom() == null) {
                meetingOfTimeSlot.setRoom(new RoomList.Room(room.trim()));
            } else {
                oldRoom = meetingOfTimeSlot.getRoom().getRoomId();
                meetingOfTimeSlot.getRoom().setRoomId(room);
            }
            replaceRoom(compId, room, timeslot, oldRoom);
        } catch (NumberFormatException e){
            log.error("Die ID der Veranstaltung muss eine Ganzzahl sein! ID: {}", companyId);
        }

    }

    private void replaceRoom(int companyId, String room, String timeslot, String oldRoom) {
        CompaniesList.Company company = searchForEventInTimeSlotWithRoom(companyId, timeslot, room);
        if(company == null){
            log.debug("Der Raum {} wurde im Timeslot {} noch von keiner Veranstaltung verwendet, und kann somit ohne weitere Anpassung für die Veranstaltung {} verwendet werden", room, timeslot, companyId);
        }
        CompaniesList.Meeting meetingOfTimeSlot = getMeetingOfTimeSlot(company.getMeeting(), timeslot);
        if(meetingOfTimeSlot != null && meetingOfTimeSlot.getRoom() != null){
            meetingOfTimeSlot.getRoom().setRoomId(oldRoom);
        }
    }

    private CompaniesList.Company searchForEventInTimeSlotWithRoom(int companyId, String timeslot, String room) {
        for (int compId : companiesCache.keySet()) {
            if(compId == companyId){
                continue;
            }
            CompaniesList.Company company = companiesCache.get(compId);
            CompaniesList.Meeting meetingOfTimeSlot = getMeetingOfTimeSlot(company.getMeeting(), timeslot);
            if(meetingOfTimeSlot != null && meetingOfTimeSlot.getRoom() != null && room.equals(meetingOfTimeSlot.getRoom().getRoomId())){
                return company;
            }
        }
        return null;
    }

    public void addRooms(List<RoomList.Room> roomList) {
        roomList.forEach(room -> roomMap.put(room.getRoomId(), room));
    }
}