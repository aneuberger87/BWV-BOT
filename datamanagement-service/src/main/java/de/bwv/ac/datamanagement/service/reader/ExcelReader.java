package de.bwv.ac.datamanagement.service.reader;

import lombok.Getter;
import lombok.extern.slf4j.Slf4j;
import org.dhatim.fastexcel.reader.Cell;
import org.dhatim.fastexcel.reader.Row;
import org.dhatim.fastexcel.reader.Sheet;

import java.io.IOException;
import java.util.*;
import java.util.stream.Stream;

/**
 * Klasse zum Einlesen von Inhalten aus Excel-Dateien
 * @param <T> Beschreibt die Datenstruktur zum Speichern der eingelesenen Daten
 */
@Getter
@Slf4j
public abstract class ExcelReader<T> {

    private final List<String> timeSlots = List.of("A", "B", "C", "D", "E");

    /**
     * Liest die Excel-Datei aus und speichert den Datensatz in der Datenstruktur, die beim Erstellen des Readers festgelegt wird.
     * @param fileLocation der Dateipfad mit Dateiname und -endung.
     * @return die Daten, gespeichert in der festgelegten Datenstruktur
     */
    public abstract T read(String fileLocation);

    /**
     * Gibt aus einem String den TimeSlot zurück. Dabei wird erwartet, dass der TimeSlot hier, das letzte Zeichen ist.
     * @param entry der String mit den TimeSlot am Ende
     * @return den TimeSlot
     */
    protected String getTimeslot(String entry) {
        if(entry == null || entry.isBlank()){
            return "";
        }
        String timeSlotCandinate = ""+entry.charAt(entry.length()-1);
        if(timeSlots.contains(timeSlotCandinate)){
            return timeSlotCandinate;
        }
        return "";
    }

    /**
     * Gibt aus einem String die führenden ganzzahligen Elemente als Integer zurück.
     * @param entry der String mit den führenden ganzzahligen Elementen
     * @return die führenden Ganzzahligen Elemente des Strings, oder <i>-1</i> falls keine solche im String existieren.
     */
    protected int getNumber(String entry) {
        if(entry == null){
            return -1;
        }
        StringBuilder result = new StringBuilder();
        for(int i = 0; i < entry.length(); i++){
            if(isNumber(""+entry.charAt(i))){
                result.append(entry.charAt(i));
            } else {
                break; //Erstes Zeichen, das keine Nummer ist gefunden
            }
        }
        String numbers = result.toString();
        if(numbers.isBlank()){
            return -1;
        }
        return Integer.parseInt(result.toString());

    }

    /**
     * Prüft ob der übergebene String eine Ganzzahl repräsentiert
     * @param str der zu Prüfende String
     * @return <i>true</i>, falls der übergebene String eine Ganzzahl repräsentiert, sonst <i>false</i>
     */
    protected boolean isNumber(String str) {
        try{
            Integer.parseInt(str);
        } catch (NumberFormatException e){
            return false;
        }
        return true;
    }

    /**
     * Einlesen der einzelnen Zeilen aus einem Sheet der Excel-Datei
     * @param sheet das Sheet aus dem die Zeilen ausgelesen werden sollen
     * @return die ausgelesenen Zeilen als Map: (Zeilen-Nummer, Spaltenelemente als Liste aus Strings)
     */
    protected Map<Integer, List<String>> readRows(Sheet sheet) {
        Map<Integer, List<String>> result = new HashMap<>();
        try (Stream<Row> rows = sheet.openStream()){
            rows.forEach(row -> {
                result.put(row.getRowNum(), new ArrayList<>());

                for (Cell cell : row) {
                    if(cell == null || cell.getRawValue() == null){
                        result.get(row.getRowNum()).add("");
                    } else {
                        result.get(row.getRowNum()).add(cell.getRawValue());
                    }
                }
            });
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
        return result;
    }


}
