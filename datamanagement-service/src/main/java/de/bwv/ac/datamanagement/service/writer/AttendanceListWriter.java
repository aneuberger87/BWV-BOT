package de.bwv.ac.datamanagement.service.writer;

import de.bwv.ac.datamanagement.data.StudentsList;
import de.bwv.ac.datamanagement.data.export.EventsAttendanceList;
import de.bwv.ac.datamanagement.service.DataStorage;
import lombok.extern.slf4j.Slf4j;
import org.dhatim.fastexcel.BorderStyle;
import org.dhatim.fastexcel.Workbook;
import org.dhatim.fastexcel.Worksheet;

import java.io.IOException;
import java.io.OutputStream;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.List;

@Slf4j
public class AttendanceListWriter extends ExcelWriter{

    public AttendanceListWriter(DataStorage dataStorage) {
        super(dataStorage);
    }

    @Override
    public void write(String fileLocation) throws IOException {
        writeEventsAttendanceList(getDataStorage().calculateEventsAttendenceList(), fileLocation);
    }

    public void writeEventsAttendanceList(EventsAttendanceList eventsAttendanceList, String fileDirectory) throws IOException {
        if (eventsAttendanceList.getErrorMessage() != null && !eventsAttendanceList.getErrorMessage().isBlank()) {
            log.warn("Can not write the Attendance-Per-Events-Plan (Reason: {})", eventsAttendanceList.getErrorMessage());
            return;
        }
        String fileLocation = fileDirectory + "/" + "Anwesenheitsliste_pro_Veranstaltung.xlsx";
        Files.deleteIfExists(Paths.get(fileLocation));
        try (OutputStream outputStream = Files.newOutputStream(Paths.get(fileLocation)); Workbook workbook = new Workbook(outputStream, "RaumUndZeitplaner", "1.0")) {
            final int COLUMN_SIZE = 4;
            for (int i = 0; i < eventsAttendanceList.getAttendanceListsPerCompany().size(); i++) {
                String companyName = eventsAttendanceList.getAttendanceListsPerCompany().get(i).getCompanyName();
                int companyId = eventsAttendanceList.getAttendanceListsPerCompany().get(i).getCompanyId();
                Worksheet worksheet = workbook.newWorksheet(companyId+"_"
                        +companyName);
                formatHeadWorksheet(worksheet, COLUMN_SIZE);
                int numberHead = writeHead(worksheet, companyName);
                List<EventsAttendanceList.AttendanceList> allAttendanceListOfCompany = eventsAttendanceList.getAttendanceListsPerCompany().get(i).getAttendanceList();
                int indexTop = numberHead+1;
                for(int k = 0; k < allAttendanceListOfCompany.size(); k++){
                    EventsAttendanceList.AttendanceList attendanceList = allAttendanceListOfCompany.get(k);
                    String roomId = attendanceList.getEvent().getRoom().getRoomId();
                    formatHeaderWorksheet(worksheet, indexTop, COLUMN_SIZE);
                    indexTop = writeHeader(worksheet, attendanceList.getEvent().getTimeSlot(), roomId, indexTop);
                    for (int j = 0; j < attendanceList.getStudents().size(); j++) {
                        formatEntriesWorksheet(worksheet, indexTop, COLUMN_SIZE);
                        writeEntry(attendanceList.getStudents().get(j), worksheet, indexTop); //Zeile 0 ist der Header
                        indexTop++;
                    }
                    indexTop = indexTop+2; //Zwei Zeile frei lassen
                }
            }
        }
    }

    private void writeEntry(StudentsList.Student student, Worksheet worksheet, int row) {
        worksheet.value(row, 0, student.getSchoolClass());
        worksheet.value(row, 1, student.getSurname());
        worksheet.value(row, 2, student.getPrename());
    }

    private void formatHeadWorksheet(Worksheet worksheet, int sizeColumn) {
        worksheet.range(0, 0, 0, 3).style().fontSize(15).bold().merge().wrapText(false).set();
        worksheet.range(1, 0, 1, 3).style().fontSize(14).bold().merge().wrapText(false).set();
        worksheet.range(0, 0, 1, sizeColumn).style().horizontalAlignment("left").wrapText(false).set();
    }

    private void formatHeaderWorksheet(Worksheet worksheet, int indexTop, int sizeColumn){
        worksheet.range(indexTop, 0, indexTop, 1).style().fontSize(12).bold().fillColor("b3daff").borderStyle(BorderStyle.THIN).wrapText(false).set();
        worksheet.range(indexTop+1, 0, indexTop+1, sizeColumn-1).style().fontSize(11).bold().fillColor("b3daff").borderStyle(BorderStyle.THIN).wrapText(false).set();
        worksheet.range(indexTop, 0, indexTop+1, sizeColumn-1).style().horizontalAlignment("left").wrapText(false).set();
    }

    private void formatEntriesWorksheet(Worksheet worksheet, int indexTop, int sizeColumn){
        worksheet.range(indexTop, 0, indexTop, sizeColumn-1).style().borderStyle(BorderStyle.THIN).horizontalAlignment("left").wrapText(false).set();
    }

    private int writeHead(Worksheet worksheet, String companiesName){
        worksheet.value(0, 0, "Anwesenheitsliste");
        worksheet.value(1, 0, companiesName);
        return 2;
    }

    private int writeHeader(Worksheet worksheet, String timeSlot, String roomId, int indexTop) {
        worksheet.value(indexTop, 0, getTime(timeSlot));
        worksheet.value(indexTop, 1, "Raum: "+roomId);
        worksheet.value(indexTop+1, 0, "Klasse");
        worksheet.value(indexTop+1, 1, "Name");
        worksheet.value(indexTop+1, 2, "Vorname");
        worksheet.value(indexTop+1, 3, "Anwesend?");

        return indexTop+2;
    }

    private String getTime(String timeSlot){
        switch(timeSlot){
            case "A" : return "8:45 – 9:30";
            case "B" : return "9:50 – 10:35";
            case "C" : return "10:35 – 11:20";
            case "D" : return "11:40– 12:25";
            case "E" : return "12:25 – 13:10";
        }
        return "";
    }
}
