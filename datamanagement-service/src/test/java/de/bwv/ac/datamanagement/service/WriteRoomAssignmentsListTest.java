package de.bwv.ac.datamanagement.service;

import de.bwv.ac.datamanagement.data.CompaniesList;
import de.bwv.ac.datamanagement.data.RoomList;
import de.bwv.ac.datamanagement.service.writer.ExcelWriter;
import de.bwv.ac.datamanagement.service.writer.RoomAssignmentsListWriter;
import org.junit.jupiter.api.Test;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class WriteRoomAssignmentsListTest {

    @Test
    void test() throws IOException {
        DataStorage dataStorage = new DataStorage();
        dataStorage.setCompanies(dummyCompaniesList());
        ExcelWriter writer = new RoomAssignmentsListWriter(dataStorage);
        writer.write("C:/Users/aneub/IdeaProjects/BWV-BOT/datamanagement-service/src/test/resources/out");
    }

    private CompaniesList dummyCompaniesList(){
        CompaniesList companiesList = new CompaniesList();
        List<CompaniesList.Company> companies = new ArrayList<>();
        companies.add(new CompaniesList.Company(1, "Company1", "Something very nice", List.of(
                new CompaniesList.Meeting("A", new RoomList.Room("201")),
                new CompaniesList.Meeting("B", new RoomList.Room("203")),
                new CompaniesList.Meeting("C", new RoomList.Room("202"))), 20
        ));
        companies.add(new CompaniesList.Company(2, "Company2ThisWillBeALongCompanyName", "Something very nice2", List.of(
                new CompaniesList.Meeting("B", new RoomList.Room("201")),
                new CompaniesList.Meeting("C", new RoomList.Room("203")),
                new CompaniesList.Meeting("D", new RoomList.Room("202"))), 20
        ));
        companies.add(new CompaniesList.Company(3, "Company3", "Something very nice3", List.of(
                new CompaniesList.Meeting("A", new RoomList.Room("203")),
                new CompaniesList.Meeting("B", new RoomList.Room("202")),
                new CompaniesList.Meeting("C", new RoomList.Room("201"))), 20
        ));
        companiesList.setCompany(companies);
        return companiesList;
    }

}
