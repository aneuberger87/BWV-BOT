package de.bwv.ac.datamanagement.data;

import lombok.Data;

import java.util.List;


@Data
public class SolutionAttendanceList {

    private List<AttendanceList> attendanceLists;

    @Data
    public static class AttendanceList {

        private String companyName;
        private CompaniesList.Meeting event;
        private List<StudentsList.Student> students;

    }

}
