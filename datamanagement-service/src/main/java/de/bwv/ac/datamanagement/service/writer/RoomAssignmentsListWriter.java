package de.bwv.ac.datamanagement.service.writer;

import de.bwv.ac.datamanagement.data.CompaniesList;
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
public class RoomAssignmentsListWriter extends ExcelWriter {

    public RoomAssignmentsListWriter(DataStorage dataStorage) {
        super(dataStorage);
    }

    @Override
    public void write(String fileLocation) throws IOException {
        writeRoomAndTimeSlotList(getDataStorage().getCompaniesList(), fileLocation);
    }

    /**
     * Writes the Room and TimeSlots for the Events as Excel-File
     *
     * @param companiesList the Companies-List
     * @param fileDirectory the directory of the file to write
     */
    private void writeRoomAndTimeSlotList(CompaniesList companiesList, String fileDirectory) throws IOException {
        if (companiesList.getErrorMessage() != null && !companiesList.getErrorMessage().isBlank()) {
            log.warn("Can not write the Rooms- and TimeSlot-Plan because the companieslist is not available (Reason: {})", companiesList.getErrorMessage());
            return;
        }
        String fileLocation = fileDirectory + "/" + "Raum_und_Zeitplanung.xlsx";
        Files.deleteIfExists(Paths.get(fileLocation));
        try (OutputStream outputStream = Files.newOutputStream(Paths.get(fileLocation)); Workbook workbook = new Workbook(outputStream, "RaumUndZeitplaner", "1.0")) {
            Worksheet worksheet = workbook.newWorksheet("Sheet 1");
            formatWorksheet(worksheet, companiesList.getCompany().size()+1, 7);
            writeHeader(worksheet);
            for (int i = 0; i < companiesList.getCompany().size(); i++) {
                writeEntry(companiesList.getCompany().get(i), worksheet, i+1); //Zeile 0 ist der Header
            }
        }
    }

    private void writeEntry(CompaniesList.Company company, Worksheet worksheet, int row) {
        worksheet.value(row, 0, company.getId());
        worksheet.value(row, 1, company.getCompName());
        List<CompaniesList.Meeting> meeting = company.getMeeting();
        for (CompaniesList.Meeting m : meeting) {
            switch (m.getTimeSlot()) {
                case "A": {
                    worksheet.value(row, 2, m.getRoom().getRoomId());
                    break;
                }
                case "B": {
                    worksheet.value(row, 3, m.getRoom().getRoomId());
                    break;
                }
                case "C": {
                    worksheet.value(row, 4, m.getRoom().getRoomId());
                    break;
                }
                case "D": {
                    worksheet.value(row, 5, m.getRoom().getRoomId());
                    break;
                }
                case "E": {
                    worksheet.value(row, 6, m.getRoom().getRoomId());
                    break;
                }
            }
        }
    }

    private void formatWorksheet(Worksheet worksheet, int sizeRows, int sizeColumn) {
        for(int i = 2; i < sizeColumn; i++){
            worksheet.width(i, 15);
        }
        worksheet.range(0, 0, 0, 1).style().merge().wrapText(true).set();
        worksheet.range(0, 2, 0, sizeColumn-1).style().borderStyle(BorderStyle.THIN).horizontalAlignment("center").bold().fillColor("b3daff").wrapText(true).set();
        worksheet.range(1, 0, sizeRows-1, 1).style().borderStyle(BorderStyle.THIN).horizontalAlignment("left").bold().wrapText(false).set();
        worksheet.range(1, 2, sizeRows-1, sizeColumn-1).style().borderStyle(BorderStyle.THIN).horizontalAlignment("center").wrapText(false).set();
    }

    private void writeHeader(Worksheet worksheet) {
        //worksheet.range(0, 0, 0, 1).style().wrapText(true).fontName("Arial").fontSize(16).bold().fillColor("3366FF").set();
        worksheet.value(0, 2, "8:45 - 9:30\nA");
        worksheet.value(0, 3, "9:50 - 10:35\nB");
        worksheet.value(0, 4, "10:35 - 11:20\nC");
        worksheet.value(0, 5, "11:40 - 12:25\nD");
        worksheet.value(0, 6, "12:25 - 13:10\nE");
    }
}
