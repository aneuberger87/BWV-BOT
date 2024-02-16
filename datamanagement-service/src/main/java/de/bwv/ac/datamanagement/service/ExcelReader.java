package de.bwv.ac.datamanagement.service;

import de.bwv.ac.datamanagement.data.StudentsList;
import org.dhatim.fastexcel.reader.Cell;
import org.dhatim.fastexcel.reader.ReadableWorkbook;
import org.dhatim.fastexcel.reader.Row;
import org.dhatim.fastexcel.reader.Sheet;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.stream.Stream;

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

    //Class, PreName, SurName
    private List<StudentsList.Student> readStudent(Sheet sheet) {
        List<StudentsList.Student> result = new ArrayList<>();
        Map<Integer, List<String>> rows = readRows(sheet);
        rows.forEach((rowNumber, entries) -> {
            if(!entries.isEmpty() && entries.size() >= 3){
                StudentsList.Student student = new StudentsList.Student();
                student.setSchoolClass(entries.get(0));
                student.setPrename(entries.get(1));
                student.setSurname(entries.get(2));
                result.add(student);
            }
        });
        return result;
    }

    private Map<Integer, List<String>> readRows(Sheet sheet) {
        Map<Integer, List<String>> result = new HashMap<>();
        try (Stream<Row> rows = sheet.openStream()){
            rows.forEach(row -> {
                result.put(row.getRowNum(), new ArrayList<>());

                for (Cell cell : row) {
                    result.get(row.getRowNum()).add(cell.getRawValue());
                }
            });
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
        return result;
    }

    //TODO: ReadCompanies

}
