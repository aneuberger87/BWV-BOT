package de.bwv.ac.datamanagement.service;

import de.bwv.ac.datamanagement.data.CompaniesList;
import de.bwv.ac.datamanagement.data.StudentsList;

import static org.junit.jupiter.api.Assertions.*;

class ExcelReaderTest {

    @org.junit.jupiter.api.Test
    void readStudentsList() {
        ExcelReader excelReader = new ExcelReader();
        StudentsList studentsList =
                excelReader.readStudentsList("src/test/resources/schuelerliste.xlsx");
        assertNotNull(studentsList);
        assertEquals(135, studentsList.getStudent().size());
        assertNull(studentsList.getErrorMessage());
    }

    @org.junit.jupiter.api.Test
    void readCompaniesList() {
        ExcelReader excelReader = new ExcelReader();
        CompaniesList companiesList =
                excelReader.readCompaniesList("src/test/resources/unternehmensliste.xlsx");
        assertNotNull(companiesList);
        assertEquals(26, companiesList.getCompany().size());
        assertNull(companiesList.getErrorMessage());
    }
}