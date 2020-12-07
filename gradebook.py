# gradebook.py
#HALEY WILLIAMS NOV 12.20
# Display the average of each student's grade.
# Display tthe average for each assignment.

gradebook = [[61, 74, 69, 62, 72, 66, 73, 65, 60, 63, 69, 63, 62, 61, 64],
             [73, 80, 78, 76, 76, 79, 75, 73, 76, 74, 77, 79, 76, 78, 72],
             [90, 92, 93, 92, 88, 93, 90, 95, 100, 99, 100, 91, 95, 99, 96],
             [96, 89, 94, 88, 100, 96, 93, 92, 94, 98, 90, 90, 92, 91, 94],
             [76, 76, 82, 78, 82, 76, 84, 82, 80, 82, 76, 86, 82, 84, 78],
             [93, 92, 89, 84, 91, 86, 84, 90, 95, 86, 88, 95, 88, 84, 89],
             [63, 66, 55, 67, 66, 68, 66, 56, 55, 62, 59, 67, 60, 70, 67],
             [86, 92, 93, 88, 90, 90, 91, 94, 90, 86, 93, 89, 94, 94, 92],
             [89, 80, 81, 89, 86, 86, 85, 80, 79, 90, 83, 85, 90, 79, 80],
             [99, 73, 86, 77, 87, 99, 71, 96, 81, 83, 71, 75, 91, 74, 72]]

class GradeBook:
    
    def main_function():
        quiz_scores = []
        assignment_scores = []
        while True:
            try:
                quiz_grade = float(input('Please enter a grade for the quiz, or press Enter to stop adding grades: '))
                quiz_scores.append(quiz_grade)
            except:
                break

        while True:
            try:
                assignment_grade = float(input('Please enter a grade for the assignment, or press Enter to stop adding grades: '))
                assignment_scores.append(assignment_grade)
            except:
                break
    
        print (quiz_scores)
        print (assignment_scores)
        print ('time for totals and averages')
    
        quiz_total = sum(quiz_scores)
        assignment_total = sum(assignment_scores)
        print ('quiz total ' + str(quiz_total))
        print ('assign total ' + str(assignment_total))

        if len(quiz_scores) > 0:
            quizScoreAverage = sum(quiz_scores)// len(quiz_scores) 
        else:
            quizScoreAverage = 0
    
        if len(assignment_scores) > 0:
            assignmentScoreAverage = sum(assignment_scores) // len(assignment_scores)
        else:
            assignmentScoreAverage = 0

        print ('quiz average ' + str(quizScoreAverage))
        print ('assign average ' + str(assignmentScoreAverage))


        
GradeBook.main_function()
