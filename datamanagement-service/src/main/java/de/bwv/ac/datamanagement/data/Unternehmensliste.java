package de.bwv.ac.datamanagement.data;

import java.util.List;

public class Unternehmensliste {
    private List<Company> company;

    public static class Company {
        int id;
        String compName;
        String trainingOccupation;
        List<Meeting> meeting;
    }

    public static class Meeting {
        String timeSlot;
        String room;
    }
}
