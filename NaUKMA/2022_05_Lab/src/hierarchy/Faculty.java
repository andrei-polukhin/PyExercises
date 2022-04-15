package hierarchy;

import entities.Student;
import entities.Teacher;

import java.util.ArrayList;
import java.util.Comparator;

/**
 * Faculty of the university
 * */
class Faculty {
    private String name;
    private final ArrayList<Department> departments;

    Faculty(String name) {
        this.name = name;
        this.departments = new ArrayList<>();
    }

    @Override
    public String toString() {
        return "Faculty{" +
                "name='" + name + '\'' +
                ", departments=" + departments +
                '}';
    }

    String getName() {
        return name;
    }

    void setName(String name) {
        this.name = name;
    }

    ArrayList<Department> getDepartments() {
        return departments;
    }

    void addDepartment(String departmentName) {
        departments.add(new Department(departmentName));
    }

    Department findDepartment(String name) {
        for (Department department : departments) {
            if (department.getName().equals(name)) {
                return department;
            }
        }
        return null;
    }

    void removeDepartment(Department department) {
        departments.remove(department);
    }

    ArrayList<Student> getStudentsOrderedByFullName() {
        ArrayList<Student> result = new ArrayList<>();
        for (Department department : departments) {
            result.addAll(department.getStudents());
        }

        result.sort(Comparator.comparing(Student::getFullName));
        return result;
    }

    ArrayList<Teacher> getTeachersOrderedByFullName() {
        ArrayList<Teacher> result = new ArrayList<>();
        for (Department department : departments) {
            result.addAll(department.getTeachers());
        }

        result.sort(Comparator.comparing(Teacher::getFullName));
        return result;
    }
}
