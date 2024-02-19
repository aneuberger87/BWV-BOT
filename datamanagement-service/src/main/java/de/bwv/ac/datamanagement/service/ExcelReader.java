package de.bwv.ac.datamanagement.service;

import de.bwv.ac.datamanagement.data.CompaniesList;
import de.bwv.ac.datamanagement.data.StudentsList;
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
public class ExcelReader { //TODO test

    public StudentsList readStudentsList(String fileLocation){
        StudentsList studentsList = new StudentsList();
        try (FileInputStream fileInputStream = new FileInputStream(fileLocation); ReadableWorkbook workbook = new ReadableWorkbook(fileInputStream)){
            List<StudentsList.Student> students = new ArrayList<>();
            workbook.getSheets().forEach(sheet -> students.addAll(readStudent(sheet)));
            studentsList.setStudent(students);
        } catch (FileNotFoundException e) {
            studentsList.setErrorMessage("Die Datei "+fileLocation+" konnte nicht gefunden werden! Studenten-Liste konnte nicht erstellt werden!");
        } catch (IOException e) {
            studentsList.setErrorMessage("Die Datei "+fileLocation+" konnte nicht ausgelesen werden! Studenten-Liste konnte nicht erstellt werden!");
        }
        return studentsList;
    }

    //Klasse, Name, Vorname
    private List<StudentsList.Student> readStudent(Sheet sheet) {
        List<StudentsList.Student> result = new ArrayList<>();
        Map<Integer, List<String>> rows = readRows(sheet);
        rows.forEach((rowNumber, entries) -> {
            if(!entries.isEmpty() && entries.size() >= 3){
                StudentsList.Student student = new StudentsList.Student();
                student.setSchoolClass(entries.get(0));
                student.setSurname(entries.get(1));
                student.setPrename(entries.get(2));
                result.add(student);
            }
        });
        if(result.isEmpty()){
            return result;
        }
        return result.subList(1, result.size()); //Without Header
    }

    private Map<Integer, List<String>> readRows(Sheet sheet) {
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

    public CompaniesList readEventList(String fileLocation){
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

    private final List<String> timeSlots = List.of("A", "B", "C", "D", "E");
    //Annahme: Mittlere Veranstaltungen können nicht ausfallen! Nur die ersten oder die Letzten!
    private List<CompaniesList.Meeting> calculateMeetings(int numberMeetings, String earliestMeeting) {
        if(numberMeetings > timeSlots.size()){
            numberMeetings = timeSlots.size();
        }
        List<CompaniesList.Meeting> meetings = new ArrayList<>();
        boolean findEarliest = false;
        for(int i = 0, counter = 0; i < timeSlots.size() && counter < numberMeetings; i++){
            if(timeSlots.get(i).equals(earliestMeeting)){
                findEarliest = true;
            }
            if(findEarliest){
                meetings.add(new CompaniesList.Meeting(timeSlots.get(i), null));
                counter++;
            }
        }
        return meetings;
    }


}
