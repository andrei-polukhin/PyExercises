package entities;

/**
 * Teacher entity
 * */
public class Teacher {
    int course;
    int group;
    String fullName;

    public Teacher(int course, int group, String fullName) {
        this.course = course;
        this.group = group;
        this.fullName = fullName;
    }

    @Override
    public String toString() {
        return "Teacher{" +
                "course=" + course +
                ", group='" + group + '\'' +
                ", fullName='" + fullName + '\'' +
                '}';
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
