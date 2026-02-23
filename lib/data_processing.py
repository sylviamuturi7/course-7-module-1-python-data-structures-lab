# This module contains functions to process student data.

#def format_student_data(student):
    #"""
    #Format student data for display.
    #The function should return a formatted string containing:
    #- Student ID
    #- Student Name
    #- Major
    #such as: "ID: 10 | Name: Louis Medina | Major: Computer Science"
    #"""
    #pass

#def display_students(student_list):
    #"""
    #Display all student records.
    #Loop through the student_list and print each student using format_student_data().
    #"""
    #pass

# Functions to process student data.
def format_student_data(student):
    # Args: student (tuple containing ID, Name, Major)
    # Returns: formatted string like "ID: 101 | Name: Alice Johnson | Major: Computer Science"
    
    student_id = student[0]
    student_name = student[1]
    student_major = student[2]
    
    formatted_string = f"ID: {student_id} | Name: {student_name} | Major: {student_major}"
    
    return formatted_string

def display_students(student_list):
    # Args: student_list (list of student tuples to display)
    # Returns: None (prints each student to console)
    
    for student in student_list:
        print(format_student_data(student))