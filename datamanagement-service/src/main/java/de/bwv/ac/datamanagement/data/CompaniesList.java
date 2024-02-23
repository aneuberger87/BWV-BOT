package de.bwv.ac.datamanagement.data;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

import java.util.ArrayList;
import java.util.List;

@Data
@NoArgsConstructor
@AllArgsConstructor
public class CompaniesList {
    private List<Company> company = new ArrayList<>();

    @Data
    @NoArgsConstructor
    @AllArgsConstructor
    public static class Company {
        private int id;
        private String compName;
        private String trainingOccupation;
        private List<Meeting> meeting = new ArrayList<>();
        private int numberOfMembers;
    }

    @Data
    @NoArgsConstructor
    @AllArgsConstructor
    public static class Meeting {
        private String timeSlot;
        private String room;
    }

    private String errorMessage;
}
