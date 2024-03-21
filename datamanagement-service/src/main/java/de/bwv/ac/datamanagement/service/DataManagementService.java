package de.bwv.ac.datamanagement.service;

import de.bwv.ac.datamanagement.data.*;
import de.bwv.ac.datamanagement.data.export.EventsAttendanceList;
import de.bwv.ac.datamanagement.data.export.TimetableList;
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

import java.util.ArrayList;

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
        log.info("GET-Anfrage für die Veranstaltungsliste");
        return dataStorage.getCompaniesList();
    }

    @GetMapping("/students")
    public StudentsList getAllStudents(){
        log.info("GET-Anfrage für die Schülerliste");
        return dataStorage.getStudentsWishList();
    }

    @GetMapping("/rooms")
    public RoomList getAllRooms(){
        log.info("GET-Anfrage für die Raumliste");
        return dataStorage.getRoomList();
    }

    @GetMapping("/students/allocation")
    public StudentsList getAllStudentsAllocations(){
        log.info("GET-Anfrage für die Zuteilung der Schüler auf die Veranstaltungen");
        return dataStorage.getStudentsAllocationList();
    }

    @GetMapping("/attendanceList")
    public EventsAttendanceList getAttendanceList(){
        log.info("GET-Anfrage für die Anwesenheitslisten der Veranstaltungen");
        return dataStorage.calculateEventsAttendenceList();
    }

    @GetMapping("/timetableList")
    public TimetableList getTimetabelList(){
        log.info("GET-Anfrage für die Laufzettel der Schüler");
        return dataStorage.calculateTimeTableList();
    }

    @PostMapping("/roomsList")
    public PostResponse postRoomsList(@RequestParam("fileLocation") String fileLocation){
        log.info("POST-Anfrage mit der FileLocation für die Excel-Raumliste");
        try {
            ExcelReader<RoomList> reader = new RoomListReader();
            RoomList roomList = reader.read(fileLocation);
            dataStorage.setRoomList(roomList);
            return new PostResponse();
        } catch (Exception e) {
            e.printStackTrace();
            log.error("POST failed with the Exception: {}, Message: {}", e.getClass().getName(), e.getMessage());
            log.error("Die RaumListe konnte nicht ausgelesene werden!");
            return new PostResponse("Die RaumListe konnte nicht ausgelesen werden! Fehlermeldung: "+e.getMessage());
        }
    }

    @PostMapping("/companiesList")
    public PostResponse postCompaniesList(@RequestParam("fileLocation") String fileLocation){
        log.info("POST-Anfrage mit der FileLocation für die Excel-Veranstaltungsliste");
        try {
            ExcelReader<CompaniesList> reader = new EventsListReader();
            CompaniesList companiesList = reader.read(fileLocation);
            dataStorage.setCompanies(companiesList);
            return new PostResponse();
        } catch (Exception e) {
            e.printStackTrace();
            log.error("POST failed with the Exception: {}, Message: {}", e.getClass().getName(), e.getMessage());
            log.error("Die Veranstaltungsliste konnte nicht ausgelesen werden!");
            return new PostResponse("Die Veranstaltungsliste konnte nicht ausgelesen werden! Fehlermeldung: "+e.getMessage());
        }
    }

    // Anfrage zum Einlesen der neuen Excel-Datei mit Studenten
    @PostMapping("/studentsList")
    public PostResponse postStudentsList(@RequestParam("fileLocation") String fileLocation){
        log.info("POST-Anfrage mit der FileLocation für die Excel-Schülerliste");
        try {
            ExcelReader<StudentsList> reader = new StudentsListReader();
            StudentsList studentsList = reader.read(fileLocation);
            dataStorage.setStudentsWishesList(studentsList);
            return new PostResponse();
        } catch (Exception e) {
            e.printStackTrace();
            log.error("POST failed with the Exception: {}, Message: {}", e.getClass().getName(), e.getMessage());
            log.error("Die Schülerliste konnte nicht ausgelesen werden!");
            return new PostResponse("Die Schülerliste konnte nicht ausgelesen werden! Fehlermeldung: "+e.getMessage());
        }
    }

    @PostMapping("/update/studentsList")
    public PostResponse updateStudentsList(@RequestBody StudentsList studentsList){
        log.info("POST-Anfrage zur Aktualisierung der Schülerliste mit den Zuteilungen anstelle der Wünsche");
        try {
            dataStorage.setStudentsAllocationList(studentsList);
            return new PostResponse();
        } catch (Exception e) {
            e.printStackTrace();
            log.error("POST failed with the Exception: {}, Message: {}", e.getClass().getName(), e.getMessage());
            log.error("Die Schülerliste konnte nicht aktuallisiert werden!");
            return new PostResponse("Die Schülerliste konnte nicht aktuallisiert werden! Fehlermeldung: "+e.getMessage());
        }
    }

    @PostMapping("/update/companiesList")
    public PostResponse updateCompaniesList(@RequestBody CompaniesList companiesList){
        log.info("POST-Anfrage zur Aktualisierung der Veranstaltungsliste mit den Zuteilungen auf Räume pro Zeitslot");
        try {
            dataStorage.setCompanies(companiesList);
            return new PostResponse();
        } catch (Exception e) {
            e.printStackTrace();
            log.error("POST failed with the Exception: {}, Message: {}", e.getClass().getName(), e.getMessage());
            log.error("Die Veranstaltungsliste konnte nicht aktuallisiert werden!");
            return new PostResponse("Die Veranstaltungsliste konnte nicht aktuallisiert werden! Fehlermeldung: "+e.getMessage());
        }
    }

    @PutMapping("/update/{companyId}/{timeslot}")
    public void updateMeetingForCompany(@PathVariable String companyId, @PathVariable String timeslot, @RequestBody String room){
        log.info("PUT-Anfrage zum Ändern des Raums, der für eine Veranstaltung mit der ID: {} im Zeitslot: {} zugeteilt wurde auf {}", companyId, timeslot, room);
        try {
            dataStorage.changeRoomForCompanyAndTimeSlot(companyId, timeslot, room);
        } catch (Exception e) {
            e.printStackTrace();
            log.error("PUT failed with the Exception: {}, Message: {}", e.getClass().getName(), e.getMessage());
            log.error("Der Raum konnte nicht geändert werden!");
        }
    }

    @PostMapping("/print/attendanceList")
    public PostResponse printAttendanceList(@RequestParam("fileLocation") String fileLocation){
        try {
            ExcelWriter writer = new AttendanceListWriter(dataStorage);
            writer.write(fileLocation);
            return new PostResponse();
        } catch (Exception e) {
            e.printStackTrace();
            return new PostResponse("Post failed with Exception: "+e.getClass().getName()+", Message: "+e.getMessage());
        }
    }

    @GetMapping("/solutionScore")
    public SolutionScore getSolutionScore() {
        SolutionScore realScore = dataStorage.getRealScore();
        if(realScore == null){
            return new SolutionScore(-1, "Der Erfüllungsscore kann nicht ermittelt werden!");
        }
        return realScore;
    }

    @PostMapping("/update/solutionScore")
    public void getSolutionScore(@RequestBody double realscore) {
        SolutionScore solutionScore = new SolutionScore(realscore, null);
        dataStorage.setRealScore(solutionScore);
    }

    @PostMapping("/print/timetableList")
    public PostResponse printTimetableList(@RequestParam("fileLocation") String fileLocation){
        try {
            ExcelWriter writer = new TimetableListWriter(dataStorage);
            writer.write(fileLocation);
            return new PostResponse();
        } catch (Exception e) {
            e.printStackTrace();
            return new PostResponse("Post failed with Exception: "+e.getClass().getName()+", Message: "+e.getMessage());
        }
    }

    @PostMapping("/print/roomAssignmentsList")
    public PostResponse printRoomAssignmentsList(@RequestParam("fileLocation") String fileLocation){
        try {
            ExcelWriter writer = new RoomAssignmentsListWriter(dataStorage);
            writer.write(fileLocation);
            return new PostResponse();
        } catch (Exception e) {
            e.printStackTrace();
            return new PostResponse("Post failed with Exception: "+e.getClass().getName()+", Message: "+e.getMessage());
        }
    }

    @GetMapping("/calculate")
    public PostResponse calculate(){
        try {
            pythonScriptExecuter.executeScript("Tranformation.py");
            return new PostResponse();
        } catch (Exception e) {
            e.printStackTrace();
            return new PostResponse("Post failed with Exception: "+e.getClass().getName()+", Message: "+e.getMessage());
        }
    }

    @DeleteMapping("/clearStorage")
    public void clearStorage(){
        dataStorage.clearStorage();
    }

    @PostMapping("rooms/add")
    public PostResponse addRooms(@RequestBody RoomList roomList){
        if(roomList == null || roomList.getErrorMessage() != null || roomList.getRoomList() == null){
            return new PostResponse("Es wurden keine Räume zum Hinzufügen übergeben!");
        }
        dataStorage.addRooms(roomList.getRoomList());
        return new PostResponse();
    }

}
