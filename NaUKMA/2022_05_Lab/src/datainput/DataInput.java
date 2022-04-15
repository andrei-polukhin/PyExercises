package datainput;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/**
 * Data input functionality
 * */
public class DataInput {
    /**
     * Get integer from user input
     * @throws IOException when input cannot be read
     * @throws NumberFormatException when input cannot be converted to int
     * */
    public static Integer getInt() throws IOException, NumberFormatException {
        String s = getString();
        return Integer.valueOf(s);
    }

    /**
     * Get string from user input
     * @throws IOException when input cannot be read
     * */
    public static String getString() throws IOException {
        InputStreamReader isr = new InputStreamReader(System.in);
        BufferedReader br = new BufferedReader(isr);
        return br.readLine();
    }
}
