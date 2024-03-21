package de.bwv.ac.datamanagement.service.reader;

import de.bwv.ac.datamanagement.data.StudentsList;
import org.dhatim.fastexcel.reader.ReadableWorkbook;
import org.dhatim.fastexcel.reader.Sheet;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;

/**
 * Klasse zum Einlesen der Schülerliste aus einer Excel-Datei.
 */
public class StudentsListReader extends ExcelReader<StudentsList> {

    /**
     * Liest die Schülerliste als Excel-Datei ein und speichert sie als {@link StudentsList}
     * @param fileLocation der Dateipfad mit Dateiname und -endung.
     * @return die ausgelesene Schülerliste
     */
    @Override
    public StudentsList read(String fileLocation) {
        return readStudentsList(fileLocation);
    }

    private StudentsList readStudentsList(String fileLocation){
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
                student.setWishList(readWishes(entries.subList(3, entries.size())));
                result.add(student);
            }
        });
        if(result.isEmpty()){
            return result;
        }
        return result.subList(1, result.size()); //Without Header
    }

    private List<StudentsList.Wish> readWishes(List<String> entries) {
        List<StudentsList.Wish> wishes = new ArrayList<>();
        for(int i = 0; i < entries.size(); i++){
            String entry = entries.get(i);
            //Event-Id mit Timeslot z.B. 4A
            wishes.add(i, new StudentsList.Wish(getNumber(entry), getTimeslot(entry)));
        }
        return wishes;
    }

}
