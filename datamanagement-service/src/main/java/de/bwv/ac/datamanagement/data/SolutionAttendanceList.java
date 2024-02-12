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
        private List<Student> students;

    }

    @Data
    public static class Student {
        private String prename, surname, schoolClass;

    }


}
