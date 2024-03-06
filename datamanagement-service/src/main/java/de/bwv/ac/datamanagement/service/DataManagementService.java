package de.bwv.ac.datamanagement.service;

import de.bwv.ac.datamanagement.data.PostResponse;
import de.bwv.ac.datamanagement.data.RoomList;
import de.bwv.ac.datamanagement.data.StudentsList;
import de.bwv.ac.datamanagement.data.CompaniesList;
import de.bwv.ac.datamanagement.service.reader.EventsListReader;
import de.bwv.ac.datamanagement.service.reader.ExcelReader;
import de.bwv.ac.datamanagement.service.reader.RoomListReader;
import de.bwv.ac.datamanagement.service.reader.StudentsListReader;
import de.bwv.ac.datamanagement.service.writer.AttendanceListWriter;
import de.bwv.ac.datamanagement.service.writer.ExcelWriter;
import de.bwv.ac.datamanagement.service.writer.RoomAssignmentsListWriter;
import de.bwv.ac.datamanagement.service.writer.TimetableListWriter;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import java.util.ArrayList;
import java.util.List;

@RestController
public class DataManagementService {
    private final DataStorage dataStorage;
    private final PythonScriptExecuter pythonScriptExecuter;

    public DataManagementService(DataStorage dataStorage, PythonScriptExecuter scriptExecuter){
        this.dataStorage = dataStorage;
        this.pythonScriptExecuter = scriptExecuter;
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

    @PostMapping("/roomsList")
    public PostResponse postRoomsList(@RequestParam("fileLocation") String fileLocation){
        try {
            ExcelReader<RoomList> reader = new RoomListReader();
            RoomList roomList = reader.read(fileLocation);
            dataStorage.setRoomList(roomList);
            return new PostResponse();
        } catch (Exception e) {
            return new PostResponse("Post failed with Exception: "+e.getClass().getName()+", Message: "+e.getMessage());
        }
    }

    @PostMapping("/companiesList")
    public PostResponse postCompaniesList(@RequestParam("fileLocation") String fileLocation){
        try {
            ExcelReader<CompaniesList> reader = new EventsListReader();
            CompaniesList companiesList = reader.read(fileLocation);
            dataStorage.setCompanies(companiesList);
            return new PostResponse();
        } catch (Exception e) {
            return new PostResponse("Post failed with Exception: "+e.getClass().getName()+", Message: "+e.getMessage());
        }
    }

    @PostMapping("/studentsList")
    public PostResponse postStudentsList(@RequestParam("fileLocation") String fileLocation){
        try {
            ExcelReader<StudentsList> reader = new StudentsListReader();
            StudentsList studentsList = reader.read(fileLocation);
            dataStorage.setStudentsList(studentsList);
            return new PostResponse();
        } catch (Exception e) {
            return new PostResponse("Post failed with Exception: "+e.getClass().getName()+", Message: "+e.getMessage());
        }
    }

    @PostMapping("update/studentsList")
    public PostResponse updateStudentsList(@RequestParam("studentsList") StudentsList studentsList){
        try {
            dataStorage.setStudentsList(studentsList);
            return new PostResponse();
        } catch (Exception e) {
            return new PostResponse("Post failed with Exception: "+e.getClass().getName()+", Message: "+e.getMessage());
        }
    }

    @PostMapping("update/companiesList")
    public PostResponse updateStudentsList(@RequestParam("companiesList") CompaniesList companiesList){
        try {
            dataStorage.setCompanies(companiesList);
            return new PostResponse();
        } catch (Exception e) {
            return new PostResponse("Post failed with Exception: "+e.getClass().getName()+", Message: "+e.getMessage());
        }
    }

    @PostMapping("print/attendanceList")
    public PostResponse printAttendanceList(@RequestParam("fileLocation") String fileLocation){
        try {
            ExcelWriter writer = new AttendanceListWriter(dataStorage);
            writer.write(fileLocation);
            return new PostResponse();
        } catch (Exception e) {
            return new PostResponse("Post failed with Exception: "+e.getClass().getName()+", Message: "+e.getMessage());
        }
    }

    @PostMapping("print/timetableList")
    public PostResponse printTimetableList(@RequestParam("fileLocation") String fileLocation){
        try {
            ExcelWriter writer = new TimetableListWriter(dataStorage);
            writer.write(fileLocation);
            return new PostResponse();
        } catch (Exception e) {
            return new PostResponse("Post failed with Exception: "+e.getClass().getName()+", Message: "+e.getMessage());
        }
    }

    @PostMapping("print/timetableList")
    public PostResponse printRoomAssignmentsList(@RequestParam("fileLocation") String fileLocation){
        try {
            ExcelWriter writer = new RoomAssignmentsListWriter(dataStorage);
            writer.write(fileLocation);
            return new PostResponse();
        } catch (Exception e) {
            return new PostResponse("Post failed with Exception: "+e.getClass().getName()+", Message: "+e.getMessage());
        }
    }

    @PostMapping("calculate")
    public PostResponse calculate(){
        try {
            pythonScriptExecuter.executeScript("Transformation.py");
            return new PostResponse();
        } catch (Exception e) {
            return new PostResponse("Post failed with Exception: "+e.getClass().getName()+", Message: "+e.getMessage());
        }
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
