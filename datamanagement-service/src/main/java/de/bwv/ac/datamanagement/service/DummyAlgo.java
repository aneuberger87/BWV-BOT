package de.bwv.ac.datamanagement.service;

import de.bwv.ac.datamanagement.data.CompaniesList;
import de.bwv.ac.datamanagement.data.RoomList;
import de.bwv.ac.datamanagement.data.StudentsList;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Component;
import org.springframework.web.client.RestTemplate;

import java.util.*;

public class DummyAlgo {

    private Map<String, Map<Integer, Integer>> numberStudentsForEventPerTimestampMap = new HashMap<>();
    private Set<StudentsList.Student> studentsWithNotAllWishesSet = new HashSet<>();

    private DataManagementService service;

    public DummyAlgo(DataManagementService service){
        this.service = service;
    }

    public void calculate(){
        eventsRequest();
        studentsRequest();
        service.updateSolutionScore(0.97);
    }

    private void eventsRequest() {
        CompaniesList companiesList = service.getAllCompanies();
        RoomList allRooms = service.getAllRooms();
        List<RoomList.Room> roomList = allRooms.getRoomList();
        int roomindex = 0;

        for (int i = 0; i < companiesList.getCompany().size(); i++) {
            CompaniesList.Company company = companiesList.getCompany().get(i);
            for (CompaniesList.Meeting meeting : company.getMeeting()) {
                String roomNr = roomList.get(getRoomIndexMod(roomindex, roomList.size())).getRoomId();
                meeting.setRoom(new RoomList.Room(roomNr));
            }
            roomindex++;
        }
        service.updateCompaniesList(companiesList);
    }

    private int getRoomIndexMod(int roomindex, int size) {
        return roomindex % size;
    }

    private void studentsRequest() {
        CompaniesList companiesList = service.getAllCompanies();
        StudentsList studentsList = service.getAllStudents();

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
                        if(hasMeetingInTimeslot(Objects.requireNonNull(getCompany(companiesList, verschobeneEvent)), strTimeSlot)){
                            verschobeneEvents.add(compId);
                            compId = verschobeneEvent;
                            verschobeneEvents.remove(verschobeneEvent);
                            break;
                        }
                    }
                }
                if(!hasMeetingInTimeslot(Objects.requireNonNull(getCompany(companiesList, compId)), strTimeSlot)){
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
                        if(hasMeetingInTimeslot(Objects.requireNonNull(getCompany(companiesList, compId)), strTimeslot)){
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
        //service.updateStudentsList(studentsList);
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
