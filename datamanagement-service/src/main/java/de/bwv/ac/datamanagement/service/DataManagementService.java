package de.bwv.ac.datamanagement.service;

import de.bwv.ac.datamanagement.data.Schulerliste;
import de.bwv.ac.datamanagement.data.Unternehmensliste;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class DataManagementService {

    @GetMapping("/companies")
    public Unternehmensliste getAllCompanies(){
        //TODO: Returns the company-List as JSON
        //companies with timeslots
        return null;
    }

    @GetMapping("/students")
    public Schulerliste getAllStudents(){
        //TODO: Returns the pupils-List as JSON
        //Pupils with preferences
        return null;
    }



}
