package de.bwv.ac.datamanagement.config;

import de.bwv.ac.datamanagement.service.DataStorage;
import de.bwv.ac.datamanagement.service.PythonScriptExecuter;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.PropertySource;

@Configuration
public class BeanConfig {

    @Bean
    DataStorage dataStorage(){
        return new DataStorage();
    }

    @Bean
    PythonScriptExecuter scriptExecuter(Properties props) {
        return new PythonScriptExecuter(props.getScriptLocation());
    }

}
