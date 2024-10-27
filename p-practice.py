

#1. FizzBuzz: Write a function that prints the numbers from 1 to 100. But for multiples of three, print "Fizz" instead of the number, and for the multiples of five, print "Buzz". For numbers which are multiples of both three and five, print "FizzBuzz".

# def my_function():
#     for i in range(1, 101):
#         if i%3 ==0 and i%5 ==0:
#             print("FizzBuzz")
#         elif i%3 ==0:
#             print("Fizz")
#         elif i%5 == 0:
#             print("Buzz")
#         else:
#             print(i)


# my_function()

# Palindrome Checker: Create a function that takes a string as input and returns True if the string is a palindrome (reads the same forwards and backwards) and False otherwise. Ignore spaces, punctuation, and capitalization.

def is_palindrome(input_str):
    


    res = str == str[-1::-1]
    if res:
        print (f"{str} is a pallindrome")
    else:
        print (f"{str} is not a pallindrome")

str = input("Enter a string to check palindrome: ")
str1 = str.lower()
is_palindrome(str)