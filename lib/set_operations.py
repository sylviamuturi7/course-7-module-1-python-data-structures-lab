# This module contains operations related to sets.

#def unique_majors(student_list):
   # """
   # Return a set of unique student majors using set comprehension.
   # Extract the major field from each student record.
   # """
  #  pass

def unique_majors(student_list):
    # Getting all unique majors from a list of students using set comprehension
    # Sets automatically handle duplicates, so we get only unique values
    unique_major_set = {student[2] for student in student_list}
    
    return unique_major_set

