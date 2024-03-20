package de.bwv.ac.datamanagement.service.reader;

import de.bwv.ac.datamanagement.data.RoomList;
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
public class RoomListReader extends ExcelReader<RoomList> {
    @Override
    public RoomList read(String fileLocation) {
        return readRoomList(fileLocation);
    }

    private RoomList readRoomList(String fileLocation){
        RoomList result = new RoomList();
        try (FileInputStream fileInputStream = new FileInputStream(fileLocation); ReadableWorkbook workbook = new ReadableWorkbook(fileInputStream)){
            List<RoomList.Room> rooms = new ArrayList<>();
            workbook.getSheets().forEach(sheet -> rooms.addAll(readRooms(sheet)));
            result.setRoomList(rooms);
        } catch (FileNotFoundException e) {
            result.setErrorMessage("Die Datei "+fileLocation+" konnte nicht gefunden werden! Studenten-Liste konnte nicht erstellt werden!");
        } catch (IOException e) {
            result.setErrorMessage("Die Datei "+fileLocation+" konnte nicht ausgelesen werden! Studenten-Liste konnte nicht erstellt werden!");
        }
        return result;
    }

    private List<RoomList.Room> readRooms(Sheet sheet) {
        List<RoomList.Room> result = new ArrayList<>();
        Map<Integer, List<String>> rows = readRows(sheet);
        rows.forEach((rowNumber, entries) -> {
            if(!entries.isEmpty()){
                RoomList.Room room = new RoomList.Room();
                room.setRoomId(entries.get(0));
                if(entries.size() > 1 && !entries.get(1).isBlank() && isNumber(entries.get(1))){
                    room.setCapacity(Integer.parseInt(entries.get(1)));
                }
                result.add(room);
            }
        });
        if(result.isEmpty()){
            return result;
        }
        return result.subList(1, result.size()); //Without Header
    }
}
