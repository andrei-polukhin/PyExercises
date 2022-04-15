package usage.cases;

import datainput.DataInput;
import exceptions.AlreadyExistsException;
import exceptions.NotFoundException;
import hierarchy.University;
import usage.common.Common;

import java.io.IOException;
import java.util.Map;

/**
 * API Testing - case #3
 * */
public class UsageThird {
    public static void third(University university) {
        System.out.print(
            "Якщо Ви хочете робити операції з студентом - уведіть 1, викладачем - 2: "
        );

        int innerChoice;
        try {
            innerChoice = DataInput.getInt();
        } catch (IOException | NumberFormatException e) {
            System.out.println("Не цифра.");
            return;
        }
        if (innerChoice < 1 || innerChoice > 2) {
            System.out.println("Цифра має бути від 1 до 2 включно");
            return;
        }

        switch (innerChoice) {
            case 1 -> thirdStudent(university);
            case 2 -> thirdTeacher(university);
        }
    }

    /**
     * Case #3 - Student
     * */
    private static void thirdStudent(University university) {
        System.out.print(
            "Якщо Ви хочете додати студента - уведіть 1, видалити - 2, редагувати - 3: "
        );

        int innerChoice;
        try {
            innerChoice = Common.getThreeChoice();
        } catch (IOException | IllegalArgumentException e) {
            System.out.println("Не цифра або не між 1 та 3.");
            return;
        }

        switch (innerChoice) {
            case 1 -> studentCreate(university);
            case 2 -> studentDelete(university);
            case 3 -> studentModify(university);
        }
    }

    private static void studentCreate(University university) {
        System.out.println(
            "Якщо Ви хочете додати студента, спочатку уведіть інформацію про факультет та кафедру, " +
            "а потім уведіть дані студента"
        );

        Map.Entry<String, String> entry;
        try {
            entry = Common.getFacultyWithDepartment();
        } catch (IOException e) {
            System.out.println("Неправильний увід");
            return;
        }

        System.out.print("Уведіть курс студента: ");
        int studentCourse;
        try {
            studentCourse = DataInput.getInt();
        } catch (IOException|NumberFormatException e) {
            System.out.println("Неправильний увід");
            return;
        }

        System.out.print("Уведіть групу студента: ");
        int studentGroup;
        try {
            studentGroup = DataInput.getInt();
        } catch (IOException|NumberFormatException e) {
            System.out.println("Неправильний увід");
            return;
        }

        System.out.print("Уведіть ім'я студента: ");
        String studentFullName;
        try {
            studentFullName = DataInput.getString();
        } catch (IOException e) {
            System.out.println("Неправильний увід");
            return;
        }

        try {
            university.addStudentToFacultyDepartment(
                entry.getKey(), entry.getValue(),
                studentCourse, studentGroup, studentFullName
            );
        } catch (NotFoundException e) {
            System.out.println("Факультет або кафедра не існують");
            return;
        } catch (AlreadyExistsException e) {
            System.out.println("Указаний студент вже існує");
            return;
        } catch (IllegalArgumentException e) {
            System.out.println("Неправильний курс або група");
            return;
        }

        System.out.println("Студента успішно створено");
    }

    private static void studentDelete(University university) {
        System.out.println(
            "Якщо Ви хочете видалити студента, спочатку уведіть інформацію про факультет та кафедру, " +
                    "а потім повне ім'я студента"
        );

        Map.Entry<String, String> entry;
        try {
            entry = Common.getFacultyWithDepartment();
        } catch (IOException e) {
            System.out.println("Неправильний увід");
            return;
        }

        System.out.print("Уведіть ім'я студента: ");
        String studentFullName;
        try {
            studentFullName = DataInput.getString();
        } catch (IOException e) {
            System.out.println("Неправильний увід");
            return;
        }

        try {
            university.removeStudentFromFacultyDepartment(
                    entry.getKey(), entry.getValue(),
                    studentFullName
            );
        } catch (NotFoundException e) {
            System.out.println("Факультет або кафедра або студент не існують");
            return;
        }

        System.out.println("Студента успішно видалено");
    }

    private static void studentModify(University university) {
        System.out.println(
            "Якщо Ви хочете редагувати студента, спочатку уведіть інформацію про факультет та кафедру, " +
                    "а потім уведіть дані студента"
        );

        // old
        Map.Entry<String, String> entry;
        try {
            entry = Common.getFacultyWithDepartment();
        } catch (IOException e) {
            System.out.println("Неправильний увід");
            return;
        }

        System.out.print("Уведіть ім'я студента наразі: ");
        String oldStudentFullName;
        try {
            oldStudentFullName = DataInput.getString();
        } catch (IOException e) {
            System.out.println("Неправильний увід");
            return;
        }

        // new
        System.out.print("Уведіть нове ім'я студента (Enter, щоб пропустити): ");
        String newStudentFullName;
        try {
            newStudentFullName = DataInput.getString();
        } catch (IOException e) {
            System.out.println("Неправильний увід");
            return;
        }
        if (newStudentFullName.equals("")) {
            newStudentFullName = null;
        }

        System.out.print("Уведіть новий курс студента (Enter, щоб пропустити): ");
        int newStudentCourse;
        try {
            newStudentCourse = DataInput.getInt();
        } catch (IOException e) {
            System.out.println("Неправильний увід");
            return;
        } catch (NumberFormatException e) {
            newStudentCourse = Integer.MIN_VALUE;
        }

        System.out.print("Уведіть нову групу студента (Enter, щоб пропустити): ");
        int newStudentGroup;
        try {
            newStudentGroup = DataInput.getInt();
        } catch (IOException e) {
            System.out.println("Неправильний увід");
            return;
        } catch (NumberFormatException e) {
            newStudentGroup = Integer.MIN_VALUE;
        }

        try {
            university.updateStudentInFacultyDepartment(
                    entry.getKey(), entry.getValue(),
                    oldStudentFullName,
                    newStudentCourse, newStudentGroup, newStudentFullName
            );
        } catch (NotFoundException e) {
            System.out.println("Факультет або кафедра або студент не існують");
            return;
        } catch (IllegalArgumentException e) {
            System.out.println("Курс уведено неправильно");
        }

        System.out.println("Студента успішно оновлено");
    }

    /**
     * Case #3 - Teacher
     * */
    private static void thirdTeacher(University university) {
        System.out.print(
            "Якщо Ви хочете додати вчителя - уведіть 1, видалити - 2, редагувати - 3: "
        );

        int innerChoice;
        try {
            innerChoice = Common.getThreeChoice();
        } catch (IOException | IllegalArgumentException e) {
            System.out.println("Не цифра або не між 1 та 3.");
            return;
        }

        switch (innerChoice) {
            case 1 -> teacherCreate(university);
            case 2 -> teacherDelete(university);
            case 3 -> teacherModify(university);
        }
    }

    private static void teacherCreate(University university) {
        System.out.println(
            "Якщо Ви хочете додати вчителя, спочатку уведіть інформацію про факультет та кафедру, " +
                    "а потім уведіть дані студента"
        );

        Map.Entry<String, String> entry;
        try {
            entry = Common.getFacultyWithDepartment();
        } catch (IOException e) {
            System.out.println("Неправильний увід");
            return;
        }

        System.out.print("Уведіть курс вчителя: ");
        int studentCourse;
        try {
            studentCourse = DataInput.getInt();
        } catch (IOException|NumberFormatException e) {
            System.out.println("Неправильний увід");
            return;
        }

        System.out.print("Уведіть групу вчителя: ");
        int studentGroup;
        try {
            studentGroup = DataInput.getInt();
        } catch (IOException|NumberFormatException e) {
            System.out.println("Неправильний увід");
            return;
        }

        System.out.print("Уведіть ім'я вчителя: ");
        String studentFullName;
        try {
            studentFullName = DataInput.getString();
        } catch (IOException e) {
            System.out.println("Неправильний увід");
            return;
        }

        try {
            university.addTeacherToFacultyDepartment(
                    entry.getKey(), entry.getValue(),
                    studentCourse, studentGroup, studentFullName
            );
        } catch (NotFoundException e) {
            System.out.println("Факультет або кафедра не існують");
            return;
        } catch (AlreadyExistsException e) {
            System.out.println("Указаний вчитель вже існує");
            return;
        } catch (IllegalArgumentException e) {
            System.out.println("Неправильний курс або група");
            return;
        }

        System.out.println("Вчителя успішно створено");
    }

    private static void teacherDelete(University university) {
        System.out.println(
            "Якщо Ви хочете видалити вчителя, спочатку уведіть інформацію про факультет та кафедру, " +
                    "а потім повне ім'я вчителя"
        );

        Map.Entry<String, String> entry;
        try {
            entry = Common.getFacultyWithDepartment();
        } catch (IOException e) {
            System.out.println("Неправильний увід");
            return;
        }

        System.out.print("Уведіть ім'я вчителя: ");
        String studentFullName;
        try {
            studentFullName = DataInput.getString();
        } catch (IOException e) {
            System.out.println("Неправильний увід");
            return;
        }

        try {
            university.removeTeacherFromFacultyDepartment(
                    entry.getKey(), entry.getValue(), studentFullName
            );
        } catch (NotFoundException e) {
            System.out.println("Факультет або кафедра або вчитель не існують");
            return;
        }

        System.out.println("Вчителя успішно видалено");
    }

    private static void teacherModify(University university) {
        System.out.println(
            "Якщо Ви хочете редагувати вчителя, спочатку уведіть інформацію про факультет та кафедру, " +
                    "а потім уведіть дані вчителя"
        );

        // old
        Map.Entry<String, String> entry;
        try {
            entry = Common.getFacultyWithDepartment();
        } catch (IOException e) {
            System.out.println("Неправильний увід");
            return;
        }

        System.out.print("Уведіть ім'я вчителя наразі: ");
        String oldStudentFullName;
        try {
            oldStudentFullName = DataInput.getString();
        } catch (IOException e) {
            System.out.println("Неправильний увід");
            return;
        }

        // new
        System.out.print("Уведіть нове ім'я вчителя (Enter, щоб пропустити): ");
        String newStudentFullName;
        try {
            newStudentFullName = DataInput.getString();
        } catch (IOException e) {
            System.out.println("Неправильний увід");
            return;
        }
        if (newStudentFullName.equals("")) {
            newStudentFullName = null;
        }

        System.out.print("Уведіть новий курс вчителя (Enter, щоб пропустити): ");
        int newStudentCourse;
        try {
            newStudentCourse = DataInput.getInt();
        } catch (IOException e) {
            System.out.println("Неправильний увід");
            return;
        } catch (NumberFormatException e) {
            newStudentCourse = Integer.MIN_VALUE;
        }

        System.out.print("Уведіть нову групу вчителя (Enter, щоб пропустити): ");
        int newStudentGroup;
        try {
            newStudentGroup = DataInput.getInt();
        } catch (IOException e) {
            System.out.println("Неправильний увід");
            return;
        } catch (NumberFormatException e) {
            newStudentGroup = Integer.MIN_VALUE;
        }

        try {
            university.updateTeacherInFacultyDepartment(
                    entry.getKey(), entry.getValue(),
                    oldStudentFullName,
                    newStudentCourse, newStudentGroup, newStudentFullName
            );
        } catch (NotFoundException e) {
            System.out.println("Факультет або кафедра або вчитель не існують");
            return;
        } catch (IllegalArgumentException e) {
            System.out.println("Курс уведено неправильно");
            return;
        }

        System.out.println("Вчителя успішно оновлено");
    }
}
