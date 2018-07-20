# def say_hello():
#     print('Hello World')
#
# say_hello()
# #say_hello

#function definition - parameters
#function call - arguments

# def print_max(a,b):
#     if a > b:
#         print(a, 'is maximum')
#     elif a==b:
#         print('Both are equal')
#     else:
#         print(b, 'is maximum')
#
# print_max(1,2)
#
# x=3
# y=3
#
# #passing variables as arguments
# print_max(x,y)


#Local variable

# global_var=50
#
# def func_local(global_var):
#     print('global variable is ', global_var)
#     global_var=5
#     print('global changed to ',global_var)
#
# func_local(global_var)
#
# print('global variable is ', global_var)


#Global variable
# x = 50
#
# def func():
#     global x
#
#     print('x is', x)
#     x = 2
#     print('Changed global x to', x)
#
#
# func()
# print('Value of x is', x)

# #Default arguments
# def say(message,times=1):
#     print(message*times)
#     print(message, times)
# say('hi',5)
# say('hi')
# #say(5,'hi')

# #Keyword arguments

# def func(a, b=5, c=10):
#     print('a is', a, 'and b is', b, 'and c is', c)
#
# func(3, 7)
# func(25, c=24)
# func(c=50, a=100)
#

#VarArgs
# #*param - arguments collected as tuple
# #**param - arguments collected as dict
#
# def phone_book(*entry_line,**names_num):
#     for line in entry_line:
#         print('Line num is', line)
#     for name,num in names_num.items():
#         print(name,num)
#
# phone_book(3,1,2,3,Hi=1200,Hello=3456,Welcome=7456)


#return statement
# def maximum(x, y):
#     if x > y:
#         return x
#     elif x == y:
#         return 'The numbers are equal'
#     else:
#         return y
#
# print(maximum(2, 3))

#DocStrings

def increment_by_1(a):
    '''Add 1 in loop.

    Argument should be non-negative and greater than 1'''
    for i in range(1,a):
        print(i+1)

increment_by_1(10)
print(increment_by_1.__doc__)
