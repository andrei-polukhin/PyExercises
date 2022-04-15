package usage.cases;

import exceptions.NotFoundException;
import hierarchy.University;
import usage.common.Common;

import java.io.IOException;
import java.util.Map;

/**
 * API Testing - Case #8
 * */
public class UsageEighth {
    public static void eighth(University university) {
        System.out.print(
            "Якщо Ви хочете робити операції з студентами - уведіть 1, викладачами - 2: "
        );

        int innerChoice;
        try {
            innerChoice = Common.getTwoChoice();
        } catch (IOException | IllegalArgumentException e) {
            System.out.println("Не цифра або не між 1 та 2.");
            return;
        }

        switch (innerChoice) {
            case 1 -> student(university);
            case 2 -> teacher(university);
        }
    }

    private static void student(University university) {
        System.out.println(
            "Якщо Ви хочете знайти інформацію про студентів, спочатку уведіть інформацію про факультет та кафедру"
        );

        Map.Entry<String, String> entry;
        try {
            entry = Common.getFacultyWithDepartment();
        } catch (IOException e) {
            System.out.println("Неправильний увід");
            return;
        }

        try {
            System.out.println(university.getAllDepartmentStudentsOrderedByFullName(
                    entry.getKey(), entry.getValue()
            ));
        } catch (NotFoundException e) {
            System.out.println("Факультет або кафедра не існує");
        }
    }

    private static void teacher(University university) {
        System.out.println(
            "Якщо Ви хочете знайти інформацію про вчителів, спочатку уведіть інформацію про факультет та кафедру"
        );

        Map.Entry<String, String> entry;
        try {
            entry = Common.getFacultyWithDepartment();
        } catch (IOException e) {
            System.out.println("Неправильний увід");
            return;
        }

        try {
            System.out.println(university.getAllDepartmentTeachersOrderedByFullName(
                entry.getKey(), entry.getValue()
            ));
        } catch (NotFoundException e) {
            System.out.println("Факультет або кафедра не існує");
        }
    }
}
