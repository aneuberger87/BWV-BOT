package de.bwv.ac.datamanagement.service;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;
import de.bwv.ac.datamanagement.data.CompaniesList;
import de.bwv.ac.datamanagement.data.RoomList;
import de.bwv.ac.datamanagement.data.StudentsList;
import lombok.Data;

import java.util.*;

public class RoomAssignmentAlgorithm {

    private DataStorage dataStorage;
    private ObjectMapper objectMapper = new ObjectMapper();

    private List<StudentsList.Student> studentData = new ArrayList<>();
    private List<RoomList.Room> roomData = new ArrayList<>();

    private Map<String, RoomAssignment> roomAssignmentsMap = new HashMap<>();
    private List<CompaniesList.Company> eventData = new ArrayList<>();

    public RoomAssignmentAlgorithm(DataStorage dataStorage){
        this.dataStorage = dataStorage;
        studentData.addAll(dataStorage.getStudentsWishList().getStudent());
        roomData.addAll(dataStorage.getRoomList().getRoomList());
        eventData.addAll(dataStorage.getCompaniesList().getCompany());
    }

    public void calculate() throws JsonProcessingException {
        allocateRooms();
        //eventsRequest();
    }

    public void allocateRooms() throws JsonProcessingException {

        initializeRoomAssigmentMap();
        //Roomdaten per Kapazität sortieren (von groß nach klein)(probieren)
        roomData = sortRoomsPerCapacity();
        //Eventdaten nach maxTeilnehmer sortieren (von groß nach klein)(probieren)
        eventData = sortEventsPerNumberParticipants();

        for(CompaniesList.Company company : eventData){
            fillNotSetMeetingsWithNull(company);
        }

        for(CompaniesList.Company event : eventData){
            //Wieviele Leute haben wollen die Veranstaltung insgesammt hören
            int anzahlInteressenten = countEventInterest(event);
            //Reale Teilnahmeranzahl (setze Veranstaltungsteilnehmerozahl min(interessenten, teilnehmeranzahl veranstaltung))
            int effectiveNumberOfParticipants = calculateEffectiveNumberOfParticipants(anzahlInteressenten, event.getNumberOfMembers());
            event.setNumberOfMembers(effectiveNumberOfParticipants);
            for(RoomList.Room room : roomData){
                //Wie viele Events müssen laufen um alle Wünsche zu erfüllen
                int effectivNumberOfEvents = Math.min(calculateNumberOfHeldEventsNeeded(anzahlInteressenten, effectiveNumberOfParticipants, room), event.getMeeting().size());
                if(assignRoomForEvent(room, event, effectivNumberOfEvents, event.getMeeting().get(0).getTimeSlot(), event.getMeeting().get(event.getMeeting().size()-1).getTimeSlot())){
                    event.getMeeting().removeIf(meeting -> meeting.getRoom() == null);
                    break;
                }
            }

        }
        List<RoomAssignment> sortedRoomAssignment = new ArrayList<>(roomAssignmentsMap.values());
        sortedRoomAssignment.sort((a, b) -> Integer.compare(b.getRoom().getCapacity(), a.getRoom().getCapacity()));

        for(RoomAssignment roomAssignment : sortedRoomAssignment){
            if(roomHasFreeSlots(roomAssignment)){
                assignFreeRoomSlots(roomAssignment);
            }
        }

        //Alle Zeitslots auffüllen (falls nicht gesetzt soll die compId = null gesetzt werden)

        for(CompaniesList.Company company: eventData){
            company.getMeeting().removeIf(meeting -> meeting.getRoom() == null);
            //fillNotSetMeetingsWithNull(company);
        }

        //Speichere Daten
        String json = objectMapper.writeValueAsString(eventData);
        System.out.println(json);
        dataStorage.setCompanies(new CompaniesList(eventData, null));
    }

    private void fillNotSetMeetingsWithNull(CompaniesList.Company company) {
        if(company.getMeeting().size() < 5){
            if(!hasTimeSlot("A",company.getMeeting())){
                company.getMeeting().add(0, new CompaniesList.Meeting("A", null));
            }
            if(!hasTimeSlot("B", company.getMeeting())){
                company.getMeeting().add(1, new CompaniesList.Meeting("B", null));
            }
            if(!hasTimeSlot("C", company.getMeeting())){
                company.getMeeting().add(2, new CompaniesList.Meeting("C", null));
            }
            if(!hasTimeSlot("D", company.getMeeting())){
                company.getMeeting().add(3, new CompaniesList.Meeting("D", null));
            }
            if(!hasTimeSlot("E", company.getMeeting())){
                company.getMeeting().add(4, new CompaniesList.Meeting("E", null));
            }
        }
    }

    private boolean hasTimeSlot(String timeSlot, List<CompaniesList.Meeting> meeting) {
        for(CompaniesList.Meeting m : meeting){
            if(m.getTimeSlot().equals(timeSlot)){
                return true;
            }
        }
        return false;
    }

    private boolean roomHasFreeSlots(RoomAssignment roomAssignment) {
        for(int eventId : roomAssignment.getAssignment().values()){
            if(eventId < 0){
                return true;
            }
        }
        return false;
    }

    private void assignFreeRoomSlots(RoomAssignment roomAssignment) {
        int anzahlPlaetzeFuerEventHinzugekommen = 0;
        int firstTimeSlot = "A".trim().charAt(0);
        for(int i = 0; i < 5; i++){
            if(roomAssignment.getAssignment().get(Character.toString(firstTimeSlot+i)) == -1){
                for (int j = 0; j < eventData.size(); j++) {
                    if(getRoomForEventOfTimeSlot(eventData.get(j).getMeeting(), firstTimeSlot+i) == null){
                        assignRoomForEvent(roomAssignment.getRoom(), eventData.get(j), 1, Character.toString(firstTimeSlot+i), Character.toString(firstTimeSlot+i));
                        break;
                    }
                }
            }
        }
    }

    private String getRoomForEventOfTimeSlot(List<CompaniesList.Meeting> meeting, int timeSlot) {
        String timeSlotAsString = Character.toString(timeSlot);
        for(CompaniesList.Meeting m : meeting){
            if(m.getTimeSlot().equals(timeSlotAsString)){
                return m.getRoom() == null ? null : m.getRoom().getRoomId();
            }
        }
        return "existiert nicht"; //Null ist schon für nicht gesetzte Räume vergeben.
    }

    private int assignRoomForEventIfATimeslotMatches(RoomAssignment roomAssignment, CompaniesList.Company event) {
        int anzahlPlaetzeFuerEventHinzugekommen = 0;
        int firstTimeSlot = "A".trim().charAt(0);
        for(int i = 0; i < 5; i++){
            if(roomAssignment.getAssignment().get(Character.toString(firstTimeSlot+i)) == -1
                    && event.getMeeting().size() > i
                    && event.getMeeting().get(i).getRoom() == null){
                assignRoomForEvent(roomAssignment.getRoom(), event, 1, Character.toString(firstTimeSlot+i), Character.toString(firstTimeSlot+i));

                anzahlPlaetzeFuerEventHinzugekommen += Math.min(event.getNumberOfMembers(), roomAssignment.getRoom().getCapacity());
            }
        }
        return anzahlPlaetzeFuerEventHinzugekommen;
    }

    private boolean assignRoomForEvent(RoomList.Room room, CompaniesList.Company event, int numberOfHeldEventsNeeded, String firstTimeslotOfEvent, String lastTimeslotOfEvent) {
        RoomAssignment roomAssignment = roomAssignmentsMap.get(room.getRoomId());
        //addEventsForRoomAssignment(roomAssignment, timeSlots);
        int counter = 0;
        int firstTimeSlot = firstTimeslotOfEvent.trim().charAt(0);
        int lastTimeSlot = lastTimeslotOfEvent.trim().charAt(0);
        int lastIndex = Math.min(lastTimeSlot, firstTimeSlot+numberOfHeldEventsNeeded);
        for(int i = firstTimeSlot; i <= lastIndex; i++){
            String timeSlotOnI = Character.toString(i);
            if(roomAssignment.getAssignment().get(timeSlotOnI) == -1){
                counter++;
                if(counter >= numberOfHeldEventsNeeded){
                    //Room found for Event
                    addEventsForRoomAssignment(roomAssignment, Character.toString((i+1)-counter), numberOfHeldEventsNeeded , event.getId());
                    assignRoomForTimeslot(event, room);
                    return true;
                }
            } else {
                counter = 0;
            }

        }
        return false;
    }


    private int calculateEffectiveNumberOfParticipants(int anzahlInteressenten, int numberOfMembers) {
        return Math.min(anzahlInteressenten, numberOfMembers);
    }

    private void addEventsForRoomAssignment(RoomAssignment roomAssignment, String firstTimeslot, int numberOfHeldEventsNeeded, int event) {
        int firstTimeSlot = firstTimeslot.trim().charAt(0);
        for(int i = 0; i < numberOfHeldEventsNeeded; i++){
            roomAssignment.getAssignment().put(Character.toString(firstTimeSlot+i), event);
        }
    }

    private void assignRoomForTimeslot(CompaniesList.Company event, RoomList.Room roomForEvent) {
        RoomAssignment roomAssignment = roomAssignmentsMap.get(roomForEvent.getRoomId());
        int firstTimeSlot = getFirstTimeSlotWithEventId(roomAssignment, event.getId());
        int lastTimeSlot = getLastTimeSlotWithEventId(roomAssignment, event.getId())-1;
        boolean foundStart = false;
        for(CompaniesList.Meeting meeting : event.getMeeting()){
            if(meeting.getTimeSlot().charAt(0) == firstTimeSlot || foundStart){
                foundStart = true;
                meeting.setRoom(roomForEvent);
            }
            if(meeting.getTimeSlot().charAt(0) == lastTimeSlot){
                break;
            }
        }
    }

    private int getLastTimeSlotWithEventId(RoomAssignment roomAssignment, int eventId) {
        int firstTimeSlot = "A".trim().charAt(0);
        for(int i = getFirstTimeSlotWithEventId(roomAssignment, eventId); i < firstTimeSlot+roomAssignment.getAssignment().size(); i++){
            if(roomAssignment.getAssignment().get(Character.toString(i)) != eventId){
                return i;
            }
        }
        return firstTimeSlot+roomAssignment.getAssignment().size();
    }

    private int getFirstTimeSlotWithEventId(RoomAssignment roomAssignment, int eventId) {
        int firstTimeSlot = "A".trim().charAt(0);
        for(int i = 0; i < roomAssignment.getAssignment().size(); i++){
            String timeSlotOnI = Character.toString(firstTimeSlot + i);
            if(roomAssignment.getAssignment().get(timeSlotOnI) == eventId){
                return firstTimeSlot+i;
            }
        }
        return firstTimeSlot+5;
    }

    private void initializeRoomAssigmentMap() {
        for(RoomList.Room room : roomData){
            roomAssignmentsMap.put(room.getRoomId(), new RoomAssignment(room));
        }
    }

    private int calculateNumberOfHeldEventsNeeded(int numberOfInterests, int numberOfParticipants, RoomList.Room room) {
        int capacity = Math.min(room.getCapacity(), numberOfParticipants);
        return (int) Math.ceil(1.* numberOfInterests / capacity);
    }


    private List<CompaniesList.Company> sortEventsPerNumberParticipants() {
        //eventData.sort((a, b) -> Integer.compare(b.getNumberOfMembers(), a.getNumberOfMembers()));
        eventData.sort((a, b) -> Integer.compare(countEventInterest(b),countEventInterest(a)));

        return eventData;
    }

    private List<RoomList.Room> sortRoomsPerCapacity() {
        roomData.sort((a, b) -> Integer.compare(b.getCapacity(), a.getCapacity()));
        return roomData;
    }

    private int countEventInterest(CompaniesList.Company event) {
        int eventId = event.getId();
        int counter = 0;
        if(studentData != null){
            for(StudentsList.Student student : studentData){
                for(StudentsList.Wish wish : student.getWishList()){
                    if(wish.getCompId() == eventId){
                        counter++;
                        break;
                    }
                }
            }
        }
        return counter;

    }


    @Data
    private static class RoomAssignment {
        private RoomList.Room room;
        private Map<String, Integer> assignment = new HashMap<>();

        public RoomAssignment(RoomList.Room room){
            this.room = room;
            assignment.put("A", -1);
            assignment.put("B", -1);
            assignment.put("C", -1);
            assignment.put("D", -1);
            assignment.put("E", -1);
        }
    }

}
