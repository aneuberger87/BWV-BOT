package de.bwv.ac.datamanagement.service;

import de.bwv.ac.datamanagement.data.CompaniesList;
import de.bwv.ac.datamanagement.data.RoomList;
import de.bwv.ac.datamanagement.data.StudentsList;
import de.bwv.ac.datamanagement.data.export.EventsAttendanceList;
import de.bwv.ac.datamanagement.service.writer.AttendanceListWriter;
import org.junit.jupiter.api.Test;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class EventAttendanceListWriterTest {

    @Test
    void test() throws IOException {
        EventsAttendanceList eventsAttendanceList = createDummyEventAttendanceList();
        AttendanceListWriter writer = new AttendanceListWriter(new DataStorage());
        writer.writeEventsAttendanceList(eventsAttendanceList, "C:/Users/aneub/IdeaProjects/BWV-BOT/datamanagement-service/src/test/resources/out");

    }

    private EventsAttendanceList createDummyEventAttendanceList() {
        EventsAttendanceList result = new EventsAttendanceList();
        List<EventsAttendanceList.AttendanceList> attendanceLists = new ArrayList<>();
        EventsAttendanceList.AttendanceList attendanceList = new EventsAttendanceList.AttendanceList();
        attendanceList.setCompanyName("Company 1");
        attendanceList.setEvent(new CompaniesList.Meeting("A", new RoomList.Room("203")));
        attendanceList.setStudents(List.of(
                new StudentsList.Student("Heinz", "Jupiter", "AlphaCut", List.of(new StudentsList.Wish(1, "A"), new StudentsList.Wish(2, "B"), new StudentsList.Wish(3, "C"))),
                new StudentsList.Student("Peter", "Pan", "AlphaCut", List.of(new StudentsList.Wish(1, "A"), new StudentsList.Wish(2, "B"), new StudentsList.Wish(3, "C"))),
                new StudentsList.Student("John", "Doe", "BetaTest", List.of(new StudentsList.Wish(1, "A"), new StudentsList.Wish(2, "B"), new StudentsList.Wish(3, "C"))),
                new StudentsList.Student("Max", "Mustermann", "GammaStrahl", List.of(new StudentsList.Wish(1, "A"), new StudentsList.Wish(2, "B"), new StudentsList.Wish(3, "C"))),
                new StudentsList.Student("Bernd", "Atlantis", "DeltaX", List.of(new StudentsList.Wish(1, "A"), new StudentsList.Wish(2, "B"), new StudentsList.Wish(3, "C")))
        ));
        attendanceLists.add(attendanceList);

        EventsAttendanceList.AttendanceList attendanceList1 = new EventsAttendanceList.AttendanceList();
        attendanceList1.setCompanyName("Company 1");
        attendanceList1.setEvent(new CompaniesList.Meeting("B", new RoomList.Room("104")));
        attendanceList1.setStudents(List.of(
                new StudentsList.Student("John", "Doe", "BetaTest", List.of(new StudentsList.Wish(1, "A"), new StudentsList.Wish(2, "B"), new StudentsList.Wish(3, "C"))),
                new StudentsList.Student("Max", "Mustermann", "GammaStrahl", List.of(new StudentsList.Wish(1, "A"), new StudentsList.Wish(2, "B"), new StudentsList.Wish(3, "C"))),
                new StudentsList.Student("Bernd", "Atlantis", "DeltaX", List.of(new StudentsList.Wish(1, "A"), new StudentsList.Wish(2, "B"), new StudentsList.Wish(3, "C")))
        ));
        attendanceLists.add(attendanceList1);

        List<EventsAttendanceList.AttendanceListsPerCompany> attendanceListsPerCompanyList = new ArrayList<>();

        EventsAttendanceList.AttendanceListsPerCompany attendancePerCompany = new EventsAttendanceList.AttendanceListsPerCompany();
        attendancePerCompany.setAttendanceList(attendanceLists);
        attendancePerCompany.setCompany(
                new CompaniesList.Company(1, "Company 1", "Something very nice", List.of(
                        new CompaniesList.Meeting("A", new RoomList.Room("203")),
                        new CompaniesList.Meeting("B", new RoomList.Room("104")),
                        new CompaniesList.Meeting("C", new RoomList.Room("108"))), 20));
       // result.setAttendanceListsPerCompany();
        attendanceListsPerCompanyList.add(attendancePerCompany);

        List<EventsAttendanceList.AttendanceList> attendanceLists2 = new ArrayList<>();
        EventsAttendanceList.AttendanceList attendanceList2 = new EventsAttendanceList.AttendanceList();
        attendanceList2.setCompanyName("Company 2");
        attendanceList2.setEvent(new CompaniesList.Meeting("B", new RoomList.Room("208")));
        attendanceList2.setStudents(List.of(
                new StudentsList.Student("Heinz", "Jupiter", "AlphaCut", List.of(new StudentsList.Wish(1, "A"), new StudentsList.Wish(2, "B"), new StudentsList.Wish(3, "C"))),
                new StudentsList.Student("Peter", "Pan", "AlphaCut", List.of(new StudentsList.Wish(1, "A"), new StudentsList.Wish(2, "B"), new StudentsList.Wish(3, "C"))),
                new StudentsList.Student("John", "Doe", "BetaTest", List.of(new StudentsList.Wish(1, "A"), new StudentsList.Wish(2, "B"), new StudentsList.Wish(3, "C"))),
                new StudentsList.Student("Max", "Mustermann", "GammaStrahl", List.of(new StudentsList.Wish(1, "A"), new StudentsList.Wish(2, "B"), new StudentsList.Wish(3, "C"))),
                new StudentsList.Student("Bernd", "Atlantis", "DeltaX", List.of(new StudentsList.Wish(1, "A"), new StudentsList.Wish(2, "B"), new StudentsList.Wish(3, "C")))
        ));
        attendanceLists2.add(attendanceList2);

        EventsAttendanceList.AttendanceListsPerCompany attendancePerCompany2 = new EventsAttendanceList.AttendanceListsPerCompany();
        attendancePerCompany2.setAttendanceList(attendanceLists2);
        attendancePerCompany2.setCompany(
                new CompaniesList.Company(2, "Company 2", "Something very nice", List.of(
                        new CompaniesList.Meeting("B", new RoomList.Room("208")),
                        new CompaniesList.Meeting("C", new RoomList.Room("108"))), 20));

        attendanceListsPerCompanyList.add(attendancePerCompany2);
        result.setAttendanceListsPerCompany(attendanceListsPerCompanyList);
        return result;
    }

}
