package de.bwv.ac.datamanagement.service.writer;

import de.bwv.ac.datamanagement.data.CompaniesList;
import de.bwv.ac.datamanagement.data.StudentsList;
import de.bwv.ac.datamanagement.data.export.EventsAttendanceList;
import de.bwv.ac.datamanagement.data.export.TimetableList;
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
public class TimetableListWriter extends ExcelWriter{
    public TimetableListWriter(DataStorage dataStorage) {
        super(dataStorage);
    }

    @Override
    public void write(String fileLocation) throws IOException {
        writeTimetableList(getDataStorage().calculateTimeTableList(), fileLocation);
    }

    public void writeTimetableList(TimetableList timetableList, String fileDirectory) throws IOException {
        if (timetableList.getErrorMessage() != null && !timetableList.getErrorMessage().isBlank()) {
            log.warn("Can not write the Attendance-Per-Events-Plan (Reason: {})", timetableList.getErrorMessage());
            return;
        }
        String fileLocation = fileDirectory + "/" + "Laufzettel.xlsx";
        Files.deleteIfExists(Paths.get(fileLocation));
        try (OutputStream outputStream = Files.newOutputStream(Paths.get(fileLocation)); Workbook workbook = new Workbook(outputStream, "RaumUndZeitplaner", "1.0")) {
            final int COLUMN_SIZE = 6;


            for (int i = 0; i < timetableList.getTimetables().size(); i++) {
                TimetableList.TimetableOfStudentsFromClass timetableOfStudentsFromClass = timetableList.getTimetables().get(i);
                //Alle Studenten einer Klasse auf das selber Sheet
                String schoolClass = timetableOfStudentsFromClass.getSchoolClass();
                List<TimetableList.StudentsAllocation> studentsAllocationList = timetableOfStudentsFromClass.getStudentsAllocationList();

                Worksheet worksheet = workbook.newWorksheet(schoolClass);
                int indexTop = 0;
                for(int k = 0; k < studentsAllocationList.size(); k++) {
                    TimetableList.StudentsAllocation studentsAllocation = studentsAllocationList.get(k);
                    String prename = studentsAllocation.getPrename();
                    String surname = studentsAllocation.getSurname();
                    formatHeaderWorksheet(worksheet, indexTop, COLUMN_SIZE);
                    indexTop = writeHeader(worksheet, schoolClass, prename, surname, indexTop);
                    List<TimetableList.TimeTable.Rows> rows = studentsAllocation.getTimeTable().getRows();
                    for(int j = 0; j < rows.size(); j++) {
                        TimetableList.TimeTable.Rows row = rows.get(j);
                        String timeSlot = row.getMeeting().getTimeSlot();
                        String roomId = row.getMeeting().getRoom().getRoomId();
                        String companyName = row.getCompanyName();
                        String companyEvent = row.getCompanyEvent();
                        String numberWish = row.getNumberWish();
                        formatEntriesWorksheet(worksheet, indexTop, COLUMN_SIZE);
                        writeEntry(timeSlot, roomId, companyName, companyEvent, numberWish, worksheet, indexTop);
                        indexTop++;
                    }
                }
            }
        }
    }

    private void writeEntry(String timeSlot, String roomId, String companyName, String companyEvent, String numberWish, Worksheet worksheet, int row) {
        worksheet.value(row, 0, timeSlot);
        worksheet.value(row, 1, getTime(timeSlot));
        worksheet.value(row, 2, roomId);
        worksheet.value(row, 3, companyName);
        worksheet.value(row, 4, companyEvent);
        worksheet.value(row, 5, numberWish);
    }


    private void formatHeaderWorksheet(Worksheet worksheet, int indexTop, int sizeColumn){
        worksheet.range(indexTop, 0, indexTop, 0).style().fontSize(12).bold().borderStyle(BorderStyle.THIN).wrapText(false).set();
        worksheet.range(indexTop+1, 0, indexTop+1, sizeColumn-1).style().fontSize(11).bold().borderStyle(BorderStyle.THIN).wrapText(false).set();
        worksheet.range(indexTop, 0, indexTop+1, sizeColumn-1).style().horizontalAlignment("left").wrapText(false).set();
    }

    private void formatEntriesWorksheet(Worksheet worksheet, int indexTop, int sizeColumn){
        worksheet.range(indexTop, 0, indexTop, sizeColumn-1).style().borderStyle(BorderStyle.THIN).horizontalAlignment("left").wrapText(false).set();
    }

    private int writeHeader(Worksheet worksheet, String schoolClass, String prename, String surname, int indexTop) {
        worksheet.value(indexTop, 0, schoolClass);
        worksheet.value(indexTop+1, 0, surname+", "+prename);
        worksheet.value(indexTop+2, 0, "");
        worksheet.value(indexTop+2, 1, "Zeit");
        worksheet.value(indexTop+2, 2, "Raum");
        worksheet.value(indexTop+2, 3, "Veranstaltung");
        worksheet.value(indexTop+2, 4, "Veranstaltung");
        worksheet.value(indexTop+2, 5, "Wunsch");

        return indexTop+3;
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
