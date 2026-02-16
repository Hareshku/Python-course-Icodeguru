class Student:
    def __init__(self, student_id, name, age, marks):
        self.id = student_id
        self.name = name
        self.age = age
        self.marks = marks
        self.total = self.calculate_total()
        self.percentage = self.calculate_percentage()
        self.grade = self.calculate_grade()
    
    def calculate_total(self):
        return sum(self.marks)
    
    def calculate_percentage(self):
        return (self.total / len(self.marks)) if self.marks else 0
    
    def calculate_grade(self):
        if self.percentage >= 90:
            return 'A+'
        elif self.percentage >= 80:
            return 'A'
        elif self.percentage >= 70:
            return 'B'
        elif self.percentage >= 60:
            return 'C'
        elif self.percentage >= 50:
            return 'D'
        else:
            return 'F'
    
    def update_details(self, name=None, age=None, marks=None):
        if name:
            self.name = name
        if age:
            self.age = age
        if marks:
            self.marks = marks
            self.total = self.calculate_total()
            self.percentage = self.calculate_percentage()
            self.grade = self.calculate_grade()
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'marks': self.marks,
            'total': self.total,
            'percentage': self.percentage,
            'grade': self.grade
        }
    
    @staticmethod
    def from_dict(data):
        student = Student(data['id'], data['name'], data['age'], data['marks'])
        return student
