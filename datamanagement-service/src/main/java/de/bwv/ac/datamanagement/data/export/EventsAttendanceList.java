package de.bwv.ac.datamanagement.data.export;

import de.bwv.ac.datamanagement.data.CompaniesList;
import de.bwv.ac.datamanagement.data.StudentsList;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

import java.util.ArrayList;
import java.util.List;


@Data
@NoArgsConstructor
@AllArgsConstructor
public class EventsAttendanceList {

    private List<AttendanceListsPerCompany> AttendanceListsPerCompany;

    @Data
    @NoArgsConstructor
    @AllArgsConstructor
    public static class AttendanceListsPerCompany {
        private CompaniesList.Company company;
        private List<AttendanceList> attendanceList;
    }

    @Data
    @NoArgsConstructor
    @AllArgsConstructor
    public static class AttendanceList {
        private String companyName;
        private CompaniesList.Meeting event;
        private List<StudentsList.Student> students = new ArrayList<>();

    }

    private String errorMessage;

}
