#!/usr/bin/env python3

def happy_new_year():
    i=1
    while i<=10:
        print(i)
        print("Happy New Year!")
        i+=1

def square_integers(int_list):
    return[i**2 for i in int_list]

def fizzbuzz():
    for a in range(1, 101):
        if a % 3 == 0  and a% 5 == 0:
            print("FizzBuzz")
        elif a % 3 == 0:
            print("Fizz")
        elif a % 5 == 0:
            print("Buzz")
        else:
            print(a)
    
