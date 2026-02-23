# This module contains functions to lazily generate student data.

#def student_generator(student_list, major):
   # """
   # Generate student records filtered by major lazily for memory efficiency
    #using a Python generator.
    #"""
    #pass


def student_generator(student_list, major):
    # We want student filtered by major instead of a list of students
    student_gen = (student for student in student_list 
                   if student[2].lower() == major.lower())
    
    return student_gen
