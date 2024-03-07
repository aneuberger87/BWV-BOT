package de.bwv.ac.datamanagement.service;

import de.bwv.ac.datamanagement.data.CompaniesList;
import de.bwv.ac.datamanagement.data.RoomList;
import de.bwv.ac.datamanagement.data.StudentsList;
import de.bwv.ac.datamanagement.data.export.EventsAttendanceList;
import de.bwv.ac.datamanagement.data.export.TimetableList;

import java.util.*;

public class DataStorage {

    //Key: Company-Id, Value: Company
    private final Map<Integer, CompaniesList.Company> companiesCache = new HashMap<>();

    //Key: Class, Value: Students from Class
    private final Map<String, List<StudentsList.Student>> studentsPerClassWishMap = new HashMap<>();
    private final Map<String, List<StudentsList.Student>> studentsPerClassAllocationMap = new HashMap<>();

    private final Map<String, RoomList.Room> roomMap = new HashMap<>();


    public CompaniesList getCompaniesList() {
        CompaniesList result = new CompaniesList();
        List<CompaniesList.Company> companies = new ArrayList<>();
        companiesCache.forEach((id, company) -> companies.add(company));
        result.setCompany(companies);
        return result;
    }

    public StudentsList getStudentsList() {
        StudentsList result = new StudentsList();
        List<StudentsList.Student> studentList = new ArrayList<>();
        if(studentsPerClassAllocationMap.isEmpty()){
            studentsPerClassWishMap.forEach((clasz, students) -> studentList.addAll(students));
        } else {
            studentsPerClassAllocationMap.forEach((clasz, students) -> studentList.addAll(students));
        }
        result.setStudent(studentList);
        return result;
    }


    public void setStudentsWishesList(StudentsList studentsList) {
        studentsPerClassWishMap.clear();
        studentsPerClassAllocationMap.clear();
        studentsList.getStudent().stream().filter(Objects::nonNull).forEach(student -> addStudent(student, studentsPerClassWishMap));
    }

    public void setStudentsAllocationList(StudentsList studentsList) {
        studentsPerClassAllocationMap.clear();
        studentsList.getStudent().stream().filter(Objects::nonNull).forEach(student -> addStudent(student, studentsPerClassAllocationMap));
    }

    private void addStudent(StudentsList.Student student, Map<String, List<StudentsList.Student>> studentsPerClassMap) {
        List<StudentsList.Student> studentList = studentsPerClassMap.getOrDefault(student.getSchoolClass(), new ArrayList<>());
        studentList.add(student);
        studentsPerClassMap.put(student.getSchoolClass(), studentList);
    }

    public void setCompanies(CompaniesList companiesList) {
        companiesCache.clear();
        companiesList.getCompany().stream().filter(Objects::nonNull).forEach(this::addCompany);
    }

    private void addCompany(CompaniesList.Company company) {
        companiesCache.put(company.getId(), company);
    }

    public void clearStorage() {
        studentsPerClassWishMap.clear();
        studentsPerClassAllocationMap.clear();
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
            attendanceListsPerCompany.setCompany(company);
            for(CompaniesList.Meeting meeting : company.getMeeting()){
                attendanceLists.add(new EventsAttendanceList.AttendanceList(company.getCompName(), meeting, getStudentsForMeeting(compId, meeting.getTimeSlot())));
            }
            attendanceListsPerCompany.setAttendanceList(attendanceLists);
            attendanceListsPerCompanyList.add(attendanceListsPerCompany);
        }
        return new EventsAttendanceList(attendanceListsPerCompanyList, null);
    }

    private List<StudentsList.Student> getStudentsForMeeting(int compId, String timeSlot) {
        List<StudentsList.Student> result = new ArrayList<>();
        for (String schoolClass : studentsPerClassWishMap.keySet()) {
            List<StudentsList.Student> studentsFromClass = studentsPerClassWishMap.get(schoolClass);
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
        List<StudentsList.Student> students = studentsPerClassWishMap.get(student.getSchoolClass());
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

}
