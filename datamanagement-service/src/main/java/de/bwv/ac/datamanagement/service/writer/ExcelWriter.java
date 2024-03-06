package de.bwv.ac.datamanagement.service.writer;

import de.bwv.ac.datamanagement.data.CompaniesList;
import de.bwv.ac.datamanagement.service.DataStorage;
import lombok.Getter;
import lombok.extern.slf4j.Slf4j;
import org.dhatim.fastexcel.Workbook;
import org.dhatim.fastexcel.Worksheet;

import java.io.IOException;
import java.io.OutputStream;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.List;

@Slf4j
public abstract class ExcelWriter {

    @Getter
    private final DataStorage dataStorage;

    public ExcelWriter(DataStorage dataStorage) {
        this.dataStorage = dataStorage;
    }

    public abstract void write(String fileLocation);




    public void writeAttendanceList(String fileLocation) {
    }

    public void writeTimetableList(String fileLocation) {
    }
}
