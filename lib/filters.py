# This module contains functions for filtering student data.

#def filter_students_by_major(student_list, major):
   # """
   # Return a filtered list of students by major using a list comprehension.
    #The function should:
    #- Check if a student's major matches the given major (case insensitive).
   # - Return a new list containing only students that match.
   # """
   # pass

   # Functions for filtering student data.
def filter_students_by_major(student_list, major):
    
    # Filter students by their major using list comprehension
    # Args: student_list (list of tuples), major (string to filter by, case insensitive)
    # Returns: list of student tuples that match the given major
    
    filtered_students = [student for student in student_list 
                        if student[2].lower() == major.lower()]
    
    return filtered_students

