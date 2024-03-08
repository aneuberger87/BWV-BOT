package de.bwv.ac.datamanagement.service.reader;

import de.bwv.ac.datamanagement.data.CompaniesList;
import lombok.extern.slf4j.Slf4j;
import org.dhatim.fastexcel.reader.ReadableWorkbook;
import org.dhatim.fastexcel.reader.Sheet;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;

@Slf4j
public class EventsListReader extends ExcelReader<CompaniesList>{

    @Override
    public CompaniesList read(String fileLocation) {
        return readEventList(fileLocation);
    }

    private CompaniesList readEventList(String fileLocation){
        CompaniesList companiesList = new CompaniesList();
        try (FileInputStream fileInputStream = new FileInputStream(fileLocation); ReadableWorkbook workbook = new ReadableWorkbook(fileInputStream)){
            List<CompaniesList.Company> companies = new ArrayList<>();
            workbook.getSheets().forEach(sheet -> companies.addAll(readEvent(sheet)));
            companiesList.setCompany(companies);
        } catch (FileNotFoundException e) {
            companiesList.setErrorMessage("Die Datei "+fileLocation+" konnte nicht gefunden werden! Studenten-Liste konnte nicht erstellt werden!");
        } catch (IOException e) {
            companiesList.setErrorMessage("Die Datei "+fileLocation+" konnte nicht ausgelesen werden! Studenten-Liste konnte nicht erstellt werden!");
        }
        return companiesList;
    }


    //Id, Name
    private List<CompaniesList.Company> readEvent(Sheet sheet) {
        List<CompaniesList.Company> result = new ArrayList<>();
        Map<Integer, List<String>> rows = readRows(sheet);
        rows.forEach((rowNumber, entries) -> {
            if(!entries.isEmpty() && entries.size() >= 5){
                CompaniesList.Company event = new CompaniesList.Company();
                try {
                    event.setId(Integer.parseInt(entries.get(0)));
                    event.setCompName(entries.get(1));
                    event.setTrainingOccupation(entries.get(2));
                    event.setNumberOfMembers(Integer.parseInt(entries.get(3)));
                    event.setMeeting(calculateMeetings(Integer.parseInt(entries.get(4)), entries.get(5)));
                    result.add(event);
                } catch (NumberFormatException e){
                    log.warn("{} ist keine Nummer!",entries.get(0));
                }
            }
        });
        return result;
    }

    //Annahme: Mittlere Veranstaltungen können nicht ausfallen! Nur die ersten oder die Letzten!
    private List<CompaniesList.Meeting> calculateMeetings(int numberMeetings, String earliestMeeting) {
        if(numberMeetings > getTimeSlots().size()){
            numberMeetings = getTimeSlots().size();
        }
        List<CompaniesList.Meeting> meetings = new ArrayList<>();
        boolean findEarliest = false;
        for(int i = 0, counter = 0; i < getTimeSlots().size() && counter < numberMeetings; i++){
            if(getTimeSlots().get(i).equals(earliestMeeting)){
                findEarliest = true;
            }
            if(findEarliest){
                meetings.add(new CompaniesList.Meeting(getTimeSlots().get(i), null));
                counter++;
            }
        }
        return meetings;
    }

}
