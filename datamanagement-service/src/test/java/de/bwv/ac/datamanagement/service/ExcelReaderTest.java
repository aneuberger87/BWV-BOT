package de.bwv.ac.datamanagement.service;

import de.bwv.ac.datamanagement.data.CompaniesList;
import de.bwv.ac.datamanagement.data.StudentsList;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.List;

import static org.junit.jupiter.api.Assertions.*;

class ExcelReaderTest {

    @Test
    void readStudentsList() {
        ExcelReader excelReader = new ExcelReader();
        StudentsList studentsList =
                excelReader.readStudentsList("src/test/resources/schuelerliste.xlsx");
        assertNotNull(studentsList);
        assertEquals(180, studentsList.getStudent().size());

        List<StudentsList.Student> students = studentsList.getStudent();
        //Check First Student: Class = RosyBrown3, surname = Li; prename = Kenneth
        StudentsList.Student student1 = new StudentsList.Student("Kenneth", "Li", "RosyBrown3", new ArrayList<>());
        assertEquals(student1, students.get(0));

        //Check Last Student: Class = DodgerBlue3, surname = Daniels, prename = Olivia
        StudentsList.Student student2 = new StudentsList.Student("Olivia", "Daniels", "DodgerBlue3", new ArrayList<>());
        assertEquals(student2, students.get(students.size()-1));

        //Keine besonders zu betrachtenden Daten in der Schülerliste vorhanden
        assertNull(studentsList.getErrorMessage());
    }

    //TODO: Methode zum Erstellen der Companies und Meetings auslagern
    @Test
    void readCompaniesList() {
        ExcelReader excelReader = new ExcelReader();
        CompaniesList companiesList =
                excelReader.readEventList("src/test/resources/unternehmensliste.xlsx");
        assertNotNull(companiesList);
        assertEquals(14, companiesList.getCompany().size());
        assertNull(companiesList.getErrorMessage());

        //Check First Entry: Id = 1, name = "Mack, Chase and Salazar", Fachrichtung = "Health service manager", Teilnehmer = 20, Veranstaltungen = 3, Frühester Zeitpunkt = B
        CompaniesList.Company company1 = new CompaniesList.Company();
        company1.setId(1);
        company1.setCompName("Mack, Chase and Salazar");
        company1.setTrainingOccupation("Health service manager");
        company1.setNumberOfMembers(20);
        ArrayList<CompaniesList.Meeting> meetings1 = new ArrayList<>();
        //drei Veranstaltungen beginnend im Timeslot B
        CompaniesList.Meeting meeting1 = new CompaniesList.Meeting("B", null);
        CompaniesList.Meeting meeting2 = new CompaniesList.Meeting("C", null);
        CompaniesList.Meeting meeting3 = new CompaniesList.Meeting("D", null);
        meetings1.add(meeting1);
        meetings1.add(meeting2);
        meetings1.add(meeting3);
        company1.setMeeting(meetings1);
        assertEquals(company1, companiesList.getCompany().get(0));

        //Check Last Entry: Id = 14, name = "Carpenter LLC", Fachrichtung = "Purchasing manager", Teilnehmer = 20, Veranstaltungen = 4, Frühester Zeitpunkt = A
        CompaniesList.Company company2 = new CompaniesList.Company();
        company2.setId(14);
        company2.setCompName("Carpenter LLC");
        company2.setTrainingOccupation("Purchasing manager");
        company2.setNumberOfMembers(20);
        ArrayList<CompaniesList.Meeting> meetings2 = new ArrayList<>();
        //vier Veranstaltungen beginnend im Timeslot A
        CompaniesList.Meeting meeting1_2 = new CompaniesList.Meeting("A", null);
        CompaniesList.Meeting meeting2_2 = new CompaniesList.Meeting("B", null);
        CompaniesList.Meeting meeting3_2 = new CompaniesList.Meeting("C", null);
        CompaniesList.Meeting meeting4_2 = new CompaniesList.Meeting("D", null);
        meetings2.add(meeting1_2);
        meetings2.add(meeting2_2);
        meetings2.add(meeting3_2);
        meetings2.add(meeting4_2);
        company2.setMeeting(meetings2);
        assertEquals(company2, companiesList.getCompany().get(companiesList.getCompany().size()-1));

        //Check special Entry: Id = 9, name = "Palmer Group", Fachrichtung = "", Teilnehmer = 20, Veranstaltungen = 3, Frühester Zeitpunkt = A
        CompaniesList.Company company3 = new CompaniesList.Company();
        company3.setId(9);
        company3.setCompName("Palmer Group");
        company3.setTrainingOccupation("");
        company3.setNumberOfMembers(20);
        ArrayList<CompaniesList.Meeting> meetings3 = new ArrayList<>();
        //vier Veranstaltungen beginnend im Timeslot A
        CompaniesList.Meeting meeting1_3 = new CompaniesList.Meeting("A", null);
        CompaniesList.Meeting meeting2_3 = new CompaniesList.Meeting("B", null);
        CompaniesList.Meeting meeting3_3 = new CompaniesList.Meeting("C", null);
        meetings3.add(meeting1_3);
        meetings3.add(meeting2_3);
        meetings3.add(meeting3_3);
        company3.setMeeting(meetings3);
        assertEquals(company3, companiesList.getCompany().get(8));
    }
}