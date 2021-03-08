'''
Text Type (String)
'''

#s = "This is a single line string"
#print(s)
#print(type(s))

#s = """this is a multiline 
#string example"""
#print(s)

#===============

#Find a character by index
#s = 'string example'
#print(s[5])

#slicing

#s = 'string example'
#print(s[2:5])
#Rememeber the count for the left for slicing starts with zero! so the letter 's' in string would be '0' and for the right index starts '1'

#==============
# a string is immutable
#s = 'string example'
#s[2] = 'o'
#print(s)
# cant chang it in this way

'''
Numeric Type (Integer, Float,Complex)
'''
#example of integer
#x = 123456789
#print(type (x))

#example of float - accurate up to 15-16 decimal places
#x= 0.123456787654
#print(type (x))

#example of complex
#x = 1+2j
#print(type (x))

'''
Sequence Type (list, Tuple, Range)
'''

#list       #note: List uses square brackets tuple does not
#x= [10, 2.5, 'hello']
#print (x[0])
#print(x[1:3]) #sliced #so first number is index, count 0-1 and the second number is position which in this case is 3 

#Also a list is mutable which means it can be changed unlike a 'string'
#x[2] = 'python'
#print (x) 

#Tuple #remember commas make it a tuple, without it, it becomes a string!
#tuple = ()
#tuple = ('cat', [4,3,2], [1,2,3])
#tuple = 'hello',
#tuple = ('hello',)
#print(type(tuple))

#===============

#tuple = ('cat', [4,3,2], [1,2,3])
#print(tuple[0])

#================

#A tuple is immutable(cant be changed)

#tuple = ('cat', [4,3,2], [1,2,3])
#tuple[2] = 10
#print(tuple)

#================

#Range
#Remember '0' is a number  so the range of 10 goes up to '9'
#x = range(10)
#for n in x:
#  print(n) 

#================
'''
Mapping Type(Dictionary)
'''
#it is mutable
#dict= {}
#print(type(dict))

#dict = {'name': 'Andrew', 'age':'28'}
#print(dict['age'])
#print(dict['name'])

#dict ['age'] = 29
#print(dict['age'])

'''
Set Types
'''
#emtpty set having set = {} is an empty dict
#set = set ()
#print(type(set))

#================

# mixed data types ( all immutable )
#set = {3.2, 'hi', (1,2,3)}
#print(type(set))
# Type error: 'set' object not suscriptable  
#print(set[0])

#================

# No duplicates, (it just takes it off)

# set = {3.2, 'hi', (1,2,3), 'hi'}
# print(set)

#================
#cannot have mutable (list) in a set
#set = {3.2, 'hi', (1,2,3), [1,2,3]}
# unhashable type: 'list'
#print(set)

'''
Boolean Type (True or False')
'''
#print(type(True))

# boolean as numbers
#print(True == 1)
#print(False == 0)

# interesting logic
#print(True + True)

# not boolean operator
#print(not True)
#print(not False)

# and boolean operator
#print(True and False)
#print(True and True)
#print(False and False)

#or boolean operator
#print(True or False)
#print(True or True)
#print(False or False)










