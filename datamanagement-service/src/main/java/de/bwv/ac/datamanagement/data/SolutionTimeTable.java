package de.bwv.ac.datamanagement.data;

import lombok.Data;

@Data
public class SolutionTimeTable {

    private SolutionAttendanceList.Student student;
    private TimeTable timeTable;

    @Data
    public static class TimeTable {
        private CompaniesList.Meeting timeSlotRoomInfo;
        private String eventName;
        private String companyName;
    }

}
