package de.bwv.ac.datamanagement.data;

import java.util.List;

public class StudentsList {

    private List<Student> student;

    public static class Student {

        private String prename, surname, schoolClass;
        private int[] wishList;
    }

    private String errorMessage;
}