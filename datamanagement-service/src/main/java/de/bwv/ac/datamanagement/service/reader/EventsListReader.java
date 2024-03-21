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

/**
 * Klasse zum Einlesen der Veranstaltungsliste aus einer Exceldatei
 */
@Slf4j
public class EventsListReader extends ExcelReader<CompaniesList>{

    /**
     * Liest die Veranstaltungsliste aus Excel ein und speichert sie als {@link CompaniesList}
     * @param fileLocation der Dateipfad mit Dateiname und -endung.
     * @return die eingelesene Veranstaltungsliste
     */
    @Override
    public CompaniesList read(String fileLocation) {
        return readEventList(fileLocation);
    }

    private CompaniesList readEventList(String fileLocation){
        CompaniesList companiesList = new CompaniesList();
        try (FileInputStream fileInputStream = new FileInputStream(fileLocation); ReadableWorkbook workbook = new ReadableWorkbook(fileInputStream)){
            List<CompaniesList.Company> companies = new ArrayList<>();
            log.info("Einlesen der Veranstaltungen aus der Datei: {}", fileLocation);
            workbook.getSheets().forEach(sheet -> companies.addAll(readEvent(sheet)));
            companiesList.setCompany(companies);
            log.info("Veranstaltungsdaten eingelesen");
        } catch (FileNotFoundException e) {
            log.error("Die Datei {} konnte nicht gefunden werden! Veranstaltungsliste konnte nicht erstellt werden!", fileLocation);
            companiesList.setErrorMessage("Die Datei "+fileLocation+" konnte nicht gefunden werden! Veranstaltungsliste konnte nicht erstellt werden!");
        } catch (IOException e) {
            log.error("Die Datei {} konnte nicht ausgelesen werden! Veranstaltungsliste konnte nicht erstellt werden!", fileLocation);
            companiesList.setErrorMessage("Die Datei "+fileLocation+" konnte nicht ausgelesen werden! Veranstaltungsliste konnte nicht erstellt werden!");
        }
        return companiesList;
    }

    //
    private List<CompaniesList.Company> readEvent(Sheet sheet) {
        List<CompaniesList.Company> result = new ArrayList<>();
        Map<Integer, List<String>> rows = readRows(sheet);
        rows.forEach((rowNumber, entries) -> {
            if(!entries.isEmpty() && entries.size() >= 5){
                CompaniesList.Company event = new CompaniesList.Company();
                try {
                    //Erstelle Company aus den Daten
                    event.setId(Integer.parseInt(entries.get(0).trim()));
                    event.setCompName(entries.get(1).trim());
                    event.setTrainingOccupation(entries.get(2).trim());
                    event.setNumberOfMembers(Integer.parseInt(entries.get(3).trim()));
                    event.setMeeting(calculateMeetings(Integer.parseInt(entries.get(4).trim()), entries.get(5).trim()));
                    result.add(event);
                } catch (NumberFormatException e){
                    log.warn("{} ist keine Nummer!",entries.get(0));
                } catch (Exception e){
                    log.error("Ein Unerwarteter Fehler ist aufgetreten. Fehler: {}", e.getMessage());
                    log.debug("Die folgende Zeile konnte nicht als Veranstaltung gespeichert werden: {}",String.join(", ", entries));
                }
            }
        });
        return result;
    }

    //Erstellt Meetings für Veranstaltungen. Meetings sind eine Zusammenstellung aus Zeitslot und Raum.
    // Hier wird der Raum allerdings noch nicht gesetzt.
    private List<CompaniesList.Meeting> calculateMeetings(int numberMeetings, String earliestMeeting) {
        if(numberMeetings > getTimeSlots().size()){
            //Es können nur maximal soviele Meetings pro Veranstaltung stattfinden wie es ZeitSlots gibt
            numberMeetings = getTimeSlots().size();
        }
        List<CompaniesList.Meeting> meetings = new ArrayList<>();

        //Erstelle nur Meetings ab dem earliestMeeting
        int earliestTimeslot = earliestMeeting.trim().charAt(0); //Bestehen nur aus einem Zeichen
        int latestTimeslot = getTimeSlots().get(getTimeSlots().size()-1).trim().charAt(0);
        for(int i = 0; i < numberMeetings && (earliestTimeslot+i) <= latestTimeslot; i++){
            meetings.add(new CompaniesList.Meeting(Character.toString(earliestTimeslot+i), null));
        }
        return meetings;
    }

}
