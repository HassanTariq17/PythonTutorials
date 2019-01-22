courses = ['History','Math','Physics','Chemistry']
print (courses)

#Print length of list
print (len(courses))

#Get any index of a list
print (courses[0])

#Getting index form end
x = 4   #x can be any number upto which index you want to access the list
print (courses[-x])

#Getting idex from anywhere in the string
x = 4     #x can be any number upto which index you ant to access tye list
print (courses[0:x])

#Appendng items to list
courses.append('Biology')   #This will add values at the end
print (courses)

#Inserting items at desired index in the list
courses.insert(0,'Art')   #First argumet is the one at which index you want to aadd items
print (courses)     
#One important thing to remember is that it will not replace items at 0 index 
#but it will shift all other indexes to next position and will add the item to desired location.

#Adding items of two different lists.
courses_1 = ['History','Math','Physics','Chemistry']
courses_2 = ['Art', 'Data Mining']

#Method 1  
courses_1.insert(0,courses_2)     #This will create a list inside a list. .extend will also do the same.
print (courses_1)

#Method 2
courses.extend(courses_2)       #this will add list 2 items individually to list 1 at the end.
print (courses)

#Remove values form lists
courses_1.remove('Math')    #You can remove any item from list using remove
print (courses_1)

value = courses_1.pop()      #This will always remove last index formm the list. Pop also returns the value poped.
print (courses_1)
print (value)

#Reverse our list
courses.reverse()
print (courses)

#Sorting our list
#method 1
print (courses.sort(reverse = True))   #Will sort list alphabetically  and print the list in reverse order

numbers = [3,6,8,2]
print (numbers.sort(reverse = True))   #Sort list and print list in alphabetical order

#Method 2
sortedList = sorted(courses)    #This will return the sorted list
print (sortedList)

#more built inn functions
#min, max, sum,find values in a list , split values based on a delimeter
#join indexs of a list based on a delimiter , find index of a cerain index , find a vlue in list, 
#iterate through items of list
#1. Using simple for loop
#2. Usning enumerate (start value)

#List vs Tuples
#muteable vs immuteable

#Sets
#Duplicate value
#Check similarity using intersection
#Combine using union

#creating empty lists, tuples, sets
#Dictionary vs Sets



