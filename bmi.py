import sys #coding: utf-8

print("BMI:Body Mass Index Calculator")
userWeight = input("enter your weight in pounds" )
userHeight = input("enter your height in inches" )
userHeightFloat = float(userHeight)

myBMIpy = round((703 *float(userWeight)) / (userHeightFloat * userHeightFloat), 2)

print("Your BMi is " + str(myBMIpy) + "%")
