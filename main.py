# Author: Augustus Perseghin agp5191@psu.edu
# Hwk1
# This program will calculate a student's GPA from 3 classes

def result2GP(letterGrade):
  GP = 0.0
  if letterGrade == 'A':
    GP = 4.0
  elif letterGrade == 'A-':
    GP = 3.67
  elif letterGrade == 'B+':
    GP = 3.33
  elif letterGrade == 'B':
    GP = 3.0
  elif letterGrade == 'C+':
    GP = 2.67
  elif letterGrade == 'C':
    GP = 2.0
  elif letterGrade == 'D':
    GP = 1.0
  return GP

i = 0
scores = [0, 0, 0]
weights = [0, 0, 0]
totalGP = 0
totalWeight = 0

while i != 3:
  scores[i] = float(result2GP(input(f"Enter your course {i + 1} letter grade: ")))
  weights[i] = float(input(f"Enter your course {i + 1} credit: "))
  print(f"Grade point for course {i+1} is: {scores[i]}")
  totalGP += scores[i]*weights[i]
  totalWeight += weights[i]
  i += 1

print(f"Your GPA is: {totalGP/totalWeight}")






