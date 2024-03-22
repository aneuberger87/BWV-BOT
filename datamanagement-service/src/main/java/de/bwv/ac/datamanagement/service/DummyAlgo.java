package de.bwv.ac.datamanagement.service;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;
import de.bwv.ac.datamanagement.data.CompaniesList;
import de.bwv.ac.datamanagement.data.RoomList;
import de.bwv.ac.datamanagement.data.SolutionScore;
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
    private ObjectMapper objectMapper = new ObjectMapper();

    public DummyAlgo(DataManagementService service){
        this.service = service;
    }

    public void calculate() throws JsonProcessingException {
        eventsRequest();
    }

    private void eventsRequest() throws JsonProcessingException {
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
        String json = objectMapper.writeValueAsString(companiesList);
        service.updateCompaniesList(json);
    }

    private int getRoomIndexMod(int roomindex, int size) {
        return roomindex % size;
    }

}
