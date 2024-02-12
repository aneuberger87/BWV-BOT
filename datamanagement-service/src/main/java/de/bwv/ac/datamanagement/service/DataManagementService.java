package de.bwv.ac.datamanagement.service;

import de.bwv.ac.datamanagement.data.StudentsList;
import de.bwv.ac.datamanagement.data.CompaniesList;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class DataManagementService { //TODO implement

    @GetMapping("/companies")
    public CompaniesList getAllCompanies(){
        return null;
    }

    @GetMapping("/students")
    public StudentsList getAllStudents(){
        return null;
    }

    @PostMapping("/students/wishes")
    public void postStudentWishes(String studentWishesAsJSON){

    }


}
