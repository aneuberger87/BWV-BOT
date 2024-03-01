package de.bwv.ac.datamanagement.service;

import de.bwv.ac.datamanagement.config.Properties;
import de.bwv.ac.datamanagement.data.CompaniesList;
import de.bwv.ac.datamanagement.data.RoomList;
import de.bwv.ac.datamanagement.data.StudentsList;
import jakarta.annotation.PostConstruct;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Component;

@Component
@Slf4j
public class DataStorageInitializer {

    private final Properties props;
    private final DataStorage dataStorage;

    public DataStorageInitializer(DataStorage dataStorage
           , Properties props
    ){
        this.dataStorage = dataStorage;
        this.props = props;
    }

    @PostConstruct
    public void initializeDataStorage(){
        if(!propsAreValid()){
            log.warn("No Locations of studentsList and companiesList can be found!");
        }
        ExcelReader reader = new ExcelReader(); //wird nur zum einlesen benötigt und kann dann wieder vom GC entfernt werden
        StudentsList studentsList = reader.readStudentsList(props.getStudentslistLocation());
        dataStorage.setStudentsList(studentsList);
        //CompaniesList companiesList = reader.readCompaniesList(props.getCompanieslistLocation());
        CompaniesList companiesList = reader.readEventList(props.getEventlistLocation());
        dataStorage.setCompanies(companiesList);

        RoomList roomList = reader.readRoomList(props.getRoomlistLocation());
        dataStorage.setRoomList(roomList);

    }

    private boolean propsAreValid() {
        return
                props != null &&
                !isNullOrBlank(props.getEventlistLocation()) &&
                !isNullOrBlank(props.getStudentslistLocation());
    }

    private boolean isNullOrBlank(String str){
        return str == null || str.isBlank();
    }

}
