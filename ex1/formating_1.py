# Example for formating

#number_one = input("Enter first number: ")
#number_two = input("Enter second number: ")
#number_three = input("Enter third number: ")

#WE CAN USE IN ONE LINE

number_one, number_two, number_three = input("Please enter three numbers separated by comma ").split(",")


average = (int(number_one)+int(number_two)+int(number_three))/3
print(average)
