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
        DataManagementService dataManagementService = new DataManagementService(dataStorage);
        CompaniesList allCompanies = dataManagementService.getAllCompanies();
        assertNotNull(allCompanies);
        assertNotNull(allCompanies.getCompany());
        assertNull(allCompanies.getErrorMessage());
        assertEquals(14, allCompanies.getCompany().size());
    }

    @Test
    void getAllStudents() {
        DataManagementService dataManagementService = new DataManagementService(dataStorage);
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

    @Test
    void getAllDummyStudents() {
        DataManagementService dataManagementService = new DataManagementService(dataStorage);
        StudentsList allDummyStudents = dataManagementService.getAllDummyStudents();
        assertNotNull(allDummyStudents);
        assertNotNull(allDummyStudents.getStudent());
        assertNull(allDummyStudents.getErrorMessage());
        assertEquals(3, allDummyStudents.getStudent().size());
        allDummyStudents.getStudent().forEach( student -> assertTrue(student.getWishList().isEmpty()));
    }

    @Test
    void getAllDummyStudentsWithWishes() {
        DataManagementService dataManagementService = new DataManagementService(dataStorage);
        StudentsList allDummyStudents = dataManagementService.getAllDummyStudentsWithWishes();
        assertNotNull(allDummyStudents);
        assertNotNull(allDummyStudents.getStudent());
        assertNull(allDummyStudents.getErrorMessage());
        assertEquals(3, allDummyStudents.getStudent().size());
        allDummyStudents.getStudent().forEach( student -> assertFalse(student.getWishList().isEmpty()));
    }

    @Test
    void getAllDummyCompaniesWithRoomsAndTimeslots() {
        DataManagementService dataManagementService = new DataManagementService(dataStorage);
        CompaniesList allDummyCompanies = dataManagementService.getAllDummyCompaniesWithRoomsAndTimeslots();
        assertNotNull(allDummyCompanies);
        assertNotNull(allDummyCompanies.getCompany());
        assertFalse(allDummyCompanies.getCompany().isEmpty());
        assertEquals(3, allDummyCompanies.getCompany().size());
        for (CompaniesList.Company company : allDummyCompanies.getCompany()) {
            assertFalse(company.getMeeting().isEmpty());
        }
        assertNull(allDummyCompanies.getErrorMessage());
    }

    @Test
    void getAllDummyCompanies() {
        DataManagementService dataManagementService = new DataManagementService(dataStorage);
        CompaniesList allDummyCompanies = dataManagementService.getAllDummyCompanies();
        assertNotNull(allDummyCompanies);
        assertNotNull(allDummyCompanies.getCompany());
        assertFalse(allDummyCompanies.getCompany().isEmpty());
        for (CompaniesList.Company company : allDummyCompanies.getCompany()) {
            assertTrue(company.getMeeting().isEmpty());
        }
        assertEquals(3, allDummyCompanies.getCompany().size());
        assertNull(allDummyCompanies.getErrorMessage());
    }
}