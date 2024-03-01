package de.bwv.ac.datamanagement.service;

import de.bwv.ac.datamanagement.data.RoomList;
import de.bwv.ac.datamanagement.data.StudentsList;
import de.bwv.ac.datamanagement.data.CompaniesList;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.ArrayList;
import java.util.List;

@RestController
public class DataManagementService {
    private final DataStorage dataStorage;

    public DataManagementService(DataStorage dataStorage){
        this.dataStorage = dataStorage;
    }

    @GetMapping("/companies")
    public CompaniesList getAllCompanies(){
        return dataStorage.getCompaniesList();
    }

    @GetMapping("/students")
    public StudentsList getAllStudents(){
        return dataStorage.getStudentsList();
    }

    @GetMapping("/rooms")
    public RoomList getAllRooms(){
        return dataStorage.getRoomList();
    }

    @PostMapping("/students/wishes")
    public void postStudentWishes(StudentsList studentsWithJson){
        //TODO test
        dataStorage.setStudentsList(studentsWithJson);
    }

    @PostMapping("/roomsList")
    public void postRoomsList(String fileLocation){
        ExcelReader reader = new ExcelReader();
        RoomList roomList = reader.readRoomList(fileLocation);
        dataStorage.setRoomList(roomList);
    }

    @PostMapping("/studentList")
    public void postStudentsList(String fileLocation){
        ExcelReader reader = new ExcelReader();
        StudentsList studentsList = reader.readStudentsList(fileLocation);
        dataStorage.setStudentsList(studentsList);
    }

    @Deprecated
    @GetMapping("/students/dummies")
    public StudentsList getAllDummyStudents(){
        StudentsList result = new StudentsList();
        List<StudentsList.Student> students = new ArrayList<>();
        List<StudentsList.Wish> wishes = new ArrayList<>();
        students.add(dummyStudent("Angelika", "Neuberger", "ITF212", wishes));
        students.add(dummyStudent("Jonas", "Haven", "ITF212", wishes));
        students.add(dummyStudent("Nils", "Winkler", "ITF212", wishes));

        result.setStudent(students);
        return result;
    }

    @Deprecated
    @GetMapping("/students/wishes/dummies")
    public StudentsList getAllDummyStudentsWithWishes(){
        StudentsList result = new StudentsList();
        List<StudentsList.Student> students = new ArrayList<>();
        List<StudentsList.Wish> wishes = new ArrayList<>();
        wishes.add(new StudentsList.Wish(1, "C"));
        wishes.add(new StudentsList.Wish(2, "A"));
        wishes.add(new StudentsList.Wish(3, "B"));
        students.add(dummyStudent("Angelika", "Neuberger", "ITF212", wishes));
        wishes.clear();

        wishes.add(new StudentsList.Wish(2, "B"));
        wishes.add(new StudentsList.Wish(3, "C"));
        wishes.add(new StudentsList.Wish(1, "A"));
        students.add(dummyStudent("Jonas", "Haven", "ITF212", wishes));
        wishes.clear();

        wishes.add(new StudentsList.Wish(2, "A"));
        wishes.add(new StudentsList.Wish(3, "C"));
        wishes.add(new StudentsList.Wish(1, "D"));
        students.add(dummyStudent("Nils", "Winkler", "ITF212", wishes));
        wishes.clear();

        result.setStudent(students);
        return result;
    }

    @Deprecated
    private StudentsList.Student dummyStudent(String prename, String surname, String clasz, List<StudentsList.Wish> wishes) {
        return new StudentsList.Student(prename, surname, clasz, new ArrayList<>(wishes));
    }


    @Deprecated
    @GetMapping("/companies/room/dummy")
    public CompaniesList getAllDummyCompaniesWithRoomsAndTimeslots() {
        CompaniesList result = new CompaniesList();
        List<CompaniesList.Company> companyList = new ArrayList<>();
        //Company 1
        List<CompaniesList.Meeting> meetings = new ArrayList<>();
        meetings.add(new CompaniesList.Meeting("A", new RoomList.Room("306")));
        meetings.add(new CompaniesList.Meeting("C" , new RoomList.Room("311")));
        meetings.add(new CompaniesList.Meeting("D", new RoomList.Room("312")));
        companyList.add(dummyCompany(1,"Heusch/BoesefeldtGmbH", "Fachinformatiker Anwendungsentwicklung", meetings));
        meetings.clear();

        //Company 2
        meetings.add(new CompaniesList.Meeting("A", new RoomList.Room("Aula")));
        meetings.add(new CompaniesList.Meeting("B", new RoomList.Room("301")));
        meetings.add(new CompaniesList.Meeting("C", new RoomList.Room("Aula")));
        meetings.add(new CompaniesList.Meeting("D", new RoomList.Room("Aula")));
        meetings.add(new CompaniesList.Meeting("E", new RoomList.Room("301")));
        companyList.add(dummyCompany(2, "RWTH", "Informatik Studium", meetings));
        meetings.clear();

        //Company 3
        meetings.add(new CompaniesList.Meeting("C", new RoomList.Room("Aula")));
        meetings.add(new CompaniesList.Meeting("E", new RoomList.Room("301")));
        companyList.add(dummyCompany(3, "Fachhochschule", "Mathematisch-technischer-Softwareentwickler", meetings));
        meetings.clear();

        result.setCompany(companyList);
        return result;

    }

    @Deprecated
    @GetMapping("/companies/dummy")
    public CompaniesList getAllDummyCompanies() {
        CompaniesList result = new CompaniesList();
        List<CompaniesList.Company> companyList = new ArrayList<>();
        //Company 1
        List<CompaniesList.Meeting> meetings = new ArrayList<>();
        companyList.add(dummyCompany(1,"Heusch/Boesefeldt GmbH", "Fachinformatiker Anwendungsentwicklung", meetings));
        //Company 2
        companyList.add(dummyCompany(2, "RWTH", "Informatik Studium", meetings));
        //Company 3
        companyList.add(dummyCompany(3, "Fachhochschule", "Mathematisch-technischer-Softwareentwickler", meetings));

        result.setCompany(companyList);
        return result;

    }

    @Deprecated
    private CompaniesList.Company dummyCompany(int id, String compName, String training, List<CompaniesList.Meeting> meetings) {
        return new CompaniesList.Company(id, compName, training, new ArrayList<>(meetings), 20);
    }

}
