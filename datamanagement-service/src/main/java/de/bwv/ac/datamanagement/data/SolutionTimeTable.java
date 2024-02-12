package de.bwv.ac.datamanagement.data;

import lombok.Data;

import java.util.List;

@Data
public class SolutionTimeTable {

    public List<Item> items;

    @Data
    public static class Item {
        private SolutionAttendanceList.Student student;
        private TimeTable timeTable;
    }
    @Data
    public static class TimeTable {
        private CompaniesList.Meeting timeSlotRoomInfo;
        private String eventName;
        private String companyName;
    }

}
