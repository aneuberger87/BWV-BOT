package de.bwv.ac.datamanagement.service.writer;

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
        TimetableList timetableList = getDataStorage().calculateTimeTableList();
        writeTimetableList(timetableList, fileLocation);
    }

    public void writeTimetableList(TimetableList timetableList, String fileDirectory) throws IOException {
        if (timetableList.getErrorMessage() != null && !timetableList.getErrorMessage().isBlank()) {
            log.warn("Can not write the TimetableList (Reason: {})", timetableList.getErrorMessage());
            return;
        }
        String fileLocation = fileDirectory + "/" + "Laufzettel.xlsx";
        Files.deleteIfExists(Paths.get(fileLocation));
        try (OutputStream outputStream = Files.newOutputStream(Paths.get(fileLocation)); Workbook workbook = new Workbook(outputStream, "Laufzettel", "1.0")) {
            final int COLUMN_SIZE = 5;

            int indexTop = 0;
            for (int i = 0; i < timetableList.getTimetables().size(); i++) {
                TimetableList.TimetableOfStudentsFromClass timetableOfStudentsFromClass = timetableList.getTimetables().get(i);
                //Alle Studenten einer Klasse auf das selber Sheet
                String schoolClass = timetableOfStudentsFromClass.getSchoolClass().trim();
                List<TimetableList.StudentsAllocation> studentsAllocationList = timetableOfStudentsFromClass.getStudentsAllocationList();

                Worksheet worksheet = workbook.newWorksheet(schoolClass);

                for(int k = 0; k < studentsAllocationList.size(); k++) {
                    TimetableList.StudentsAllocation studentsAllocation = studentsAllocationList.get(k);
                    String prename = studentsAllocation.getPrename();
                    String surname = studentsAllocation.getSurname();
                    formatHeaderWorksheet(worksheet, indexTop, COLUMN_SIZE);
                    indexTop = writeHeader(worksheet, schoolClass, prename, surname, indexTop);
                    List<TimetableList.TimeTable.Rows> rows = studentsAllocation.getTimeTable().getRows();
                    rows.removeIf(r -> r.getMeeting() == null || r.getMeeting().getRoom() == null);
                    for(int j = 0; j < rows.size(); j++) {
                        TimetableList.TimeTable.Rows row = rows.get(j);
                        try {
                            String timeSlot = row.getMeeting().getTimeSlot();
                            String roomId = row.getMeeting().getRoom().getRoomId();
                            String companyName = row.getCompanyName();
                            String companyEvent = row.getCompanyEvent();
                            String numberWish = row.getNumberWish();
                            formatEntriesWorksheet(worksheet, indexTop, COLUMN_SIZE);
                            writeEntry(timeSlot, roomId, companyName, companyEvent, numberWish, worksheet, indexTop);
                        } catch (Exception e){
                            log.error("Fehler beim Bearbeiten von student: {} {}, Klasse {}", prename, surname, schoolClass);
                            e.printStackTrace();
                        }
                        indexTop = indexTop+1;
                    }
                    indexTop = indexTop + 3;
                }
                indexTop = 0;
            }
        }
    }

    private void writeEntry(String timeSlot, String roomId, String companyName, String companyEvent, String numberWish, Worksheet worksheet, int row) {
        //worksheet.value(row, 0, timeSlot);
        worksheet.value(row, 0, getTime(timeSlot));
        worksheet.value(row, 1, roomId);
        worksheet.value(row, 2, companyName);
        worksheet.value(row, 3, companyEvent);
        worksheet.value(row, 4, numberWish);
    }


    private void formatHeaderWorksheet(Worksheet worksheet, int indexTop, int sizeColumn){
        worksheet.range(indexTop, 0, indexTop, 0).style().fontSize(12).bold().fillColor("b3daff").borderStyle(BorderStyle.THIN).wrapText(false).set();
        worksheet.range(indexTop+1, 0, indexTop+1, 0).style().fontSize(11).bold().fillColor("b3daff").borderStyle(BorderStyle.THIN).wrapText(false).set();
        worksheet.range(indexTop+2, 0, indexTop+2, sizeColumn-1).style().fontSize(11).bold().fillColor("b3daff").borderStyle(BorderStyle.THIN).wrapText(false).set();
        worksheet.range(indexTop, 0, indexTop+1, sizeColumn-1).style().horizontalAlignment("left").wrapText(false).set();
    }

    private void formatEntriesWorksheet(Worksheet worksheet, int indexTop, int sizeColumn){
        worksheet.range(indexTop, 0, indexTop, sizeColumn-1).style().borderStyle(BorderStyle.THIN).horizontalAlignment("left").wrapText(false).set();
    }

    private int writeHeader(Worksheet worksheet, String schoolClass, String prename, String surname, int indexTop) {
        worksheet.value(indexTop, 0, schoolClass);
        worksheet.value(indexTop+1, 0, surname+", "+prename);
       // worksheet.value(indexTop+2, 0, "");
        worksheet.value(indexTop+2, 0, "Zeit");
        worksheet.value(indexTop+2, 1, "Raum");
        worksheet.value(indexTop+2, 2, "Unternehmen");
        worksheet.value(indexTop+2, 3, "Veranstaltung");
        worksheet.value(indexTop+2, 4, "Wunsch");

        return indexTop+3;
    }

    private String getTime(String timeSlot){
        switch(timeSlot){
            case "A" : return "08:45 – 09:30";
            case "B" : return "09:50 – 10:35";
            case "C" : return "10:35 – 11:20";
            case "D" : return "11:40 – 12:25";
            case "E" : return "12:25 – 13:10";
        }
        return "";
    }
}
