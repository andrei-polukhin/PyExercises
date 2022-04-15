package hierarchy;

import exceptions.AlreadyExistsException;
import exceptions.NotFoundException;

import entities.*;

import java.util.AbstractMap;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.Map;

/**
 * University class.
 *
 * Main entrypoint of the API.
 * */
public class University {
    private final String name;
    private final ArrayList<Faculty> faculties;

    public University(String name) {
        this.name = name;
        this.faculties = new ArrayList<>();
    }

    @Override
    public String toString() {
        return "University{" +
                "name='" + name + '\'' +
                ", faculties=" + faculties +
                '}';
    }

    /**
     * Helper method to find faculty by name
     * */
    private Faculty getFaculty(String facultyName) {
        for (Faculty faculty : faculties) {
            if (faculty.getName().equals(facultyName)) {
                return faculty;
            }
        }
        return null;
    }

    /**
     * Helper method to find a pair of the department and the student
     * in the whole university
     * */
    private Map.Entry<Department, Student> findStudentWithDepartmentAmongAll(
        String facultyName, String departmentName, String studentFullName
    ) throws NotFoundException {
        Faculty foundFaculty = getFaculty(facultyName);
        if (foundFaculty == null) {
            throw new NotFoundException();
        }
        Department foundDepartment = foundFaculty.findDepartment(departmentName);
        if (foundDepartment == null) {
            throw new NotFoundException();
        }
        Student foundStudent = foundDepartment.findStudentByFullName(studentFullName);
        if (foundStudent == null) {
            throw new NotFoundException();
        }

        return new AbstractMap.SimpleEntry<>(foundDepartment, foundStudent);
    }

    /**
     * Helper method to find a pair of the department and the teacher
     * in the whole university
     * */
    private Map.Entry<Department, Teacher> findTeacherWithDepartmentAmongAll(
            String facultyName, String departmentName, String teacherFullName
    ) throws NotFoundException {
        Faculty foundFaculty = getFaculty(facultyName);
        if (foundFaculty == null) {
            throw new NotFoundException();
        }
        Department foundDepartment = foundFaculty.findDepartment(departmentName);
        if (foundDepartment == null) {
            throw new NotFoundException();
        }
        Teacher foundTeacher = foundDepartment.findTeacherByFullName(teacherFullName);
        if (foundTeacher == null) {
            throw new NotFoundException();
        }

        return new AbstractMap.SimpleEntry<>(foundDepartment, foundTeacher);
    }

    /**
     * Case #1: add the faculty to the university
     * */
    public void addFaculty(String facultyName) throws AlreadyExistsException {
        if (getFaculty(facultyName) != null) {
            throw new AlreadyExistsException();
        }
        faculties.add(new Faculty(facultyName));
    }

    /**
     * Case #1: update the faculty of the university
     * */
    public void updateFacultyName(String oldName, String newName) throws NotFoundException {
        Faculty foundFaculty = getFaculty(oldName);
        if (foundFaculty == null) {
            throw new NotFoundException();
        }

        foundFaculty.setName(newName);
    }

    /**
     * Case #1: delete the faculty of the university
     * */
    public void removeFaculty(String facultyName) throws NotFoundException {
        Faculty foundFaculty = getFaculty(facultyName);
        if (foundFaculty == null) {
            throw new NotFoundException();
        }
        faculties.remove(foundFaculty);
    }

    /**
     * Case #2: add the department of the faculty of the university
     * */
    public void addFacultyDepartment(
        String facultyName, String departmentName
    ) throws NotFoundException, AlreadyExistsException {
        Faculty foundFaculty = getFaculty(facultyName);
        if (foundFaculty == null) {
            throw new NotFoundException();
        }

        if (foundFaculty.findDepartment(departmentName) != null) {
            throw new AlreadyExistsException();
        }

        foundFaculty.addDepartment(departmentName);
    }

    /**
     * Case #2: update the department of the faculty of the university (name)
     * */
    public void updateFacultyDepartmentName(
        String facultyName, String oldDepartmentName, String newDepartmentName
    ) throws NotFoundException {
        Faculty foundFaculty = getFaculty(facultyName);
        if (foundFaculty == null) {
            throw new NotFoundException();
        }

        Department foundDepartment = foundFaculty.findDepartment(oldDepartmentName);
        if (foundDepartment == null) {
            throw new NotFoundException();
        }

        foundDepartment.setName(newDepartmentName);
    }

    /**
     * Case #2: remove the department of the faculty of the university
     * */
    public void deleteFacultyDepartment(String facultyName, String departmentName) throws NotFoundException {
        Faculty foundFaculty = getFaculty(facultyName);
        if (foundFaculty == null) {
            throw new NotFoundException();
        }

        Department foundDepartment = foundFaculty.findDepartment(departmentName);
        if (foundDepartment == null) {
            throw new NotFoundException();
        }

        foundFaculty.removeDepartment(foundDepartment);
    }

    /**
     * Case #3: add a student to the department of the faculty of the university
     * */
    public void addStudentToFacultyDepartment(
        String facultyName, String departmentName,
        int studentCourse, int studentGroup, String studentFullName
    ) throws NotFoundException, AlreadyExistsException {
        Faculty foundFaculty = getFaculty(facultyName);
        if (foundFaculty == null) {
            throw new NotFoundException();
        }
        if (studentCourse < 1 || studentCourse > 4 || studentGroup < 1) {
            throw new IllegalArgumentException();
        }
        Department foundDepartment = foundFaculty.findDepartment(departmentName);
        if (foundDepartment == null) {
            throw new NotFoundException();
        }

        if (foundDepartment.findStudentByFullName(studentFullName) != null) {
            throw new AlreadyExistsException();
        }

        foundDepartment.addStudent(studentCourse, studentGroup, studentFullName);
    }

    /**
     * Case #3: remove a student from the department of the faculty of the university
     * */
    public void removeStudentFromFacultyDepartment(
        String facultyName, String departmentName,
        String studentFullName
    ) throws NotFoundException {
        Map.Entry<Department, Student> entry = findStudentWithDepartmentAmongAll(facultyName, departmentName, studentFullName);
        Department foundDepartment = entry.getKey();
        Student foundStudent = entry.getValue();
        foundDepartment.removeStudent(foundStudent);
    }

    /**
     * Case #3: update a student in the department of the faculty of the university
     * */
    public void updateStudentInFacultyDepartment(
        String facultyName, String departmentName,
        String oldStudentFullName,
        int newCourse, int newGroup, String newFullName
    ) throws NotFoundException, IllegalArgumentException {
        if ((newCourse < 1 || newCourse > 4) && newCourse != Integer.MIN_VALUE) {
            throw new IllegalArgumentException();
        }
        if (newGroup < 1 && newGroup != Integer.MIN_VALUE) {
            throw new IllegalArgumentException();
        }

        Map.Entry<Department, Student> entry = findStudentWithDepartmentAmongAll(facultyName, departmentName, oldStudentFullName);
        Student foundStudent = entry.getValue();

        if (newCourse != Integer.MIN_VALUE) {
            foundStudent.setCourse(newCourse);
        }
        if (newGroup != Integer.MIN_VALUE) {
            foundStudent.setGroup(newGroup);
        }
        if (newFullName != null) {
            foundStudent.setFullName(newFullName);
        }
    }

    /**
     * Case #3: add a teacher to the department of the faculty of the university
     * */
    public void addTeacherToFacultyDepartment(
            String facultyName, String departmentName,
            int teacherCourse, int teacherGroup, String teacherFullName
    ) throws NotFoundException, AlreadyExistsException {
        if (teacherCourse < 1 || teacherCourse > 4 || teacherGroup < 1) {
            throw new IllegalArgumentException();
        }
        Faculty foundFaculty = getFaculty(facultyName);
        if (foundFaculty == null) {
            throw new NotFoundException();
        }
        Department foundDepartment = foundFaculty.findDepartment(departmentName);
        if (foundDepartment == null) {
            throw new NotFoundException();
        }

        if (foundDepartment.findTeacherByFullName(teacherFullName) != null) {
            throw new AlreadyExistsException();
        }

        foundDepartment.addTeacher(teacherCourse, teacherGroup, teacherFullName);
    }

    /**
     * Case #3: remove a teacher from the department of the faculty of the university
     * */
    public void removeTeacherFromFacultyDepartment(
            String facultyName, String departmentName,
            String teacherFullName
    ) throws NotFoundException {
        Map.Entry<Department, Teacher> entry = findTeacherWithDepartmentAmongAll(facultyName, departmentName, teacherFullName);
        Department foundDepartment = entry.getKey();
        Teacher foundTeacher = entry.getValue();
        foundDepartment.removeTeacher(foundTeacher);
    }

    /**
     * Case #3: update a teacher in the department of the faculty of the university
     * */
    public void updateTeacherInFacultyDepartment(
            String facultyName, String departmentName,
            String oldTeacherFullName,
            int newCourse, int newGroup, String newFullName
    ) throws NotFoundException, IllegalArgumentException {
        if ((newCourse < 1 || newCourse > 4) && newCourse != Integer.MIN_VALUE) {
            throw new IllegalArgumentException();
        }
        if (newGroup < 1 && newGroup != Integer.MIN_VALUE) {
            throw new IllegalArgumentException();
        }

        Map.Entry<Department, Teacher> entry = findTeacherWithDepartmentAmongAll(
                facultyName, departmentName, oldTeacherFullName
        );
        Teacher foundTeacher = entry.getValue();

        if (newCourse != Integer.MIN_VALUE) {
            foundTeacher.setCourse(newCourse);
        }
        if (newGroup != Integer.MIN_VALUE) {
            foundTeacher.setGroup(newGroup);
        }
        if (newFullName != null) {
            foundTeacher.setFullName(newFullName);
        }
    }

    /**
     * Case #4: find a student by full name in the whole university
     * */
    public Student findStudentByFullNameAmongAll(String fullName) throws NotFoundException {
        for (Faculty faculty : faculties) {
            for (Department department : faculty.getDepartments()) {
                Student foundStudent = department.findStudentByFullName(fullName);
                if (foundStudent != null) {
                    return foundStudent;
                }
            }
        }
        throw new NotFoundException();
    }

    /**
     * Case #4: find a teacher by full name in the whole university
     * */
    public Teacher findTeacherByFullNameAmongAll(String fullName) throws NotFoundException {
        for (Faculty faculty : faculties) {
            for (Department department : faculty.getDepartments()) {
                Teacher foundTeacher = department.findTeacherByFullName(fullName);
                if (foundTeacher != null) {
                    return foundTeacher;
                }
            }
        }
        throw new NotFoundException();
    }

    /**
     * Case #5: get all students ordered by course
     * */
    public ArrayList<Student> getAllStudentsOrderedByCourse() {
        ArrayList<Student> allStudents = new ArrayList<>();

        for (Faculty faculty : faculties) {
            for (Department department : faculty.getDepartments()) {
                allStudents.addAll(department.getStudents());
            }
        }

        allStudents.sort(Comparator.comparingInt(Student::getCourse));
        return allStudents;
    }

    /**
     * Case #6: get all faculty students ordered by full name
     * */
    public ArrayList<Student> getAllFacultyStudentsOrderedByFullName(String facultyName) throws NotFoundException {
        Faculty foundFaculty = getFaculty(facultyName);
        if (foundFaculty == null) {
            throw new NotFoundException();
        }

        return foundFaculty.getStudentsOrderedByFullName();
    }

    /**
     * Case #6: get all faculty teachers ordered by full name
     * */
    public ArrayList<Teacher> getAllFacultyTeachersOrderedByFullName(String facultyName) throws NotFoundException {
        Faculty foundFaculty = getFaculty(facultyName);
        if (foundFaculty == null) {
            throw new NotFoundException();
        }

        return foundFaculty.getTeachersOrderedByFullName();
    }

    /**
     * Case #7: get all department students ordered by course
     * */
    public ArrayList<Student> getAllDepartmentStudentsOrderedByCourse(
        String facultyName, String departmentName
    ) throws NotFoundException {
        Faculty foundFaculty = getFaculty(facultyName);
        if (foundFaculty == null) {
            throw new NotFoundException();
        }
        Department foundDepartment = foundFaculty.findDepartment(departmentName);
        if (foundDepartment == null) {
            throw new NotFoundException();
        }

        return foundDepartment.getStudentsOrderedByCourse();
    }

    /**
     * Case #8: get all department students ordered by full name
     * */
    public ArrayList<Student> getAllDepartmentStudentsOrderedByFullName(
        String facultyName, String departmentName
    ) throws NotFoundException {
        Faculty foundFaculty = getFaculty(facultyName);
        if (foundFaculty == null) {
            throw new NotFoundException();
        }
        Department foundDepartment = foundFaculty.findDepartment(departmentName);
        if (foundDepartment == null) {
            throw new NotFoundException();
        }

        return foundDepartment.getStudentsOrderedByFullName();
    }

    /**
     * Case #8: get all department teachers ordered by full name
     * */
    public ArrayList<Teacher> getAllDepartmentTeachersOrderedByFullName(
            String facultyName, String departmentName
    ) throws NotFoundException {
        Faculty foundFaculty = getFaculty(facultyName);
        if (foundFaculty == null) {
            throw new NotFoundException();
        }
        Department foundDepartment = foundFaculty.findDepartment(departmentName);
        if (foundDepartment == null) {
            throw new NotFoundException();
        }

        return foundDepartment.getTeachersOrderedByFullName();
    }

    /**
     * Case #9: get all department students of a specific course
     * */
    public ArrayList<Student> getAllDepartmentStudentsOfCourse(
        String facultyName, String departmentName, int course
    ) throws NotFoundException {
        Faculty foundFaculty = getFaculty(facultyName);
        if (foundFaculty == null) {
            throw new NotFoundException();
        }
        Department foundDepartment = foundFaculty.findDepartment(departmentName);
        if (foundDepartment == null) {
            throw new NotFoundException();
        }

        return foundDepartment.getStudentsOfCourse(course);
    }

    /**
     * Case #10: get all department students of a specific course ordered by full name
     * */
    public ArrayList<Student> getAllDepartmentStudentsOfCourseOrderedByFullName(
            String facultyName, String departmentName, int course
    ) throws NotFoundException {
        Faculty foundFaculty = getFaculty(facultyName);
        if (foundFaculty == null) {
            throw new NotFoundException();
        }
        Department foundDepartment = foundFaculty.findDepartment(departmentName);
        if (foundDepartment == null) {
            throw new NotFoundException();
        }

        return foundDepartment.getStudentsOfCourseOrderedByFullName(course);
    }
}
