package usage.cases;

import datainput.DataInput;
import exceptions.NotFoundException;
import hierarchy.University;
import usage.common.Common;

import java.io.IOException;

/**
 * API Testing - Case #4
 * */
public class UsageFourth {
    public static void fourth(University university) {
        System.out.print(
            "Якщо Ви хочете знайти інформацію про студента - натисніть 1, викладача - 2: "
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
            "Якщо Ви хочете знайти інформацію про студента, уведіть його повне ім'я"
        );

        System.out.print("Уведіть ім'я студента: ");
        String studentName;
        try {
            studentName = DataInput.getString();
        } catch (IOException e) {
            System.out.println("Неправильний увід");
            return;
        }

        try {
            System.out.println(university.findStudentByFullNameAmongAll(studentName));
        } catch (NotFoundException e) {
            System.out.println("Студента не знайдено");
        }
    }

    private static void teacher(University university) {
        System.out.println(
            "Якщо Ви хочете знайти інформацію про викладача, уведіть його повне ім'я"
        );

        System.out.print("Уведіть ім'я викладача: ");
        String studentName;
        try {
            studentName = DataInput.getString();
        } catch (IOException e) {
            System.out.println("Неправильний увід");
            return;
        }

        try {
            System.out.println(university.findTeacherByFullNameAmongAll(studentName));
        } catch (NotFoundException e) {
            System.out.println("Студента не знайдено");
        }
    }
}
