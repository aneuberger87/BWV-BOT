package de.bwv.ac.datamanagement.data;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

import java.util.ArrayList;
import java.util.List;

@Data
public class RoomList {
    private List<Room> roomList = new ArrayList<>();

    @Data
    @NoArgsConstructor
    public static class Room {
        private String roomId;
        private int capacity = 20;

        public Room(String roomId){
            this.roomId = roomId;
        }
    }

    private String errorMessage;
}
