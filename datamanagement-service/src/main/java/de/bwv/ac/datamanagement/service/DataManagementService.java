package de.bwv.ac.datamanagement.service;

import de.bwv.ac.datamanagement.data.PostResponse;
import de.bwv.ac.datamanagement.data.RoomList;
import de.bwv.ac.datamanagement.data.StudentsList;
import de.bwv.ac.datamanagement.data.CompaniesList;
import de.bwv.ac.datamanagement.data.export.EventsAttendanceList;
import de.bwv.ac.datamanagement.service.reader.EventsListReader;
import de.bwv.ac.datamanagement.service.reader.ExcelReader;
import de.bwv.ac.datamanagement.service.reader.RoomListReader;
import de.bwv.ac.datamanagement.service.reader.StudentsListReader;
import de.bwv.ac.datamanagement.service.writer.AttendanceListWriter;
import de.bwv.ac.datamanagement.service.writer.ExcelWriter;
import de.bwv.ac.datamanagement.service.writer.RoomAssignmentsListWriter;
import de.bwv.ac.datamanagement.service.writer.TimetableListWriter;
import lombok.extern.slf4j.Slf4j;
import org.springframework.web.bind.annotation.*;

@RestController
@Slf4j
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
        return dataStorage.getStudentsWishList();
    }

    @GetMapping("/students/allocation")
    public StudentsList getAllStudentsAllocations(){
        return dataStorage.getStudentsAllocationList();
    }

    @GetMapping("/rooms")
    public RoomList getAllRooms(){
        return dataStorage.getRoomList();
    }

    @GetMapping("/attendanceList")
    public EventsAttendanceList getAttendanceList(){
        return dataStorage.calculateEventsAttendenceList();
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

    // Anfrage zum Einlesen der neuen Excel-Datei mit Studenten
    @PostMapping("/studentsList")
    public PostResponse postStudentsList(@RequestParam("fileLocation") String fileLocation){
        try {
            ExcelReader<StudentsList> reader = new StudentsListReader();
            StudentsList studentsList = reader.read(fileLocation);
            dataStorage.setStudentsWishesList(studentsList);
            return new PostResponse();
        } catch (Exception e) {
            return new PostResponse("Post failed with Exception: "+e.getClass().getName()+", Message: "+e.getMessage());
        }
    }

    @PostMapping("update/studentsList")
    public PostResponse updateStudentsList(@RequestParam("student") StudentsList studentsList){
        try {
            dataStorage.setStudentsAllocationList(studentsList);
            return new PostResponse();
        } catch (Exception e) {
            return new PostResponse("Post failed with Exception: "+e.getClass().getName()+", Message: "+e.getMessage());
        }
    }

    @PutMapping("update/{companyId}/{timeslot}")
    public CompaniesList updateMeetingForCompany(@PathVariable String companyId, @PathVariable String timeslot, @RequestBody String room){
        //TODO: implement
        return null;
    }
/*
    @PostMapping("update/allocation/studentsList")
    public PostResponse updateAllocationStudentsList(@RequestParam("studentsList") StudentsList studentsList){
        try {
            dataStorage.setStudentsAllocationList(studentsList);
            return new PostResponse();
        } catch (Exception e) {
            return new PostResponse("Post failed with Exception: "+e.getClass().getName()+", Message: "+e.getMessage());
        }
    }
*/
    @PostMapping("update/companiesList")
    public PostResponse updateCompaniesList(@RequestParam("company") CompaniesList companiesList){
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

    @PostMapping("print/roomAssignmentsList")
    public PostResponse printRoomAssignmentsList(@RequestParam("fileLocation") String fileLocation){
        try {
            ExcelWriter writer = new RoomAssignmentsListWriter(dataStorage);
            writer.write(fileLocation);
            return new PostResponse();
        } catch (Exception e) {
            return new PostResponse("Post failed with Exception: "+e.getClass().getName()+", Message: "+e.getMessage());
        }
    }

    @GetMapping("calculate")
    public PostResponse calculate(){
        try {
            pythonScriptExecuter.executeScript("Tranformation.py");
            return new PostResponse();
        } catch (Exception e) {
            return new PostResponse("Post failed with Exception: "+e.getClass().getName()+", Message: "+e.getMessage());
        }
    }
/*
    @PostMapping("/update/timetableList")
    public PostResponse updateTimetableList(String json){
        try {
            System.out.println(json);
            return new PostResponse();
        } catch (Exception e) {
            return new PostResponse("Post failed with Exception: "+e.getClass().getName()+", Message: "+e.getMessage());
        }
    }
 */

}
