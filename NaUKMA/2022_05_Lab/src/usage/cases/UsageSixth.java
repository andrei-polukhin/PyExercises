package usage.cases;

import datainput.DataInput;
import exceptions.NotFoundException;
import hierarchy.University;
import usage.common.Common;

import java.io.IOException;

public class UsageSixth {
    public static void sixth(University university) {
        System.out.print(
            "Якщо Ви хочете знайти інформацію про студентів - натисніть 1, викладачів - 2: "
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
        System.out.println("Щоб знайти інформацію про студентів, уведіть ім'я факультету");

        System.out.print("Уведіть ім'я факультету: ");
        String facultyName;
        try {
            facultyName = DataInput.getString();
        } catch (IOException e) {
            System.out.println("Неправильний увід");
            return;
        }

        try {
            System.out.println(university.getAllFacultyStudentsOrderedByFullName(facultyName));
        } catch (NotFoundException e) {
            System.out.println("Факультет не знайдено");
        }
    }

    private static void teacher(University university) {
        System.out.println("Щоб знайти інформацію про студентів, уведіть ім'я факультету");

        System.out.print("Уведіть ім'я факультету: ");
        String facultyName;
        try {
            facultyName = DataInput.getString();
        } catch (IOException e) {
            System.out.println("Неправильний увід");
            return;
        }

        try {
            System.out.println(university.getAllFacultyTeachersOrderedByFullName(facultyName));
        } catch (NotFoundException e) {
            System.out.println("Факультет не знайдено");
        }
    }
}
