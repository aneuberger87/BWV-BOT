package de.bwv.ac.datamanagement.service;

import de.bwv.ac.datamanagement.config.Properties;
import de.bwv.ac.datamanagement.data.CompaniesList;
import de.bwv.ac.datamanagement.data.RoomList;
import de.bwv.ac.datamanagement.data.StudentsList;
import de.bwv.ac.datamanagement.service.reader.EventsListReader;
import de.bwv.ac.datamanagement.service.reader.ExcelReader;
import de.bwv.ac.datamanagement.service.reader.RoomListReader;
import de.bwv.ac.datamanagement.service.reader.StudentsListReader;
import jakarta.annotation.PostConstruct;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Component;

@Component
@Slf4j
@Deprecated
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
        ExcelReader<StudentsList> studentsReader = new StudentsListReader(); //wird nur zum einlesen benötigt und kann dann wieder vom GC entfernt werden
        StudentsList studentsList = studentsReader.read(props.getStudentslistLocation());
        dataStorage.setStudentsWishesList(studentsList);
        //CompaniesList companiesList = reader.readCompaniesList(props.getCompanieslistLocation());

        ExcelReader<CompaniesList> eventsReader = new EventsListReader();
        CompaniesList companiesList = eventsReader.read(props.getEventlistLocation());
        dataStorage.setCompanies(companiesList);

        ExcelReader<RoomList> roomsReader = new RoomListReader();
        RoomList roomList = roomsReader.read(props.getRoomlistLocation());
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
