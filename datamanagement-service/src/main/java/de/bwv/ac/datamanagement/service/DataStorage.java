package de.bwv.ac.datamanagement.service;

import de.bwv.ac.datamanagement.data.CompaniesList;
import de.bwv.ac.datamanagement.data.RoomList;
import de.bwv.ac.datamanagement.data.StudentsList;
import de.bwv.ac.datamanagement.data.export.EventsAttendanceList;

import java.util.*;

public class DataStorage {

    //Key: Company-Id, Value: Company
    private final Map<Integer, CompaniesList.Company> companiesCache = new HashMap<>();

    //Key: Class, Value: Students from Class
    private final Map<String, List<StudentsList.Student>> studentsPerClass = new HashMap<>();

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
        studentsPerClass.forEach((clasz, students) -> studentList.addAll(students));
        result.setStudent(studentList);
        return result;
    }


    public void setStudentsList(StudentsList studentsList) {
        studentsPerClass.clear();
        studentsList.getStudent().stream().filter(Objects::nonNull).forEach(this::addStudent);
    }

    private void addStudent(StudentsList.Student student) {
        List<StudentsList.Student> studentList = studentsPerClass.getOrDefault(student.getSchoolClass(), new ArrayList<>());
        studentList.add(student);
        studentsPerClass.put(student.getSchoolClass(), studentList);
    }

    public void setCompanies(CompaniesList companiesList) {
        companiesCache.clear();
        companiesList.getCompany().stream().filter(Objects::nonNull).forEach(this::addCompany);
    }

    private void addCompany(CompaniesList.Company company) {
        companiesCache.put(company.getId(), company);
    }

    public void clearStorage() {
        studentsPerClass.clear();
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
        //TODO
        return null;
    }
}
