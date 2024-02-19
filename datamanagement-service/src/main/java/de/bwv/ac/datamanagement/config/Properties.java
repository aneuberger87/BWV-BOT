package de.bwv.ac.datamanagement.config;

import lombok.Data;
import org.springframework.boot.context.properties.ConfigurationProperties;
import org.springframework.stereotype.Component;

@Component
@ConfigurationProperties(prefix = "de.bwv.bot")
@Data
public class Properties {

    private String studentslistLocation;
    private String companieslistLocation;
}
