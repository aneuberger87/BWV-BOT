package de.bwv.ac.datamanagement.service.writer;

import de.bwv.ac.datamanagement.data.StudentsList;
import de.bwv.ac.datamanagement.data.export.EventsAttendanceList;
import de.bwv.ac.datamanagement.service.DataStorage;
import lombok.extern.slf4j.Slf4j;
import org.dhatim.fastexcel.Workbook;
import org.dhatim.fastexcel.Worksheet;

import java.io.IOException;
import java.io.OutputStream;
import java.nio.file.Files;
import java.nio.file.Paths;

@Slf4j
public class AttendanceListWriter extends ExcelWriter{

    public AttendanceListWriter(DataStorage dataStorage) {
        super(dataStorage);
    }

    @Override
    public void write(String fileLocation) throws IOException {
        writeEventsAttendanceist(getDataStorage().calculateEventsAttendenceList(), fileLocation);
    }

    private void writeEventsAttendanceist(EventsAttendanceList eventsAttendanceList, String fileDirectory) throws IOException {
        if (eventsAttendanceList.getErrorMessage() != null && !eventsAttendanceList.getErrorMessage().isBlank()) {
            log.warn("Can not write the Attendance-Per-Events-Plan (Reason: {})", eventsAttendanceList.getErrorMessage());
            return;
        }
        String fileLocation = fileDirectory + "/" + "Anwesenheitsliste_pro_Veranstaltung.xlsx";
        Files.deleteIfExists(Paths.get(fileLocation));
        try (OutputStream outputStream = Files.newOutputStream(Paths.get(fileLocation)); Workbook workbook = new Workbook(outputStream, "RaumUndZeitplaner", "1.0")) {
            for (int i = 0; i < eventsAttendanceList.getAttendanceLists().size(); i++) {
                Worksheet worksheet = workbook.newWorksheet("Sheet "+(i+1));
                EventsAttendanceList.AttendanceList attendanceList = eventsAttendanceList.getAttendanceLists().get(i);
                int numberHeaderRows = writeHeader(worksheet, attendanceList.getCompanyName(), attendanceList.getEvent().getTimeSlot());
                formatWorksheet(worksheet, eventsAttendanceList.getAttendanceLists().size()+numberHeaderRows, 4);

                for (int j = 0; j <= attendanceList.getStudents().size(); j++) {
                    writeEntry(attendanceList.getStudents().get(j), worksheet, i+numberHeaderRows); //Zeile 0 ist der Header
                }
            }
        }
    }

    private void writeEntry(StudentsList.Student student, Worksheet worksheet, int row) {
        worksheet.value(row, 0, student.getSchoolClass());
        worksheet.value(row, 1, student.getSurname());
        worksheet.value(row, 2, student.getPrename());
    }

    private void formatWorksheet(Worksheet worksheet, int sizeRows, int sizeColumn) {
        for(int i = 0; i < sizeColumn; i++){
            worksheet.width(i, 15);
        }
        worksheet.range(0, 0, sizeRows, sizeColumn).style().horizontalAlignment("center").wrapText(true).set();
    }

    private int writeHeader(Worksheet worksheet, String companiesName, String timeSlot) {
        worksheet.value(0, 0, "Anwesenheitsliste");
        worksheet.value(1, 0, companiesName);
        worksheet.value(2, 0, timeSlot);
        worksheet.value(3, 0, "Klasse");
        worksheet.value(3, 1, "Name");
        worksheet.value(3, 2, "Vorname");
        worksheet.value(3, 3, "Anwesend?");
        return 3;
    }
}
