package usage.cases;

import datainput.DataInput;
import exceptions.AlreadyExistsException;
import exceptions.NotFoundException;
import hierarchy.University;
import usage.common.Common;

import java.io.IOException;
import java.util.Map;

/**
 * API Testing - case #2
 * */
public class UsageSecond {
    public static void second(University university) {
        System.out.print(
            "Якщо Ви хочете створити кафедру факультета - натисніть 1, видалити - 2, редагувати - 3: "
        );

        int innerChoice;
        try {
            innerChoice = Common.getThreeChoice();
        } catch (IOException | IllegalArgumentException e) {
            System.out.println("Не цифра або не між 1 та 3.");
            return;
        }

        switch (innerChoice) {
            case 1 -> secondCreate(university);
            case 2 -> secondDelete(university);
            case 3 -> secondModify(university);
        }
    }

    private static void secondCreate(University university) {
        System.out.println(
            "Щоб створити кафедру, спочатку уведіть факультет, що існує, потім ім'я нової кафедри"
        );

        System.out.print("Уведіть ім'я факультету: ");
        String facultyName;
        try {
            facultyName = DataInput.getString();
        } catch (IOException e) {
            System.out.println("Неправильний увід");
            return;
        }

        System.out.print("Уведіть ім'я нової кафедри: ");
        String departmentName;
        try {
            departmentName = DataInput.getString();
        } catch (IOException e) {
            System.out.println("Неправильний увід");
            return;
        }

        try {
            university.addFacultyDepartment(facultyName, departmentName);
        } catch (NotFoundException e) {
            System.out.println("Факультет не існує - спочатку створіть його");
            return;
        } catch (AlreadyExistsException e) {
            System.out.println("Указана кафедра уже існує");
            return;
        }

        System.out.println("Кафедра була успішно створена");
    }

    private static void secondDelete(University university) {
        System.out.println(
            "Щоб видалити кафедру, спочатку уведіть факультет, потім ім'я кафедри"
        );

        Map.Entry<String, String> entry;
        try {
            entry = Common.getFacultyWithDepartment();
        } catch (IOException e) {
            System.out.println("Неправильний увід");
            return;
        }

        try {
            university.deleteFacultyDepartment(entry.getKey(), entry.getValue());
        } catch (NotFoundException e) {
            System.out.println("Факультет або кафедра не існує - спочатку створіть його/її");
            return;
        }

        System.out.println("Кафедру було успішно видалено");
    }

    private static void secondModify(University university) {
        System.out.println(
            "Щоб відредагувати кафедру, спочатку уведіть факультет, потім старе ім'я кафедри, а потім - нове"
        );

        System.out.print("Уведіть ім'я факультету: ");
        String facultyName;
        try {
            facultyName = DataInput.getString();
        } catch (IOException e) {
            System.out.println("Неправильний увід");
            return;
        }

        System.out.print("Уведіть старе ім'я кафедри: ");
        String oldDepartmentName;
        try {
            oldDepartmentName = DataInput.getString();
        } catch (IOException e) {
            System.out.println("Неправильний увід");
            return;
        }

        System.out.print("Уведіть нове ім'я кафедри: ");
        String newDepartmentName;
        try {
            newDepartmentName = DataInput.getString();
        } catch (IOException e) {
            System.out.println("Неправильний увід");
            return;
        }

        try {
            university.updateFacultyDepartmentName(facultyName, oldDepartmentName, newDepartmentName);
        } catch (NotFoundException e) {
            System.out.println("Факультет або кафедра не існує - спочатку створіть його/її");
            return;
        }

        System.out.println("Кафедру було успішно оновлено");
    }
}
