# Author: Augustus Perseghin agp5191@psu.edu
# Date: 9/11/2020
# Hwk1
# This program will calculate a student's GPA from 3 classes

def getGradePoint(letterGrade):
  GP = 0.0
  if letterGrade == 'A':
    GP = 4.0
  elif letterGrade == 'A-':
    GP = 3.67
  elif letterGrade == 'B+':
    GP = 3.33
  elif letterGrade == 'B':
    GP = 3.0
  elif letterGrade == 'B-':
    GP = 2.67
  elif letterGrade == 'C+':
    GP = 2.33
  elif letterGrade == 'C':
    GP = 2.0
  elif letterGrade == 'D':
    GP = 1.0
  return GP

def run():
  i = 0
  scores = [0, 0, 0]
  weights = [0, 0, 0]
  totalGP = 0
  totalWeight = 0

  while i != 3:
    scores[i] = float(getGradePoint(input(f"Enter your course {i + 1} letter grade: ")))
    weights[i] = float(input(f"Enter your course {i + 1} credit: "))
    print(f"Grade point for course {i+1} is: {scores[i]}")
    totalGP += scores[i]*weights[i]
    totalWeight += weights[i]
    i += 1

  print(f"Your GPA is: {totalGP/totalWeight}")

if __name__ == "__main__":
  run()