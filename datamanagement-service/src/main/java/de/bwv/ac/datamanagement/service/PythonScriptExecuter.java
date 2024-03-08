package de.bwv.ac.datamanagement.service;

import java.io.*;
import java.util.List;
import java.util.stream.Collectors;

public class PythonScriptExecuter {

    private final String scriptLocation;

    public PythonScriptExecuter(String scriptLocation){
        this.scriptLocation = scriptLocation;
    }

    public void executeScript(String pythonFile) throws IOException {
        ProcessBuilder processBuilder = new ProcessBuilder("python", resolvePythonScriptPath(pythonFile));
        processBuilder.redirectErrorStream(true);

        Process process = processBuilder.start();
        List<String> results = readProcessOutput(process.getInputStream());
        for (int i = 0; i < results.size(); i++) {
            System.out.println(results.get(i));
        }
    }

    private List<String> readProcessOutput(InputStream inputStream) throws IOException {
        try (BufferedReader output = new BufferedReader(new InputStreamReader(inputStream))) {
            return output.lines()
                    .collect(Collectors.toList());
        }
    }

    private String resolvePythonScriptPath(String filename) {
        File file = new File(scriptLocation + filename);
        return file.getAbsolutePath();
    }
}
