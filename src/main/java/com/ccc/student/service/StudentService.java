package com.ccc.student.service;

import com.ccc.student.model.Student;

import java.util.List;

public interface StudentService {
    List<Student> getAllStudents();

    Student getStudentById(Long id);

    void createStudent(Student student);

    void updateStudent(Student updatedStudent);

    void deleteStudent(Long id);
}
