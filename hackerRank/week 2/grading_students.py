def grading_students(grades):
    result  = []
    for grade in grades:
        if grade <38:
                result.append(grade)
        else:
             if grade%5==0:
                  
                  roundof_grade = grade
                  if roundof_grade - grade<3:
                       result.append(roundof_grade)
                  else:
                       result.append(grade)
                  
             else:
                  roundof_grade = (grade+5)-(grade%5)
                  if roundof_grade-grade < 3:
                       result.append(roundof_grade)
                  else:
                       result.append(grade)
    return result
grades = [84,29,57]
print(grading_students(grades))
