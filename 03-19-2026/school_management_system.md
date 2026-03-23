# School Management System — Markdown Sheet

## Overview
This app is a simple **school management system** built in Python.  
It manages:

- **Students**
- **Classes**
- **Grades**
- **Enrollments**
- **A menu-driven terminal interface**

The sample data is based on **Hogwarts**.

---

## Helper Functions

### `print_divider(symbol="=", count=80)`
Prints a horizontal divider line.

### `print_center(text: str, char_count=80)`
Centers text in the console.

### `print_left(text: str)`
Prints text with indentation.

### `generate_id(base_number, list)`
Creates a new ID based on the base number and the length of a list.

### `wait_for_user(text="Press enter to continue...\n")`
Pauses the program until the user presses Enter.

### `print_title(text)`
Prints a formatted title using dividers and centered text.

---

## Class 1: `Student`

Represents a student in the school system.

### Attributes
- `student_id` — student ID number
- `name` — student name
- `grade_level` — grade level from 9 to 12

### Methods
- `__init__(student_id, name, grade_level)`
- `display_info()`  
  Prints student information.
- `__str__()`  
  Returns a readable string representation.

### Example
```python
student = Student(1001, "Harry Potter", 10)
print(student)
```

---

## Class 2: `Class`

Represents a school class or course.

### Attributes
- `class_id` — class ID
- `class_name` — name of the class
- `teacher` — teacher name
- `enrolled_students` — list of enrolled `Student` objects

### Methods
- `__init__(class_id, class_name, teacher)`
- `add_student(student: Student)`  
  Adds a student if they are not already enrolled.
- `remove_student(student_id: int)`  
  Removes a student by ID.
- `list_students()`  
  Displays all enrolled students.
- `__str__()`  
  Returns a readable string representation.

### Example
```python
classroom = Class(2001, "Defense Against the Dark Arts", "Severus Snape")
```

---

## Class 3: `Grade`

Represents a grade for a student in a class.

### Attributes
- `grade_id` — grade ID
- `student` — `Student` object
- `class_obj` — `Class` object
- `score` — numeric score

### Methods
- `__init__(grade_id, student, class_obj, score)`
- `get_letter_grade()`  
  Converts numeric score to a letter grade:
  - `90-100` → `A`
  - `80-89` → `B`
  - `70-79` → `C`
  - `60-69` → `D`
  - `< 60` → `F`
- `display_grade()`  
  Prints grade details.
- `__str__()`  
  Returns a readable string representation.

### Example
```python
grade = Grade(3001, student, classroom, 95)
print(grade.get_letter_grade())
```

---

## Class 4: `School`

Main management class for the whole system.

### Attributes
- `school_name`
- `students_list`
- `classes_list`
- `grades_list`

---

## School Methods

### Student Management

#### `add_student(student_id, name, grade_level)`
Adds a new student if the ID does not already exist.

#### `find_student(student_id)`
Searches for a student by ID.

#### `list_all_students()`
Displays all registered students.

---

### Class Management

#### `add_class(class_id, class_name, teacher)`
Adds a new class if the ID does not already exist.

#### `find_class(class_id)`
Searches for a class by ID.

#### `list_all_classes()`
Displays all registered classes.

---

### Enrollment Management

#### `enroll_student_in_class(student_id, class_id)`
Enrolls a student into a class.

Process:
1. Find the student
2. Find the class
3. Use the class’s `add_student()` method
4. Return `True` if successful

---

### Grade Management

#### `add_grade(grade_id, student_id, class_id, score)`
Adds a grade for a student in a class.

Checks:
- Student exists
- Class exists
- Grade ID is unique

#### `list_grades_for_student(student_id)`
Shows all grades for one student.

#### `list_grades_for_class(class_id)`
Shows all grades for one class.

#### `calculate_student_average(student_id)`
Calculates the average score for a student.

---

## Main Program Flow

The `main()` function does the following:

1. Creates a `School` object named **Hogwarts**
2. Adds sample students
3. Adds sample classes
4. Enrolls students in classes
5. Adds sample grades
6. Opens an interactive menu

---

## Sample Data

### Students
| ID | Name | Grade |
|---|---|---|
| 1001 | Harry Potter | 10 |
| 1002 | Hermione Granger | 10 |
| 1003 | Ron Weasly | 10 |
| 1004 | Neville Longbottom | 10 |
| 1005 | Ginny Weasley | 9 |
| 1006 | Draco Malfoy | 11 |
| 1007 | Dean Thomas | 12 |
| 1008 | George Weasly | 12 |

### Classes
| ID | Class Name | Teacher |
|---|---|---|
| 2001 | Defense Against the Dark Arts | Severus Snape |
| 2002 | Astronomy | Aurora Sinistra |

### Grades
| Grade ID | Student | Class | Score |
|---|---|---|---|
| 3001 | Harry Potter | Defense Against the Dark Arts | 89 |
| 3002 | Harry Potter | Astronomy | 99 |
| 3003 | Hermione Granger | Defense Against the Dark Arts | 100 |
| 3004 | Ron Weasly | Defense Against the Dark Arts | 78 |

---

## Menu Options

| Option | Action |
|---|---|
| 1 | List all students |
| 2 | List all classes |
| 3 | Add a new student |
| 4 | Add a new class |
| 5 | Enroll student in class |
| 6 | Add a grade |
| 7 | View student grades |
| 8 | View class grades |
| 9 | Calculate student average |
| exit | Quit the program |

---

## Important Logic Rules

- Student grades must be between **9 and 12**
- A student can only be added once by ID
- A class can only be added once by ID
- A student must exist before enrollment
- A class must exist before enrollment
- A grade should only be added for valid student/class pairs
- Duplicate grade IDs are not allowed

---

## Letter Grade Scale

| Score Range | Letter |
|---|---|
| 90–100 | A |
| 80–89 | B |
| 70–79 | C |
| 60–69 | D |
| Below 60 | F |

---

## Notes on the Code

- The app uses **object-oriented programming**
- Data is stored in **lists** during runtime
- The menu system uses a `while True` loop
- The program is terminal-based and interactive

---

## Possible Improvements

- Add file saving/loading
- Add teacher management
- Add class averages
- Add search by student name
- Add attendance tracking
- Add GPA calculation
- Add report card generation

---

## Example Output Style

```text
================================================================================
                              WELCOME TO THE SCHOOL MANAGEMENT SYSTEM
================================================================================
```

```text
1. List all students
2. List all classes
3. Add a new student
4. Add a new class
5. Enroll student in class
6. Add a grade
7. View student grades
8. View class grades
9. Calculate student average
```