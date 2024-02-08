package de.bwv.ac.datamanagement.data;

import java.util.List;

public class SolutionAnwesenheitsliste {

    List<Items> items;

    public static class Items {

        private String unternehmen; //Name
        private Unternehmensliste.Meeting event;
        private List<Anwesenheitsliste> anwesenheitsliste;

    }

    public class Anwesenheitsliste {

        private String prename, surname, schoolClass;

    }


}
