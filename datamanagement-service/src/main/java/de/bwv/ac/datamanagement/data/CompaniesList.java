package de.bwv.ac.datamanagement.data;

import lombok.Data;

import java.util.List;

@Data
public class CompaniesList {
    private List<Company> company;

    @Data
    public static class Company {
        int id;
        String compName;
        String trainingOccupation;
        List<Meeting> meeting;
    }

    @Data
    public static class Meeting {
        char timeSlot;
        String room;
    }

    private String errorMessage;
}
