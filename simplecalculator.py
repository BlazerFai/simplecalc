# -*- coding: utf-8 -*-
"""simplecalculator.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1IpMdRxG8RzC6gho_RNxU2ok1t-FtbOd4
"""

number1 = input("Enter a number:")
number2 = input("Enter another number:")

print("Okay now, choose your operation!")
op = input("+ - x /")
if (number1 and number2 == "0" and op == "/"):
    raise Exception("Nice try, you can't divide by 0")
if(op == "+"):
    print(int(number1) + int(number2))
elif(op == "-"):
    print(int(number1) - int(number2))
elif(op == "x"):
    print(int(number1) * int(number2))
elif(op == "/"):
    print(int(number1) / int(number2))
else:
    print("Invalid!")

