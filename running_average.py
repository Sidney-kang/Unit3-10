# Created by : Sidney Kang
# Created on : 23 Oct. 2017
# Created for : ICS3UR
# Daily Assignment - Unit3-09
# This program displays the "running average"

#variables
number_times_inputed = 0.0
running_average = 0.0
sum_of_marks = 0.0
user_input = 0.0

#process
print("Enter any number from 0-100.")
print("Type '-1' to get your final average")

while user_input != -1.0:  
     if user_input < -1.0 or user_input > 100: 
        print ("Please enter a positive number between 0-100")    
        number_times_inputed = number_times_inputed -1.0  
        sum_of_marks = sum_of_marks - user_input
        user_input = raw_input("Mark entered: ")
        user_input = float(user_input)
        number_times_inputed = number_times_inputed + 1.0                    
        sum_of_marks = sum_of_marks + user_input 
        running_average = sum_of_marks/number_times_inputed
     else:
        user_input = raw_input("Mark entered: ")
        user_input = float(user_input)
        number_times_inputed = number_times_inputed + 1.0                    
        sum_of_marks = sum_of_marks + user_input 
        running_average = sum_of_marks/number_times_inputed
      	
#output
if user_input == -1.0:
   number_times_inputed = number_times_inputed - 1.0
   sum_of_marks = sum_of_marks - user_input
   running_average = sum_of_marks/number_times_inputed                  
   print ("Average is: " + str(running_average))     
