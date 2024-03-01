package de.bwv.ac.datamanagement.service;

import de.bwv.ac.datamanagement.data.CompaniesList;
import de.bwv.ac.datamanagement.data.RoomList;
import de.bwv.ac.datamanagement.data.SolutionAttendanceList;
import de.bwv.ac.datamanagement.data.StudentsList;

import java.util.*;

public class DataStorage { //TODO test

    //Key: Company-Id, Value: Company
    private final Map<Integer, CompaniesList.Company> companiesCache = new HashMap<>();

    //Key: Class, Value: Students from Class
    private final Map<String, List<StudentsList.Student>> studentsPerClass = new HashMap<>();

    //Key: Company-Name, Value: AttendanceList for Company
    private final Map<String, SolutionAttendanceList.AttendanceList> attendanceListPerCompany = new HashMap<>();

    private final List<RoomList.Room> roomList = new ArrayList<>();

    private SolutionAttendanceList calculateAttendanceList() {
        //TODO
        return null;
    }

    public SolutionAttendanceList getSolutionAttendanceList() {
        SolutionAttendanceList result = new SolutionAttendanceList();
        if(attendanceListPerCompany.isEmpty()){
            return calculateAttendanceList();
        }
        List<SolutionAttendanceList.AttendanceList> attendanceLists = new ArrayList<>();
        attendanceListPerCompany.forEach((companyName, attendanceList) -> attendanceLists.add(attendanceList));
        result.setAttendanceLists(attendanceLists);
        return result;
    }

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
        studentsPerClass.forEach((clasz, students) -> studentList.addAll(students));
        result.setStudent(studentList);
        return result;
    }


    public void setStudentsList(StudentsList studentsList) {
        studentsPerClass.clear();
        attendanceListPerCompany.clear();
        studentsList.getStudent().stream().filter(Objects::nonNull).forEach(this::addStudent);
    }

    private void addStudent(StudentsList.Student student) {
        List<StudentsList.Student> studentList = studentsPerClass.getOrDefault(student.getSchoolClass(), new ArrayList<>());
        studentList.add(student);
        studentsPerClass.put(student.getSchoolClass(), studentList);
    }

    public void setCompanies(CompaniesList companiesList) {
        companiesCache.clear();
        attendanceListPerCompany.clear();
        companiesList.getCompany().stream().filter(Objects::nonNull).forEach(this::addCompany);

    }

    private void addCompany(CompaniesList.Company company) {
        companiesCache.put(company.getId(), company);
    }

    public void clearStorage() {
        studentsPerClass.clear();
        companiesCache.clear();
        attendanceListPerCompany.clear();
    }

    public void setRoomList(RoomList rooms){
        this.roomList.clear();
        this.roomList.addAll(rooms.getRoomList());
    }

    public RoomList getRoomList() {
        RoomList result = new RoomList();
        result.setRoomList(roomList);
        return result;
    }
}
