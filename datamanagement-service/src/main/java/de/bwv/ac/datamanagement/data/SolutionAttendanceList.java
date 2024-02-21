package de.bwv.ac.datamanagement.data;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

import java.util.List;


@Data
@NoArgsConstructor
@AllArgsConstructor
public class SolutionAttendanceList {

    private List<AttendanceList> attendanceLists;

    @Data
    @NoArgsConstructor
    @AllArgsConstructor
    public static class AttendanceList {

        private String companyName;
        private CompaniesList.Meeting event;
        private List<StudentsList.Student> students;

    }

    private String errorMessage;

}
