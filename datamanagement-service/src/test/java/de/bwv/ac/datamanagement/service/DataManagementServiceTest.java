package de.bwv.ac.datamanagement.service;

import de.bwv.ac.datamanagement.config.Properties;
import de.bwv.ac.datamanagement.data.CompaniesList;
import de.bwv.ac.datamanagement.data.StudentsList;
import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.Test;

import java.sql.DatabaseMetaData;

import static org.junit.jupiter.api.Assertions.*;

class DataManagementServiceTest {

    private static DataStorage dataStorage = new DataStorage();

    @BeforeAll
    public static void setUp(){
        Properties props = new Properties();
        props.setEventlistLocation("src/test/resources/unternehmensliste.xlsx");
        props.setStudentslistLocation("src/test/resources/schuelerliste.xlsx");
        props.setRoomlistLocation("src/test/resources/IMPORT_BOT0_Raumliste.xlsx");
        DataStorageInitializer initializer = new DataStorageInitializer(dataStorage, props);
        initializer.initializeDataStorage();
    }

    @Test
    void getAllCompanies() {
        DataManagementService dataManagementService = new DataManagementService(dataStorage, null);
        CompaniesList allCompanies = dataManagementService.getAllCompanies();
        assertNotNull(allCompanies);
        assertNotNull(allCompanies.getCompany());
        assertNull(allCompanies.getErrorMessage());
        assertEquals(14, allCompanies.getCompany().size());
    }

    @Test
    void getAllStudents() {
        DataManagementService dataManagementService = new DataManagementService(dataStorage, null);
        StudentsList allStudents = dataManagementService.getAllStudents();
        assertNotNull(allStudents);
        assertNotNull(allStudents.getStudent());
        assertNull(allStudents.getErrorMessage());
        assertEquals(180, allStudents.getStudent().size());
    }

    @Test
    void postStudentWishes() {
        //Not implemented yet
    }

    @Test
    void postStudentsList() {
        //Not implemented yet
    }

}