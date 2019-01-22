#An integer is a whole number
integrNumber = 3
print (type(integrNumber))

#A decimal value is basically of float data type
floatNumber = 3.14
print (type(floatNumber))

#Basic arithmetic Operations
number1 = 10
number2 = 6

#Addition
number3 = number2 + number1

#Subtraction 
number3 = number1 - number2

#Multiplication
number3 = number1 * number2

#Division
number3 = number1 / number2

#Floor Division
number3 = number1 // number2   #gives result in whole numbers

#Multiplication
number3 = number1 + number2

#modulus
number3 = number1 % number2    #gives the reminder. Modulus operator can be used to check if number is even or odd if we divide the number by 2

#built-in functions
print (round(7.23,1))   # the second argument tells upto how many numbers you want to round up the figure.
print (abs(-3))  #returns value without -ve sign
#other operators
# == , != , >, <, >=, <= 

#Strings can be casted into integeres. Otherwise you may not get the required results by applying the reuiqred operations.
number1 = '10'
number2 = '6'

#Without Casting
print (number2 + number1)

#After Casting
print (int(number1) + int(number2))
