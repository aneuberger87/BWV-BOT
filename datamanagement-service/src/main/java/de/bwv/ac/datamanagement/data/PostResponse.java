package de.bwv.ac.datamanagement.data;

import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@NoArgsConstructor
public class PostResponse {
    private boolean postSuccessful = true;
    private String errormessage;

    public PostResponse (String errormessage){
        postSuccessful = false;
        this.errormessage = errormessage;
    }
}
