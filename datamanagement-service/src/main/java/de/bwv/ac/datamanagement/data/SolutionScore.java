package de.bwv.ac.datamanagement.data;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@NoArgsConstructor
@AllArgsConstructor
public class SolutionScore {

    private double realScore;

    private String errorMessage;

}
