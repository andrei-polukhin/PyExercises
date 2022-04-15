package usage.common;

import datainput.DataInput;

import java.io.IOException;
import java.util.AbstractMap;
import java.util.Map;

/**
 * Common STDIN patterns
 * */
public class Common {
    /**
     * Get faculty with department
     * @return The faculty -> department map entry
     * */
    public static Map.Entry<String, String> getFacultyWithDepartment() throws IOException {
        System.out.print("Уведіть ім'я факультету: ");
        String facultyName = DataInput.getString();

        System.out.print("Уведіть ім'я кафедри: ");
        String departmentName = DataInput.getString();

        return new AbstractMap.SimpleEntry<>(facultyName, departmentName);
    }

    /**
     * Choice between 1 and 2 inclusive
     * */
    public static int getTwoChoice() throws IOException, IllegalArgumentException {
        int innerChoice = DataInput.getInt();
        if (innerChoice < 1 || innerChoice > 2) {
            throw new IllegalArgumentException();
        }
        return innerChoice;
    }

    /**
     * Choice between 1 and 3 inclusive
     * */
    public static int getThreeChoice() throws IOException, IllegalArgumentException {
        int innerChoice = DataInput.getInt();
        if (innerChoice < 1 || innerChoice > 3) {
            throw new IllegalArgumentException();
        }
        return innerChoice;
    }
}
