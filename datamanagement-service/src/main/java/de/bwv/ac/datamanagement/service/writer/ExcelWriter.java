package de.bwv.ac.datamanagement.service.writer;

import de.bwv.ac.datamanagement.service.DataStorage;
import lombok.Getter;
import lombok.extern.slf4j.Slf4j;

import java.io.IOException;

@Getter
@Slf4j
public abstract class ExcelWriter {

    private final DataStorage dataStorage;

    public ExcelWriter(DataStorage dataStorage) {
        this.dataStorage = dataStorage;
    }

    public abstract void write(String fileLocation) throws IOException;

}
