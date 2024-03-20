package de.bwv.ac.datamanagement.data.storage;

import de.bwv.ac.datamanagement.data.StudentsList;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

import java.util.List;

@Data
@AllArgsConstructor
@NoArgsConstructor
public class StudentStorageDatamodel {

    private StudentsList.Student student;
    private List<StudentsList.Wish> allocation;

    public static String getId(StudentsList.Student student){
        return student.getSchoolClass()+"_"+student.getPrename()+"_"+student.getSurname();
    }

}
