package de.bwv.ac.datamanagement.service;

import org.junit.jupiter.api.Test;

import javax.script.*;
import java.io.*;
import java.util.List;
import java.util.stream.Collectors;

public class PythonTest {

    @Test
    public void test() throws IOException {

        ProcessBuilder processBuilder = new ProcessBuilder("python", resolvePythonScriptPath("Tranformation.py"));
        processBuilder.redirectErrorStream(true);

        Process process = processBuilder.start();
        List<String> results = readProcessOutput(process.getInputStream());
        System.out.println();


    }

    //@Test
    public void test2() throws FileNotFoundException, ScriptException {
        /*
        StringWriter writer = new StringWriter(); //ouput will be stored here

        ScriptEngineManager manager = new ScriptEngineManager();
        ScriptContext context = new SimpleScriptContext();

        context.setWriter(writer); //configures output redirection
        ScriptEngine engine = manager.getEngineByName("python");
        engine.eval(new FileReader("../Transformation/Tranformation.py"), context);
        System.out.println(writer.toString());
        */


        /*
        try(PythonInterpreter pyInterp = new PythonInterpreter()) {
            pyInterp.exec("print('Hello Python World!')");
        }

         */
    }

    private List<String> readProcessOutput(InputStream inputStream) throws IOException {
        try (BufferedReader output = new BufferedReader(new InputStreamReader(inputStream))) {
            return output.lines()
                    .collect(Collectors.toList());
        }
    }

    private String resolvePythonScriptPath(String filename) {
        File file = new File("../Transformation/" + filename);
        return file.getAbsolutePath();
    }

}
