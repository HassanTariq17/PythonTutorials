# this is will give an error because python interprets the 2nd ' as the ending quote.
#message = 'Hassan's string'

#There  are 2 ways to handle this
message = 'Hassan\'s string'     #Here backlash will not be included as string index
print (message)

#and the other way is 
message = "Hassan's string"
print (message)

#multi line textual data in python
message = """I am starting my python tutorial.
			This is multi line textual data."""
print (message)

#len to find the number of characters in string
print (len(message))

#Access index wise string
#indexing starts from 0 and goes untill the length of string-1
print (message[0])
print (message[6])

#slicing in strings
print (message[0:5])   #this will give all string indexes from 0 to 4 excluding 5
print (message[:5])    #this will give all string indexes upto index 4
print (message[5:])	   #this will give all string indexes from index 5 till end
print (message[-1])	   #this will give last index of string
print (message[-3:])   #this will give all string indexes from 3rd last index to last index.
print (message[:-3])   #this will give all string indexes excluding last 3


#to lower case
print (message.lower())

#to upper case
print(message.upper())

#count an alphabet in string
print (message.count('s'))

#To find the starting index of a word. or and alphabet
print (message.find('s'))
print (message.find('starting'))

#This will give -1 beaucse tye word is not found,
print (message.find('justice'))

#To replace a word in our string
message = message.replace('data','string')
print (message)

#concatenate stings
name = "Hassan"
greeting = "Welcome"


#Method 1
message = greeting + name
print (message)

#Method 2
#using an additional string in between
message = greeting + ", " + name
print (message)

#Method 3
#Using the plcaeholder for each function
message = '{}, {}'.format(greeting,name) 
print (message)

#New things in python >= 3.x
#the fstrings
message = f'{greeting} , {name}!'
print (message)

#Get all related functions of a particular object
print (dir(message))
