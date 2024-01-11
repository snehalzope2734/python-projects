'''To Calculate the BMI We want the few data from user as its weight in kg and height in meters
BMI stands for Body Mass Index is a measure of body fat on the basis of height and weight '''
import time
print("...........Welcome to BMI Calculator...........")
time.sleep(2)
print("Please Enter Some Information")
name = input("Enter Your Name:")
height = float(input("Enter the Height in cm:"))
weight = float(input("Enter the Weight in kg:"))
BMI = weight/(height/100)**2
print("Your Information")
print(f'Your name is{name},Your Height is {height},Your Weight is {weight} ,Your BMI is {BMI}')
if BMI <=18.5:
    print("Opps!!!You are underweight")
elif BMI<=24.9:
    print("Yayy!!!You are Normal")
elif BMI<=29.9:
        print("Hmmm!!!You are overweight")
else:     print("Opps!!!You are obese")

