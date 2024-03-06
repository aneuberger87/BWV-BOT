package de.bwv.ac.datamanagement.service;

import java.io.File;
import java.io.IOException;

public class PythonScriptExecuter {

    private final String scriptLocation;

    public PythonScriptExecuter(String scriptLocation){
        this.scriptLocation = scriptLocation;
    }

    public void executeScript(String pythonFile) throws IOException {
        ProcessBuilder processBuilder = new ProcessBuilder("python", resolvePythonScriptPath(pythonFile));
        processBuilder.redirectErrorStream(true);

        Process process = processBuilder.start();
    }

    private String resolvePythonScriptPath(String filename) {
        File file = new File(scriptLocation + filename);
        return file.getAbsolutePath();
    }
}
