package hierarchy;

import entities.*;

import java.util.ArrayList;
import java.util.Comparator;

/**
 * Department of the faculty of the university
 * */
class Department {
    private String name;
    private final ArrayList<Student> students;
    private final ArrayList<Teacher> teachers;

    Department(String name) {
        this.name = name;
        this.students = new ArrayList<>();
        this.teachers = new ArrayList<>();
    }

    @Override
    public String toString() {
        return "Department{" +
                "name='" + name + '\'' +
                ", students=" + students +
                ", teachers=" + teachers +
                '}';
    }

    String getName() {
        return name;
    }

    void setName(String name) {
        this.name = name;
    }

    ArrayList<Student> getStudents() {
        return students;
    }

    ArrayList<Teacher> getTeachers() {
        return teachers;
    }

    void addStudent(int course, int group, String fullName) {
        students.add(new Student(course, group, fullName));
    }

    void addTeacher(int course, int group, String fullName) {
        teachers.add(new Teacher(course, group, fullName));
    }

    ArrayList<Student> getStudentsOrderedByCourse() {
        students.sort(Comparator.comparingInt(Student::getCourse));
        return students;
    }

    ArrayList<Student> getStudentsOrderedByFullName() {
        students.sort(Comparator.comparing(Student::getFullName));
        return students;
    }

    ArrayList<Teacher> getTeachersOrderedByFullName() {
        teachers.sort(Comparator.comparing(Teacher::getFullName));
        return teachers;
    }

    ArrayList<Student> getStudentsOfCourse(int course) {
        ArrayList<Student> result = new ArrayList<>();

        for (Student student : students) {
            if (student.getCourse() == course) {
                result.add(student);
            }
        }

        return result;
    }

    ArrayList<Student> getStudentsOfCourseOrderedByFullName(int course) {
        ArrayList<Student> woOrder = getStudentsOfCourse(course);
        woOrder.sort(Comparator.comparing(Student::getFullName));
        return woOrder;
    }

    Student findStudentByFullName(String fullName) {
        for (Student student : students) {
            if (student.getFullName().equals(fullName)) {
                return student;
            }
        }
        return null;
    }

    Teacher findTeacherByFullName(String fullName) {
        for (Teacher teacher : teachers) {
            if (teacher.getFullName().equals(fullName)) {
                return teacher;
            }
        }
        return null;
    }

    void removeStudent(Student student) {
        students.remove(student);
    }

    void removeTeacher(Teacher teacher) {
        teachers.remove(teacher);
    }
}
