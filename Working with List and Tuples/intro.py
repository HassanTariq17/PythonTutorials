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
#split values based on a delimeter
print (max(numbers))  #to print maximum number in the list
print (min(numbers))  #To get the minimum number in the list.
print (sum(numbers))  #to get the sum of all indexs in the list

#to find a value in the list
print (courses.index('Math'))

#Join strings in the list given a delimeter
delimeter = '-'
new_string = delimeter.join(courses)
print (new_string)

#Split the string
splitted_string = new_string.split('-')
print (splitted_string)

#find a vlue in list
print ('Math' in courses)


#iterate through items of list
#1. Using simple for loop
for each in courses:
	print (each)

#2. Usning enumerate (start value) enumerate returns 2 values one the index and other the value of index
for index,each in enumerate(courses):   
	print (index,each)

#List vs Tuples
#muteable vs immuteable
#Lists are mutebale. Means you can change values of lists once assigned.
#Lists are immutebale. Means you can not change values of lists once assigned.

#Tuples 
new_tuple = (1,2,3,'Math')
print (new_tuple)

#Sets
new_set = {1,1,2,3,4,5}    #duplicate values are not allowed in sets. sets automatically remove duplicate values.
print (new_set)

#Check similarity using intersection
set1 = {1,2,3,4}
set2 = {3,4,5,6,}
print (set1.intersection(set2))      #this will give all similar items in two sets


#Combine using union
set3 = set1.union(set2)
print (set3)

#creating empty lists, tuples, sets
empty_list = []
empty_tuple = ()
empty_set = set()    #empty_set = {}   will declare a dictionary
#Dictionary vs Sets



