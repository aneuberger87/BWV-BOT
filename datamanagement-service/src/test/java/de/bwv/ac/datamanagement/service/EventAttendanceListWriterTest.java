package de.bwv.ac.datamanagement.service;

import de.bwv.ac.datamanagement.data.CompaniesList;
import de.bwv.ac.datamanagement.data.RoomList;
import de.bwv.ac.datamanagement.data.StudentsList;
import de.bwv.ac.datamanagement.service.writer.AttendanceListWriter;
import org.junit.jupiter.api.Test;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class EventAttendanceListWriterTest {

    private DataStorage dataStorage = new DataStorage();

    @Test
    void test() throws IOException {
        setDummies();
        AttendanceListWriter writer = new AttendanceListWriter(dataStorage);
        writer.write("C:/Users/aneub/IdeaProjects/BWV-BOT/datamanagement-service/src/test/resources/out");

    }

    private void setTestData(){

    }

    private void setDummies() {
        setDummyCompanies();
        setDummyStudents();
    }

    private void setDummyStudents() {
        List<StudentsList.Student> students = new ArrayList<>();
        students.addAll(List.of(new StudentsList.Student("Heinz", "Jupiter", "AlphaCut", List.of(new StudentsList.Wish(1, "A"), new StudentsList.Wish(2, "B"), new StudentsList.Wish(1, "C"))),
                new StudentsList.Student("Peter", "Pan", "AlphaCut", List.of(new StudentsList.Wish(1, "A"), new StudentsList.Wish(2, "B"), new StudentsList.Wish(1, "C"))),
                new StudentsList.Student("John", "Doe", "BetaTest", List.of(new StudentsList.Wish(1, "A"), new StudentsList.Wish(2, "B"), new StudentsList.Wish(1, "C"))),
                new StudentsList.Student("Max", "Mustermann", "GammaStrahl", List.of(new StudentsList.Wish(1, "A"), new StudentsList.Wish(2, "B"), new StudentsList.Wish(3, "C"))),
                new StudentsList.Student("Bernd", "Atlantis", "DeltaX", List.of(new StudentsList.Wish(1, "A"), new StudentsList.Wish(2, "B"), new StudentsList.Wish(3, "C")))));

        dataStorage.setStudentsList(new StudentsList(students, null));
    }

    private void setDummyCompanies() {
        List<CompaniesList.Company> companies = new ArrayList<>();
        companies.add(new CompaniesList.Company(1, "Company 1", "Something very nice", List.of(
                new CompaniesList.Meeting("A", new RoomList.Room("203")),
                new CompaniesList.Meeting("B", new RoomList.Room("104")),
                new CompaniesList.Meeting("C", new RoomList.Room("108"))), 20));
        companies.add(new CompaniesList.Company(2, "Company 2", "Something very nice", List.of(
                new CompaniesList.Meeting("B", new RoomList.Room("208")),
                new CompaniesList.Meeting("C", new RoomList.Room("108"))), 20));
        dataStorage.setCompanies(new CompaniesList(companies, null));
    }


}
