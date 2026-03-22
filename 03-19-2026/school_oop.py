class Student:
    """A class to represent a student.
    
    Attributes:
    
    student_id (int): Unique identifier for each student
    name (str): Student's full name
    grade_level  (int): Student grade level (9-12)
    
    """
    
    def __init__(self, student_id, name, grade_level):
        self.student_id = student_id
        self.name = name
        self.grade_level = grade_level
        
    def display_info(self):
        print(f"ID: {self.student_id} | Name: {self.name} | Grade: {self.grade_level}")
    
    def __str__(self):
        return f"Student(ID: {self.student_id}, Name: {self.name}, Grade: {self.grade_level})"