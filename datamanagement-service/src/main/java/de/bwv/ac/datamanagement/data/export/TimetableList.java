package de.bwv.ac.datamanagement.data.export;

import de.bwv.ac.datamanagement.data.CompaniesList;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

import java.util.ArrayList;
import java.util.List;

@Data
@NoArgsConstructor
@AllArgsConstructor
public class TimetableList {

    private List<TimetableOfStudentsFromClass> timetables = new ArrayList<>();

    @Data
    @NoArgsConstructor
    @AllArgsConstructor
    public static class TimetableOfStudentsFromClass {
        private String schoolClass;
        private List<StudentsAllocation> studentsAllocationList = new ArrayList<>();
    }

    @Data
    @NoArgsConstructor
    @AllArgsConstructor
    public static class StudentsAllocation {
        private String prename;
        private String surname;
        private TimeTable timeTable;
    }

    @Data
    @NoArgsConstructor
    @AllArgsConstructor
    public static class TimeTable{
        private List<Rows> rows = new ArrayList<>();

        @Data
        @NoArgsConstructor
        @AllArgsConstructor
        public static class Rows {
            private CompaniesList.Meeting meeting;
            private String companyName;
            private String companyEvent;
            private String numberWish = "-";
        }
    }

    private String errorMessage;
}
