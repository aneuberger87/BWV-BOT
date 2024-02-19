package de.bwv.ac.datamanagement.data;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

import java.util.List;

@Data
@NoArgsConstructor
@AllArgsConstructor
public class StudentsList {

    private List<Student> student;

    @Data
    @NoArgsConstructor
    @AllArgsConstructor
    public static class Student {

        private String prename, surname, schoolClass;
        private List<Wish> wishList;
    }

    @Data
    @NoArgsConstructor
    @AllArgsConstructor
    public static class Wish {
        private int compId;
        private String timeSlot;
    }

    private String errorMessage;
}