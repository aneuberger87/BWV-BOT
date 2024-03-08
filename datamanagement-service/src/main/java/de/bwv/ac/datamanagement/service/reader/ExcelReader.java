package de.bwv.ac.datamanagement.service.reader;

import de.bwv.ac.datamanagement.data.CompaniesList;
import de.bwv.ac.datamanagement.data.RoomList;
import de.bwv.ac.datamanagement.data.StudentsList;
import lombok.Getter;
import lombok.extern.slf4j.Slf4j;
import org.dhatim.fastexcel.reader.Cell;
import org.dhatim.fastexcel.reader.ReadableWorkbook;
import org.dhatim.fastexcel.reader.Row;
import org.dhatim.fastexcel.reader.Sheet;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.*;
import java.util.stream.Stream;

@Slf4j
public abstract class ExcelReader<T> {

    @Getter
    private final List<String> timeSlots = List.of("A", "B", "C", "D", "E");

    public abstract T read(String fileLocation);

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

    protected boolean isNumber(String str) {
        try{
            Integer.parseInt(str);
        } catch (NumberFormatException e){
            return false;
        }
        return true;
    }

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
