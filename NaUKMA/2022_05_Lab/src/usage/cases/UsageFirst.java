package usage.cases;

import datainput.DataInput;
import exceptions.AlreadyExistsException;
import exceptions.NotFoundException;
import hierarchy.University;
import usage.common.Common;

import java.io.IOException;

/**
 * API Testing - case #1
 * */
public class UsageFirst {
    public static void first(University university) {
        System.out.print(
                "Якщо Ви хочете створити факультет - натисніть 1, видалити - 2, редагувати - 3: "
        );

        int innerChoice;
        try {
            innerChoice = Common.getThreeChoice();
        } catch (IOException | IllegalArgumentException e) {
            System.out.println("Не цифра або не між 1 та 3.");
            return;
        }

        switch (innerChoice) {
            case 1 -> firstCreate(university);
            case 2 -> firstDelete(university);
            case 3 -> firstModify(university);
        }
    }

    private static void firstCreate(University university) {
        System.out.print("Щоб створити факультет, уведіть його ім'я: ");

        String facultyName;
        try {
            facultyName = DataInput.getString();
        } catch (IOException e) {
            System.out.println("Неправильний увід");
            return;
        }

        try {
            university.addFaculty(facultyName);
        } catch (AlreadyExistsException e) {
            System.out.println("Цей факультет уже існує, неможливо створити");
            return;
        }

        System.out.println("Факультет було успішно створено");
    }

    private static void firstDelete(University university) {
        System.out.print("Щоб видалити факультет, уведіть його ім'я: ");

        String facultyName;
        try {
            facultyName = DataInput.getString();
        } catch (IOException e) {
            System.out.println("Неправильний увід");
            return;
        }

        try {
            university.removeFaculty(facultyName);
        } catch (NotFoundException e) {
            System.out.println("Цей факультет не існує, неможливо видалити");
            return;
        }

        System.out.println("Факультет було успішно видалено");
    }

    private static void firstModify(University university) {
        System.out.println("Щоб відредагувати факультет, уведіть його старе ім'я, а потім нове");

        System.out.print("Старе ім'я: ");
        String oldFacultyName;
        try {
            oldFacultyName = DataInput.getString();
        } catch (IOException e) {
            System.out.println("Неправильний увід");
            return;
        }

        System.out.print("Нове ім'я: ");
        String newFacultyName;
        try {
            newFacultyName = DataInput.getString();
        } catch (IOException e) {
            System.out.println("Неправильний увід");
            return;
        }

        try {
            university.updateFacultyName(oldFacultyName, newFacultyName);
        } catch (NotFoundException e) {
            System.out.println("Цей факультет не існує, неможливо редагувати");
            return;
        }

        System.out.println("Факультет було успішно відредаговано");
    }
}
