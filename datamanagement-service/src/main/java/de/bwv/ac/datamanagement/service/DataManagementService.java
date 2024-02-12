package de.bwv.ac.datamanagement.service;

import de.bwv.ac.datamanagement.data.StudentsList;
import de.bwv.ac.datamanagement.data.CompaniesList;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class DataManagementService {

    @GetMapping("/companies")
    public CompaniesList getAllCompanies(){
        //TODO: Returns the company-List as JSON
        //companies with timeslots
        return null;
    }

    @GetMapping("/students")
    public StudentsList getAllStudents(){
        //TODO: Returns the pupils-List as JSON
        //Pupils with preferences
        return null;
    }



}
