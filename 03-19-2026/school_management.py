"""
SCHOOL MANAGEMENT SYSTEM - STUDENT TEMPLATE
===========================================
Instructions: Fill in the missing code in the methods marked with TODO.
Follow the comments to complete each class.
"""

# ============================================
# STEP 1: STUDENT CLASS
# ============================================
import random

class Student:
    """
    A class representing a student
    
    Attributes:
        student_id (int): 4 digit student ID starting with 1
        name (str): student name
        grade_level (number): student grade level (9-12)
    """
    
    def __init__(self, student_id, name, grade_level):
        """Initialize Student with student_id (4 digits), name, grade_level"""
        self.student_id = student_id
        self.name = name
        self.grade_level = grade_level
    
    def display_info(self):
        """Print student id, name and grade"""
        print(f"ID: {self.student_id} | Name: {self.name} | Grade: {self.grade_level}")
    
    def __str__(self):
        """Return a string representation of the student"""
        return f"Student(ID: {self.student_id}, Name: {self.name}, Grade: {self.grade_level})"


# ============================================
# STEP 2: CLASS CLASS (School Course)
# ============================================

class Class:
    """
    A class representing a Class
    
    Attributes:
        class_id (int): Classroom ID in integers
        class_name (str): name of the class
        teacher (str): name of the teacher in charge
    """
    
    def __init__(self, class_id, class_name, teacher):
        """Initialize Class with class_id, class_name, and teacher"""
        self.class_id = class_id
        self.class_name = class_name
        self.teacher = teacher
        self.enrolled_students = []
    
    def add_student(self, student: Student):
        """Add student to Class object's enrolled students list if
        it's an instance of Student Class
        """
        if not isinstance(student, Student):
            raise TypeError("You can only add Student objects to class")
        self.enrolled_students.append(student)
        print(f"Added: {student}")

    
    def remove_student(self, student_id: int):
        """
        Remove a student from class
        """
        if not student_id in [student.student_id for student in self.enrolled_students]:
            print(f"Could not found student with ID: {student_id}")
        else:
            for student in self.enrolled_students:
                if student_id == student.student_id:
                    print("Student Found:")
                    self.enrolled_students.remove(student)
                    print(f"Student removed (ID: {student.student_id} Name: {student.name})")
                    
    def list_students(self):
        if len(self.enrolled_students) == 0:
            print("There are no students in this class")
        else:
            for index, student in enumerate(self.enrolled_students):
                print(f"{index + 1}. {student}")
    
    def __str__(self):
        # TODO: Return string representation of the class
        # Include class ID, name, teacher, and number of students
        # YOUR CODE HERE
        return f"Class()"


# ============================================
# STEP 3: GRADE CLASS
# ============================================

class Grade:
    """
    TODO: Create a class to represent a student's grade in a class.
    
    Instructions:
    1. Initialize with grade_id, student, class_obj, score
    2. Create a method to convert numerical score to letter grade
    3. Create a method to display grade information
    """
    
    def __init__(self, grade_id, student: Student, class_obj: Class, score: int):
        self.grade_id = grade_id
        self.student = student
        self.class_obj = class_obj
        self.score = score
    
    def get_letter_grade(self):
        """
        Convert numerical score to letter grade.
        Use this scale:
        90-100: A
        80-89: B
        70-79: C
        60-69: D
        Below 60: F
        """
        if self.score >= 90:
            return "A"
        elif self.score >= 80:
            return "B"
        elif self.score >= 70:
            return "C"
        elif self.score >= 60:
            return "D"
        else:
            return "F"
    
    def display_grade(self):
        # TODO: Print grade information including letter grade
        # Example: "Grade ID: 301 | Student: Alice | Class: Math | Score: 95 | Letter: A"
        # YOUR CODE HERE
        print(f"Grade ID: {self.grade_id} | Student: {self.student.name} | "
              f"Class: {self.class_obj.class_name} | Score: {self.score} | "
              f"Letter: {self.get_letter_grade()}")
    
    def __str__(self):
        # TODO: Return string representation of the grade
        # Include letter grade in the string
        # YOUR CODE HERE
        return (f"Grade(ID: {self.grade_id}; Student: {self.student.name}; "
                f"Class: {self.class_obj.class_name}, Score: {self.score}; "
                f"Letter: {self.get_letter_grade()})")


# ============================================
# STEP 4: SCHOOL MANAGEMENT SYSTEM
# ============================================

class School:
    """
    TODO: Create the main school management class.
    
    This class will manage all students, classes, and grades.
    """
    
    def __init__(self, school_name):
        # TODO: Initialize school name and empty lists for students, classes, and grades
        # YOUR CODE HERE
        self.school_name  = school_name
        self.students_list = []
        self.classes_list = []
        self.grades_list = []
    
    # ---------- STUDENT MANAGEMENT ----------
    
    def add_student(self, student_id: int, name: str, grade_level: int):
        # TODO: Create a new Student object and add to students list
        # Check if student_id already exists
        # Return the new student or None if failed
        # YOUR CODE HERE
        if student_id in [student.student_id for student in self.students_list]:
            print(f"{name} is already enrolled (ID: {student_id}). Try another student.")
            return None
        else:
            student = Student(student_id, name, grade_level)
            self.students_list.append(student)
            return student
    
    def find_student(self, student_id):
        for student in self.students_list:
            if student_id == student.student_id:
                return student
        print(f"Student ID {student_id} not found")
        return None
    
    def list_all_students(self):
        if not self.students_list:
            print(f"There are no students in enrolled in {self.school_name}")
        else:
            print("=" * 50)
            print(f"Students at {self.school_name}")
            print("=" * 50)
            for index, student in enumerate(self.students_list):
                print(f"{index + 1}) {student}")
    
    # ---------- CLASS MANAGEMENT ----------
    
    def add_class(self, class_id, class_name, teacher):
        # TODO: Create a new Class object and add to classes list
        # Check if class_id already exists
        # Return the new class or None if failed
        # YOUR CODE HERE
        pass
    
    def find_class(self, class_id):
        # TODO: Find and return a class by ID
        # Return None if not found
        # YOUR CODE HERE
        pass
    
    def list_all_classes(self):
        # TODO: Display all classes in the school
        # Include number of students enrolled in each class
        # YOUR CODE HERE
        pass
    
    # ---------- ENROLLMENT MANAGEMENT ----------
    
    def enroll_student_in_class(self, student_id, class_id):
        # TODO: Enroll a student in a class
        # Find both student and class first
        # Use the class's add_student method
        # Return True if successful, False otherwise
        # YOUR CODE HERE
        pass
    
    # ---------- GRADE MANAGEMENT ----------
    
    def add_grade(self, grade_id, student_id, class_id, score):
        # TODO: Add a grade for a student in a class
        # Verify student and class exist
        # Verify student is enrolled in the class
        # Check if grade_id already exists
        # Create and add new Grade object
        # YOUR CODE HERE
        pass
    
    def list_grades_for_student(self, student_id):
        # TODO: Display all grades for a specific student
        # YOUR CODE HERE
        pass
    
    def list_grades_for_class(self, class_id):
        # TODO: Display all grades for a specific class
        # YOUR CODE HERE
        pass
    
    def calculate_student_average(self, student_id):
        # TODO: Calculate and display average grade for a student
        # Return the average or None if no grades
        # YOUR CODE HERE
        pass


# ============================================
# STEP 5: MAIN PROGRAM WITH SAMPLE DATA
# ============================================

def main():
    """
    TODO: Create the main program with sample data and menu system.
    
    Instructions:
    1. Create a School object
    2. Add sample data (students, classes, enrollments, grades)
    3. Create an interactive menu system
    """
    
    # print("=" * 60)
    # print("🏫 WELCOME TO THE SCHOOL MANAGEMENT SYSTEM 🏫")
    # print("=" * 60)
    
    hogwarts = School('Hogwarts')
    
    hogwarts.add_student(1001, 'Harry Potter', 9)
    hogwarts.add_student(1002, 'Hermione Granger', 9)
    hogwarts.add_student(1003, 'Ron Weasly', 9)
    
    print(hogwarts.find_student(1001))
    print(hogwarts.find_student(1002))
    
    hogwarts.list_all_students()
    
    # TODO: Create your school
    # school = School("Your School Name")
    
    # TODO: Add sample students
    # Use the data from the tutorial or create your own
    
    # TODO: Add sample classes
    
    # TODO: Enroll students in classes
    
    # TODO: Add sample grades
    
    # TODO: Create the interactive menu system
    # Include options to:
    # - List all students
    # - List all classes
    # - Add a new student
    # - Add a new class
    # - Enroll student in class
    # - Add a grade
    # - View student grades
    # - View class grades
    # - Calculate student average
    # - Exit
    
    # HINT: Use a while loop and if/elif statements for the menu
    
    # YOUR CODE HERE
    pass


# ============================================
# RUN THE PROGRAM
# ============================================

if __name__ == "__main__":
    main()


# ============================================
# BONUS CHALLENGES (Optional)
# ============================================

"""
Once you complete the basic system, try these challenges:

1. Add a Teacher class with attributes (teacher_id, name, subjects)
2. Add a method to calculate class average
3. Add search functionality (find students by name)
4. Add data persistence (save to and load from a file)
5. Add a report card generator
6. Add GPA calculation (4.0 scale)
7. Add attendance tracking
8. Add student schedules/timetables
"""

# ============================================
# ANSWER KEY (For teachers)
# ============================================

"""
The complete solution is available in the tutorial document.
Students should refer to the tutorial for guidance but try to
write the code themselves first.
"""
