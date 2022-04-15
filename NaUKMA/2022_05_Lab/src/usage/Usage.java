package usage;

import datainput.DataInput;
import hierarchy.University;
import usage.cases.*;

import java.io.IOException;

/**
 * Test API!
 * */
public class Usage {
    private static University university = null;

    public static void main(String[] args) {
        // intro
        System.out.println("=== ВІТАЄМО В МЕНЮ ПРОГРАМИ ==");

        // create a university
        University university;
        try {
            university = createUniversity();
        } catch (IOException e) {
            System.out.println("Спробуйте ще раз. Перезавантажте програму...");
            return;
        }
        Usage.university = university;
        System.out.println();

        // handle choice
        handleChoice();
    }

    private static University createUniversity() throws IOException {
        System.out.print("Введіть ім'я університету (рекомендовано НаУКМА): ");
        String universityName = DataInput.getString();
        return new University(universityName);
    }

    private static void printInstruction() {
        System.out.println("--= ОБЕРІТЬ ОДИН З ВАРІАНТІВ --=");
        System.out.println("1. Створити/видалити/редагувати факультет.");
        System.out.println("2. Створити/видалити/редагувати кафедру факультета.");
        System.out.println("3. Додати/видалити/редагувати студента/викладача до кафедри.");
        System.out.println("4. Знайти студента/викладача за ПІБ, курсом або групою.");
        System.out.println("5. Вивести всіх студентів впорядкованих за курсами.");
        System.out.println("6. Вивести всіх студентів/викладачів факультета впорядкованих за алфавітом.");
        System.out.println("7. Вивести всіх студентів кафедри впорядкованих за курсами.");
        System.out.println("8. Вивести всіх студентів/викладачів кафедри впорядкованих за алфавітом.");
        System.out.println("9. Вивести всіх студентів кафедри вказаного курсу.");
        System.out.println("10. Вивести всіх студентів кафедри вказаного курсу впорядкованих за алфавітом.");
    }

    private static void handleChoice() {
        int proceed = 1;

        do {
            // print instructions
            printInstruction();
            System.out.println();

            // choice of method
            System.out.print("Зробіть свій вибір (уведіть число від 1 до 10 включно): ");
            int choice;
            try {
                choice = DataInput.getInt();
            } catch (IOException|NumberFormatException e) {
                System.out.println("Спробуйте ще раз");
                continue;
            }
            if (choice < 1 || choice > 10) {
                System.out.println("Уведіть число від 1 до 10 включно, спробуйте ще раз");
                continue;
            }
            handleMethods(choice);

            // loop of attempts
            try {
                System.out.print("Уведіть 1, щоб продовжити, 0 в іншому випадку: ");
                proceed = DataInput.getInt();
            } catch (IOException|NumberFormatException e) {
                break;
            }
        } while (proceed == 1);
    }

    private static void handleMethods(int methodNumber) {
        switch (methodNumber) {
            case 1 -> UsageFirst.first(university);
            case 2 -> UsageSecond.second(university);
            case 3 -> UsageThird.third(university);
            case 4 -> UsageFourth.fourth(university);
            case 5 -> UsageFifth.fifth(university);
            case 6 -> UsageSixth.sixth(university);
            case 7 -> UsageSeventh.seventh(university);
            case 8 -> UsageEighth.eighth(university);
            case 9 -> UsageNinth.ninth(university);
            case 10 -> UsageTenth.tenth(university);
        }
    }
}
