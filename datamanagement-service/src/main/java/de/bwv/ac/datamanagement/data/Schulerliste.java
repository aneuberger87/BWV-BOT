package de.bwv.ac.datamanagement.data;

import java.util.List;

public class Schulerliste {

    private List<Schueler> student;

    public static class Schueler {

        private String prename, surname, schoolClass;
        private int[] wishList;
    }
}