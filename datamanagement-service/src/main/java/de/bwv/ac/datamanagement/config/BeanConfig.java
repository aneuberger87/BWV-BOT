package de.bwv.ac.datamanagement.config;

import de.bwv.ac.datamanagement.service.DataStorage;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.PropertySource;

@Configuration
public class BeanConfig {

    @Bean
    DataStorage dataStorage(){
        return new DataStorage();
    }

}
