# Author: Augustus Perseghin agp5191@psu.edu
# Hwk1
# This program will calculate a student's GPA from 3 classes

def result2GP(letterGrade):
  GP = 0
  if letterGrade[0] == 'A':
    GP += 4
  elif letterGrade[0] == 'B':
    GP += 3
  elif letterGrade[0] == 'C':
    GP += 2
  elif letterGrade[0] == 'D':
    GP += 1
  if letterGrade[1] == '+':
    GP += 0.33
  elif letterGrade[1] == '-':
    GP -= 0.33
  return GP

i = 0
scores = [0, 0, 0]
weights = [0, 0, 0]
totalGP = 0
totalWeight = 0

while i != 3:
  scores[i] = int(result2GP(input(f"Enter your course {i + 1} letter grade: ") + " "))
  weights[i] = int(input(f"Enter your course {i + 1} credit: "))
  print(f"Grade point for course {i+1} is: {scores[i]}")
  totalGP += scores[i]*weights[i]
  totalWeight += weights[i]
  i += 1

print(f"Your GPA is: {totalGP/totalWeight}")






