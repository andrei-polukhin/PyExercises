package entities;

/**
 * Student entity
 * */
public class Student {
    int course;
    int group;
    String fullName;

    public Student(int course, int group, String fullName) {
        this.course = course;
        this.group = group;
        this.fullName = fullName;
    }

    @Override
    public String toString() {
        return "Student{" +
                "course=" + course +
                ", group='" + group + '\'' +
                ", fullName='" + fullName + '\'' +
                '}';
    }

    public int getCourse() {
        return course;
    }

    public String getFullName() {
        return fullName;
    }

    public void setCourse(int course) {
        this.course = course;
    }

    public void setGroup(int group) {
        this.group = group;
    }

    public void setFullName(String fullName) {
        this.fullName = fullName;
    }
}
