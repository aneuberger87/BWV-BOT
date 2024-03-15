package de.bwv.ac.datamanagement.service;

import de.bwv.ac.datamanagement.data.CompaniesList;
import de.bwv.ac.datamanagement.data.RoomList;
import de.bwv.ac.datamanagement.data.StudentsList;
import de.bwv.ac.datamanagement.data.export.EventsAttendanceList;
import de.bwv.ac.datamanagement.data.export.TimetableList;
import de.bwv.ac.datamanagement.data.storage.StudentStorageDatamodel;
import lombok.extern.slf4j.Slf4j;

import java.util.*;
import java.util.function.Function;

@Slf4j
public class DataStorage {

    //Key: Company-Id, Value: Company
    private final Map<Integer, CompaniesList.Company> companiesCache = new HashMap<>();
    //Key: Class, Value: Students from Class
    //private final Map<String, List<StudentsList.Student>> studentsPerClassWishMap = new HashMap<>();
    //private final Map<String, List<StudentsList.Student>> studentsPerClassAllocationMap = new HashMap<>();

    private final Map<String, List<String>> studentsPerClass = new HashMap<>();
    private final Map<String, StudentStorageDatamodel> studentsMap = new HashMap<>();
    private final Map<String, RoomList.Room> roomMap = new HashMap<>();
    //private final Map<Integer, List<EventsAttendanceList.AttendanceList>> attendanceListPerCompanyMap = new HashMap<>();


    public CompaniesList getCompaniesList() {
        CompaniesList result = new CompaniesList();
        if(companiesCache.isEmpty()){
            result.setErrorMessage("Es wurden keine Veranstaltungen eingelesen. Entweder war die Datei leer/fehlerhaft oder es wurde noch keine Datei hochgeladen!");
            return result;
        }
        List<CompaniesList.Company> companies = new ArrayList<>();
        companiesCache.forEach((id, company) -> companies.add(company));
        result.setCompany(companies);
        return result;
    }

    public StudentsList getStudentsWishList(){
        StudentsList result = getStudentList(studentStorageDatamodel -> studentStorageDatamodel.getStudent().getWishList());
        if(result.getStudent().isEmpty()){
            result.setErrorMessage("Es wurden keine Schüler eingelesen. Entweder war die Schüler-Datei leer/fehlerhaft oder es wurde noch keine Datei hochgeladen!");
        }
        return result;
    }

    public StudentsList getStudentsAllocationList(){
        StudentsList result = getStudentList(StudentStorageDatamodel::getAllocation);
        if(result.getStudent().isEmpty()){
            result.setErrorMessage("Es wurde noch keine Zuteilung erstellt!");
        }
        return result;
    }

    private StudentsList getStudentList(Function<StudentStorageDatamodel, List<StudentsList.Wish>> wishListForStudent){
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
        studentsPerClass.clear();
        studentsList.getStudent().stream().filter(Objects::nonNull).forEach(this::addStudent);
    }

    private void addStudent(StudentsList.Student student) {
        String schoolClass = student.getSchoolClass();
        List<String> studentsInClass = studentsPerClass.getOrDefault(schoolClass, new ArrayList<>());
        String studentId = StudentStorageDatamodel.getId(student);
        studentsInClass.add(studentId);
        studentsPerClass.put(schoolClass, studentsInClass);
        StudentStorageDatamodel studentStorageDatamodel = new StudentStorageDatamodel(student, new ArrayList<>());
        studentsMap.put(studentId, studentStorageDatamodel);
    }

    public void setStudentsAllocationList(StudentsList studentsList) {
        studentsList.getStudent().stream().filter(Objects::nonNull).forEach(this::updateStudent);
    }

    private void updateStudent(StudentsList.Student student) {
        StudentStorageDatamodel studentStorageDatamodel = studentsMap.get(StudentStorageDatamodel.getId(student));
        if(studentStorageDatamodel == null){
            log.warn("Es existiert kein Datensatz für den Schüler {} {} in der Klasse {}!", student.getPrename(), student.getSurname(), student.getSchoolClass());
            return;
        }
        studentStorageDatamodel.setAllocation(student.getWishList());
    }
/*
    private void addStudent(StudentsList.Student student, Map<String, List<StudentsList.Student>> studentsPerClassMap) {
        List<StudentsList.Student> studentList = studentsPerClassMap.getOrDefault(student.getSchoolClass(), new ArrayList<>());
        studentList.add(student);
        studentsPerClassMap.put(student.getSchoolClass(), studentList);
    }
*/
    public void setCompanies(CompaniesList companiesList) {
        companiesCache.clear();
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
    }

    public void setRoomList(RoomList rooms){
        this.roomMap.clear();
        for (RoomList.Room room : rooms.getRoomList()) {
            roomMap.put(room.getRoomId(), room);
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
            attendanceListsPerCompany.setCompanyName(company.getCompName());
            attendanceListsPerCompany.setCompanyId(compId);
            for(CompaniesList.Meeting meeting : company.getMeeting()){
                attendanceLists.add(new EventsAttendanceList.AttendanceList(meeting, getStudentsForMeeting(compId, meeting.getTimeSlot())));
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
                    if(wish.getCompId() == compId && timeSlot.equals(wish.getTimeSlot())){
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
            StudentStorageDatamodel studentStorageDatamodel = studentsMap.get(id);
            StudentsList.Student storedStudent = studentStorageDatamodel.getStudent();
            StudentsList.Student student = new StudentsList.Student();
            student.setSchoolClass(storedStudent.getSchoolClass());
            student.setPrename(storedStudent.getPrename());
            student.setSurname(storedStudent.getSurname());
            student.setWishList(wishForStudent.apply(studentStorageDatamodel));
            students.add(student);
        });
        return students;
    }
/*
    public TimetableList calculateTimeTableList() {
        if(studentsPerClassAllocationMap.isEmpty()){
            studentsPerClassAllocationMap.putAll(studentsPerClassWishMap); //Erstmal für Test Zwecke
            // return new TimetableList(new ArrayList<>(), "Es kann keine Laufliste erstellt werden, weil die Zuteilung noch nicht erfolgt ist");
        }
        TimetableList timeTableList = new TimetableList();
        List<TimetableList.TimetableOfStudentsFromClass> timeTablesOfClasses = new ArrayList<>();
        for (String schoolClass : studentsPerClassAllocationMap.keySet()) {
            TimetableList.TimetableOfStudentsFromClass timetableOfStudentsFromClass = new TimetableList.TimetableOfStudentsFromClass();
            List<TimetableList.StudentsAllocation> studentsAllocations = new ArrayList<>();
            List<StudentsList.Student> studentsFromClass = studentsPerClassAllocationMap.get(schoolClass);
            for(StudentsList.Student student : studentsFromClass){
                TimetableList.StudentsAllocation allocation = new TimetableList.StudentsAllocation();
                allocation.setPrename(student.getPrename());
                allocation.setSurname(student.getSurname());
                TimetableList.TimeTable timetable = getTimeTable(student, schoolClass);
                allocation.setTimeTable(timetable);
                studentsAllocations.add(allocation);
            }
            timetableOfStudentsFromClass.setStudentsAllocationList(studentsAllocations);
            timeTablesOfClasses.add(timetableOfStudentsFromClass);
        }
        timeTableList.setTimetables(timeTablesOfClasses);
        return timeTableList;
    }
 */

    private final List<String> timeSlots = List.of("A", "B", "C", "D", "E");

    private TimetableList.TimeTable getTimeTable(StudentsList.Student student, String schoolClass) {
        TimetableList.TimeTable timeTable = new TimetableList.TimeTable();
        List<TimetableList.TimeTable.Rows> rows = new ArrayList<>();
        for(String timeSlot : timeSlots){
            StudentsList.Wish wish = getWish(student, timeSlot);
            if(wish != null){
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
        for(StudentsList.Student s : students){
            if(s.equals(student)){
                for(int i = 0; i < student.getWishList().size(); i++){
                    if(wish.equals(student.getWishList().get(i))){
                        return ""+i;
                    }
                }
            }
        }
        return "-";
    }

    private CompaniesList.Meeting getMeetingOfTimeSlot(List<CompaniesList.Meeting> meetingList, String timeSlot) {
        for(CompaniesList.Meeting meeting : meetingList){
            if(meeting.getTimeSlot().equals(timeSlot)){
                return meeting;
            }
        }
        return null;
    }

    private StudentsList.Wish getWish(StudentsList.Student student, String timeSlot) {
        for(StudentsList.Wish wish : student.getWishList()){
            if(wish.getTimeSlot().trim().equals(timeSlot.trim())){
                return wish;
            }
        }
        return null;
    }
/*
    public EventsAttendanceList getEventsAttendanceList() {
        List<EventsAttendanceList.AttendanceListsPerCompany> attendanceListsPerCompanyList = new ArrayList<>();
        try {


            for (Integer companyId : stu.keySet()) {
                CompaniesList.Company company = companiesCache.get(companyId);
                List<EventsAttendanceList.AttendanceList> attendanceLists = attendanceListPerCompanyMap.get(companyId);
                EventsAttendanceList.AttendanceListsPerCompany attendanceListsPerCompany = new EventsAttendanceList.AttendanceListsPerCompany(companyId, company.getCompName(), attendanceLists);
                attendanceListsPerCompanyList.add(attendanceListsPerCompany);
            }
        } catch (Exception e){
            return new EventsAttendanceList(new ArrayList<>(), "Die Anwesenheitsliste konnte nicht geladen werden. Fehlermeldung: "+e.getMessage());
        }
        return new EventsAttendanceList(attendanceListsPerCompanyList, null);
    }

    public void setEventsAttendanceList(EventsAttendanceList eventsAttendanceList) {
        attendanceListPerCompanyMap.clear();
        for (EventsAttendanceList.AttendanceListsPerCompany attendanceListsPerCompany : eventsAttendanceList.getAttendanceListsPerCompany()) {
            List<EventsAttendanceList.AttendanceList> attendanceList = attendanceListsPerCompany.getAttendanceList();
            int companyId = attendanceListsPerCompany.getCompanyId();
            attendanceListPerCompanyMap.put(companyId, attendanceList);
        }
    }
 */
}