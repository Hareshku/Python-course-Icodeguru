import json
import os
from student import Student


class StudentManager:
    def __init__(self, file_name='students.json'):
        self.students = []
        self.file_name = file_name
        self.load_from_file()
    
    def id_exists(self, student_id):
        return any(s.id == student_id for s in self.students)
    
    def add_student(self, student_id, name, age, marks):
        if self.id_exists(student_id):
            raise ValueError("Student ID already exists")
        if age <= 0:
            raise ValueError("Age must be positive")
        if not name.strip():
            raise ValueError("Name cannot be empty")
        for mark in marks:
            if not (0 <= mark <= 100):
                raise ValueError("Marks must be between 0 and 100")
        
        student = Student(student_id, name, age, marks)
        self.students.append(student)
        self.save_to_file()
        return student
    
    def view_students(self):
        return self.students
    
    def search_student(self, student_id):
        for student in self.students:
            if student.id == student_id:
                return student
        return None
    
    def update_student(self, student_id, name=None, age=None, marks=None):
        student = self.search_student(student_id)
        if not student:
            raise ValueError("Student not found")
        
        if age and age <= 0:
            raise ValueError("Age must be positive")
        if marks:
            for mark in marks:
                if not (0 <= mark <= 100):
                    raise ValueError("Marks must be between 0 and 100")
        
        student.update_details(name, age, marks)
        self.save_to_file()
        return student
    
    def delete_student(self, student_id):
        student = self.search_student(student_id)
        if not student:
            raise ValueError("Student not found")
        self.students.remove(student)
        self.save_to_file()
    
    def save_to_file(self):
        data = [s.to_dict() for s in self.students]
        with open(self.file_name, 'w') as f:
            json.dump(data, f, indent=4)
    
    def load_from_file(self):
        if os.path.exists(self.file_name):
            try:
                with open(self.file_name, 'r') as f:
                    data = json.load(f)
                    self.students = [Student.from_dict(s) for s in data]
            except json.JSONDecodeError:
                self.students = []
        else:
            self.students = []
