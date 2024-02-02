package de.bwv.ac.datamanagement.service;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class DataManagementService {

    @GetMapping("/companies")
    public String getAllCompanies(){
        //TODO: Returns the company-List as JSON
        //companies with timeslots
        return "";
    }

    @GetMapping("/pupils")
    public String getAllPupils(){
        //TODO: Returns the pupils-List as JSON
        //Pupils with preferences
        return "";
    }



}
