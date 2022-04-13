#Rowan Patton
#July 17, 2021
#calculator.py

#Ask the user what operation they'd like to perform. Store input.
user_operation =  input("Please select one option: add/subtract/multiply/divide: ")
#As long as the user does not put in a valid operation (not case senstive), continue to ask the user for a valid operation
while user_operation.lower() not in("add", "subtract", "multiply", "divide"):
    user_operation =  input("That's not a valid response. Please select one option: add/subtract/multiply/divide: ")
#once the user puts in a valid operation, tell them which operation they chose
else: print ("You chose " + user_operation.lower() + ".")

#ask for the 2 numbers to calculate and store the user's answers
first_number = float(input("What is the first number? "))
second_number = float(input("What is the second number? "))

#based on the user's chosen operation, compute the response and print the equation
if user_operation.lower() == ("add"):
                              answer = (first_number) + (second_number)
                              print (str(first_number) + " + " + str(second_number) + " = " + str(answer))

elif user_operation.lower() == ("subtract"):
                              answer = (first_number) - (second_number)
                              print (str(first_number) + " - " + str(second_number) + " = " + str(answer))

elif user_operation.lower() == ("multiply"):
                              answer = (first_number) * (second_number)
                              print (str(first_number) + " x " + str(second_number) + " = " + str(answer))

elif user_operation.lower() == ("divide"):
                              answer = (first_number) / (second_number)
                              print (str(first_number) + " / " + str(second_number) + " = " + str(answer))



                              
