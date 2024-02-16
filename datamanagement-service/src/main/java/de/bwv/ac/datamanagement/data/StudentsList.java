package de.bwv.ac.datamanagement.data;

import lombok.Data;

import java.util.List;

@Data
public class StudentsList {

    private List<Student> student;

    @Data
    public static class Student {

        private String prename, surname, schoolClass;
        private Wish[] wishList;
    }

    @Data
    public static class Wish {
        private int compId;
        private char timeSlot;
    }

    private String errorMessage;
}