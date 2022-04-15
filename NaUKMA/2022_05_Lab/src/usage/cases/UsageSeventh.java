package usage.cases;

import exceptions.NotFoundException;
import hierarchy.University;
import usage.common.Common;

import java.io.IOException;
import java.util.Map;

/**
 * API Testing - Case #7
 * */
public class UsageSeventh {
    public static void seventh(University university) {
        System.out.println(
            "Якщо Ви хочете знайти інформацію про студентів кафедри, уведіть факультет і кафедру"
        );

        Map.Entry<String, String> entry;
        try {
            entry = Common.getFacultyWithDepartment();
        } catch (IOException e) {
            System.out.println("Неправильний увід");
            return;
        }

        try {
            System.out.println(university.getAllDepartmentStudentsOrderedByCourse(
                    entry.getKey(), entry.getValue()
            ));
        } catch (NotFoundException e) {
            System.out.println("Факультет або кафедра не існує");
        }
    }
}
