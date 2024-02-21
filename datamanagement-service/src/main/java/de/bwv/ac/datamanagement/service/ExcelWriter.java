package de.bwv.ac.datamanagement.service;

import de.bwv.ac.datamanagement.data.CompaniesList;
import lombok.extern.slf4j.Slf4j;
import org.dhatim.fastexcel.Workbook;
import org.dhatim.fastexcel.Worksheet;

import java.io.IOException;
import java.io.OutputStream;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.List;

@Slf4j
public class ExcelWriter { //TODO test

    /**
     * Writes the Room and TimeSlots for the Events as Excel-File
     *
     * @param companiesList the Companies-List
     * @param fileDirectory the directory of the file to write
     */
    public void writeRoomAndTimeSlotList(CompaniesList companiesList, String fileDirectory) throws IOException {
        if (companiesList.getErrorMessage() != null && !companiesList.getErrorMessage().isBlank()) {
            log.warn("Can not write the Rooms- and TimeSlot-Plan because the companieslist is not available (Reason: {})", companiesList.getErrorMessage());
            return;
        }
        String fileLocation = fileDirectory + "/" + "Raum_und_Zeitplanung.xlsx";
        Files.deleteIfExists(Paths.get(fileLocation));

        try (OutputStream outputStream = Files.newOutputStream(Paths.get(fileLocation)); Workbook workbook = new Workbook(outputStream, "RaumUndZeitplaner", "1.0")) {
            Worksheet worksheet = workbook.newWorksheet("Sheet 1");
            worksheet.width(0, 10);
            worksheet.width(1, 25);
            worksheet.width(2, 15);
            worksheet.width(3, 15);
            worksheet.width(4, 15);
            worksheet.width(5, 15);
            worksheet.width(6, 15);
            worksheet.width(7, 15);

            worksheet.range(0, 0, 0, 1).style().wrapText(true).fontName("Arial").fontSize(16).bold().fillColor("3366FF").set();
            worksheet.value(0, 2, "8:45 - 9:30\nA");
            worksheet.value(0, 3, "9:50 - 10:35\nB");
            worksheet.value(0, 4, "10:35 - 11:20\nC");
            worksheet.value(0, 5, "11:40 - 12:25\nD");
            worksheet.value(0, 6, "12:25 - 13:10\nE");


            worksheet.range(2, 0, 2, 1).style().wrapText(true).set();


            for (int i = 0; i < companiesList.getCompany().size(); i++) {

                CompaniesList.Company company = companiesList.getCompany().get(i);
                worksheet.value(i + 1, 0, company.getId());
                worksheet.value(i + 1, 1, company.getCompName());
                List<CompaniesList.Meeting> meeting = company.getMeeting();
                for (CompaniesList.Meeting m : meeting) {
                    switch (m.getTimeSlot()) {
                        case "A": {
                            worksheet.value(i + 1, 2, m.getRoom());
                            break;
                        }
                        case "B": {
                            worksheet.value(i + 1, 3, m.getRoom());
                            break;
                        }
                        case "C": {
                            worksheet.value(i + 1, 4, m.getRoom());
                            break;
                        }
                        case "D": {
                            worksheet.value(i + 1, 5, m.getRoom());
                            break;
                        }
                        case "E": {
                            worksheet.value(i + 1, 6, m.getRoom());
                            break;
                        }
                    }
                }
            }
        }
    }


    //TODO: writeAttendanceList

}
