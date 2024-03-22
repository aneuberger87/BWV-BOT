package de.bwv.ac.datamanagement.service;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;
import de.bwv.ac.datamanagement.config.Properties;
import de.bwv.ac.datamanagement.data.CompaniesList;
import de.bwv.ac.datamanagement.data.PostResponse;
import de.bwv.ac.datamanagement.data.RoomList;
import de.bwv.ac.datamanagement.data.StudentsList;
import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.Test;
import org.springframework.http.ResponseEntity;
import org.springframework.web.client.RestTemplate;

import java.sql.DatabaseMetaData;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class DataManagementServiceTest {

    private static DataStorage dataStorage = new DataStorage();

    private ObjectMapper objectMapper = new ObjectMapper();

    @BeforeAll
    public static void setUp(){
        Properties props = new Properties();
        props.setEventlistLocation("src/test/resources/unternehmensliste.xlsx");
        props.setStudentslistLocation("src/test/resources/schuelerliste.xlsx");
        props.setRoomlistLocation("src/test/resources/IMPORT_BOT0_Raumliste.xlsx");
        DataStorageInitializer initializer = new DataStorageInitializer(dataStorage, props);
        initializer.initializeDataStorage();
    }

    @Test
    void getAllCompanies() {
        DataManagementService dataManagementService = new DataManagementService(dataStorage, null);
        CompaniesList allCompanies = dataManagementService.getAllCompanies();
        assertNotNull(allCompanies);
        assertNotNull(allCompanies.getCompany());
        assertNull(allCompanies.getErrorMessage());
        assertEquals(14, allCompanies.getCompany().size());
    }

    @Test
    void getAllStudents() {
        DataManagementService dataManagementService = new DataManagementService(dataStorage, null);
        StudentsList allStudents = dataManagementService.getAllStudents();
        assertNotNull(allStudents);
        assertNotNull(allStudents.getStudent());
        assertNull(allStudents.getErrorMessage());
        assertEquals(180, allStudents.getStudent().size());
    }

    @Test
    void postStudentWishes() {
        //Not implemented yet
    }

    @Test
    void postStudentsList() {
        //Not implemented yet
    }




    /////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    //////////////////////////////////////// Tests From Test-Client /////////////////////////////////////////////////
    /////////////////////////////////////////////////////////////////////////////////////////////////////////////////


    private Map<String, Map<Integer, Integer>> numberStudentsForEventPerTimestampMap = new HashMap<>();
    private Set<StudentsList.Student> studentsWithNotAllWishesSet = new HashSet<>();

    @Test
    void test() throws JsonProcessingException {
        dataStorage.clearStorage();
        DataManagementService dataManagementService = new DataManagementService(dataStorage, null);
        readStudentList(dataManagementService,"src/test/resources/IMPORT_BOT2_Wahl.xlsx");
        readCompanies(dataManagementService,"src/test/resources/IMPORT_BOT1_Veranstaltungsliste.xlsx");
        readRoomList(dataManagementService,"src/test/resources/IMPORT_BOT0_Raumliste.xlsx");
        String fileLocation = "src/test/resources/out";
        studentsRequest(dataManagementService);
        eventsRequest(dataManagementService);
        raumzuweisung(dataManagementService, fileLocation);
        anwesenheitsListRequest(dataManagementService, fileLocation);
        laufzettelListRequest(dataManagementService, fileLocation);

        // Ändere Raum 101 auf 103 in Timeslot A compId 2
        putAufruf(dataManagementService, "2", "A", "103");
        fileLocation = "src/test/resources/out/afterChangeRoom";
        raumzuweisung(dataManagementService, fileLocation);
        anwesenheitsListRequest(dataManagementService, fileLocation);
        laufzettelListRequest(dataManagementService, fileLocation);
    }

    private void readRoomList(DataManagementService dataManagementService, String fileLocation) {
        assertEquals(new PostResponse(), dataManagementService.postRoomsList(fileLocation));
        assertNotNull(dataStorage.getRoomList());
        assertFalse(dataStorage.getRoomList().getRoomList().isEmpty());
        assertEquals(27, dataStorage.getRoomList().getRoomList().size());
    }

    private void readCompanies(DataManagementService dataManagementService, String fileLocation) {
        assertEquals(new PostResponse(), dataManagementService.postCompaniesList(fileLocation));
    }

    private void readStudentList(DataManagementService dataManagementService, String fileLocation) {
        assertEquals(new PostResponse(), dataManagementService.postStudentsList(fileLocation));
    }

    private void putAufruf(DataManagementService dataManagementService, String companyId, String timeslot, String newRoomId) {
        dataManagementService.updateMeetingForCompany(companyId, timeslot, newRoomId);
    }

    private void laufzettelListRequest(DataManagementService dataManagementService, String fileLocation) {
        assertEquals(new PostResponse(), dataManagementService.printTimetableList(fileLocation));
    }

    private void raumzuweisung(DataManagementService dataManagementService, String fileLocation) {
        assertEquals(new PostResponse(), dataManagementService.printRoomAssignmentsList(fileLocation));
    }

    private void anwesenheitsListRequest(DataManagementService dataManagementService, String fileLocation) {
        assertEquals(new PostResponse(), dataManagementService.printAttendanceList(fileLocation));
    }

    private void eventsRequest(DataManagementService dataManagementService) throws JsonProcessingException {
        CompaniesList companiesList = dataManagementService.getAllCompanies();
        for (int i = 0; i < companiesList.getCompany().size(); i++) {
            CompaniesList.Company company = companiesList.getCompany().get(i);
            for (CompaniesList.Meeting meeting : company.getMeeting()) {
                int roomNr = 100 + i;
                meeting.setRoom(new RoomList.Room(""+roomNr));
            }
        }
        String json = objectMapper.writeValueAsString(companiesList);
        dataManagementService.updateCompaniesList(json);
    }

    private void studentsRequest(DataManagementService dataManagementService) throws JsonProcessingException {
        CompaniesList companiesList = dataManagementService.getAllCompanies();
        StudentsList studentsList = dataManagementService.getAllStudents();

        for (StudentsList.Student student : studentsList.getStudent()) {
            char start = 'A';
            int i = 0;
            int timeslot = start;
            Set<Integer> verschobeneEvents = new HashSet<>();
            for (i = 0, timeslot = start; i < Math.min(5, student.getWishList().size()); i++, timeslot++) {
                String strTimeSlot = Character.toString(timeslot);
                int compId = student.getWishList().get(i).getCompId();
                if(!verschobeneEvents.isEmpty()){
                    for (Integer verschobeneEvent : verschobeneEvents) {
                        if(hasMeetingInTimeslot(getCompany(companiesList, verschobeneEvent), strTimeSlot)){
                            verschobeneEvents.add(compId);
                            compId = verschobeneEvent;
                            verschobeneEvents.remove(verschobeneEvent);
                            break;
                        }
                    }
                }
                if(!hasMeetingInTimeslot(getCompany(companiesList, compId), strTimeSlot)){
                    verschobeneEvents.add(compId);
                    compId = -1;
                }
                Map<Integer, Integer> numberStudentsPerEvent = numberStudentsForEventPerTimestampMap.getOrDefault(strTimeSlot, new HashMap<>());
                Integer numberStudentsForMeeting = numberStudentsPerEvent.getOrDefault(compId, 0);
                numberStudentsPerEvent.put(compId, numberStudentsForMeeting+1);
                numberStudentsForEventPerTimestampMap.put(strTimeSlot, numberStudentsPerEvent);
                if(compId < 0){
                    student.getWishList().set(i, null);
                } else {
                    student.getWishList().get(i).setTimeSlot(Character.toString(timeslot));
                    student.getWishList().get(i).setCompId(compId);
                }
            }
            if(!verschobeneEvents.isEmpty()){
                for (int j = 0; j < student.getWishList().size(); j++) {
                    StudentsList.Wish wish = student.getWishList().get(j);
                    if(wish != null){
                        continue;
                    }
                    for (Integer compId : verschobeneEvents) {
                        String strTimeslot = Character.toString(start + j);
                        if(hasMeetingInTimeslot(getCompany(companiesList, compId), strTimeslot)){
                            wish = new StudentsList.Wish(compId, strTimeslot);
                            wish.setCompId(compId);
                            student.getWishList().set(j, wish);
                            verschobeneEvents.remove(compId);
                        }
                    }

                }
            }
            if(i < 5){
                studentsWithNotAllWishesSet.add(student);
            }
        }
        for (StudentsList.Student student : studentsWithNotAllWishesSet) {
            List<StudentsList.Wish> wishList = student.getWishList();
            char start = 'A';
            Set<Integer> companiesAlreadyVisitEventsOf = new HashSet<>();
            for(int i = 0; i < 5; i++){
                if(wishList.size() > i){
                    companiesAlreadyVisitEventsOf.add(wishList.get(i).getCompId());
                    continue;
                }
                int timeslot = start + i;
                String strTimeSlot = Character.toString(timeslot);
                int compId = searchTheEventInTimeSlotWithTheMostStudentsUnderTwentyNotInSet(strTimeSlot, companiesAlreadyVisitEventsOf);
                Map<Integer, Integer> studentsPerEvent = numberStudentsForEventPerTimestampMap.getOrDefault(strTimeSlot, new HashMap<>());
                Integer numberStudents = studentsPerEvent.getOrDefault(compId, 0);
                studentsPerEvent.put(compId, numberStudents+1);
                numberStudentsForEventPerTimestampMap.put(strTimeSlot, studentsPerEvent);
                wishList.add(new StudentsList.Wish(compId, strTimeSlot));
            }
        }
        String json = objectMapper.writeValueAsString(studentsList);
        dataManagementService.updateStudentsList(json);
    }

    private boolean hasMeetingInTimeslot(CompaniesList.Company company, String strTimeSlot) {
        for (CompaniesList.Meeting meeting : company.getMeeting()) {
            if(meeting.getTimeSlot().equals(strTimeSlot)){
                return true;
            }
        }
        return false;
    }

    private CompaniesList.Company getCompany(CompaniesList companiesList, int compId) {
        for (CompaniesList.Company company : companiesList.getCompany()) {
            if(company.getId() == compId){
                return company;
            }
        }
        return null;
    }

    private int searchTheEventInTimeSlotWithTheMostStudentsUnderTwentyNotInSet(String strTimeSlot, Set<Integer> alreadyVisitCompanyEvent) {
        Map<Integer, Integer> numberStudentsPerEvent = numberStudentsForEventPerTimestampMap.get(strTimeSlot);
        int maxUnderTwenty = 0;
        int compIdWithMaxUnderTwentyStudents = -1;
        for (Integer compId : numberStudentsPerEvent.keySet()) {
            if(!alreadyVisitCompanyEvent.contains(compId)){
                Integer numberStudents = numberStudentsPerEvent.get(compId);
                if(numberStudents < 20 && numberStudents > maxUnderTwenty){
                    maxUnderTwenty = numberStudents;
                    compIdWithMaxUnderTwentyStudents = compId;
                }

            }
        }
        return compIdWithMaxUnderTwentyStudents;
    }
}