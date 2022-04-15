package usage.cases;

import datainput.DataInput;
import exceptions.NotFoundException;
import hierarchy.University;
import usage.common.Common;

import java.io.IOException;
import java.util.Map;

/**
 * API Testing - Case #9
 * */
public class UsageNinth {
    public static void ninth(University university) {
        System.out.println("Щоб вивести всіх студентів указаного курсу, уведіть факультет, кафедру та курс студентів");

        Map.Entry<String, String> entry;
        try {
            entry = Common.getFacultyWithDepartment();
        } catch (IOException e) {
            System.out.println("Неправильний увід");
            return;
        }

        System.out.print("Уведіть курс студентів: ");
        int studentCourse;
        try {
            studentCourse = DataInput.getInt();
        } catch (IOException|NumberFormatException e) {
            System.out.println("Неправильний увід");
            return;
        }

        try {
            System.out.println(
                university.getAllDepartmentStudentsOfCourse(
                    entry.getKey(), entry.getValue(), studentCourse
                )
            );
        } catch (NotFoundException e) {
            System.out.println("Факультет або кафедра не існує");
        }
    }
}
