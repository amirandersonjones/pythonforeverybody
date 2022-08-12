# name = input("Enter your name: ")
# print(f"hello, {name}")

# write a program to prompt the user for hours and rae per hour to compute gross pay
# hours = input("Enter your hours: ")
# hours = float(hours)
# rate = input("Enter your pay rate: ")
# rate = float(rate)
# pay = hours * rate
# print(f"your total amount of hours was {hours}, your pay rate is ${rate}. Your total pay for this period is ${pay}")

# width = 17
# height = 12.0

# print(width/2.0, type(width))
# x=0
# y=10
# if 0 == x:
#     if y == 10:
#         print("Yes")

# for i in range(5):
#     print(i)
#     if i > 2:
#         print("Bigger than 2")
#     print("Done with i", i)
# print("All done")

# def helloworld(name):
#     print(f"Hello {name}")

# helloworld("AMir")

# Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours.Rewrite your pay program using try and except so that your program handles non-numeric input gracefully by printing a message and exiting the program. The following shows two executions of the program:
# hours = input("Enter your hours do not include overtime: ")
# try:
#     hours = float(hours)
# except:
#     print("Im sorry, you must enter a numberic value")
#     quit()
# rate = input("Enter your pay rate: ")
# rate = float(rate)
# overtime = input("How many hours over 40 did you work?: ")
# overtime = float(overtime)
# halftime = rate + (rate/2)


# pay = (hours * rate) + (overtime * halftime)
# print(f"your total amount of hours was {hours}, your pay rate is ${rate}. Your total pay for this period is ${pay}")

# def greet_language(language):
#     if language == "spanish":
#         print("hola")
#     elif language == "french":
#         print("bonjour")
#     else:
#         print("Hello")
# greet_language("german")

# def greet():
#     return "Hello"
# print(greet(), "Amir")

# Rewrite your pay computation with time-and-a-half for overtime and create a function called computepay which takes two parameters(hours and rate).

# def computepay ():
#     hours = input("how many hours did you work?: ")
#     hours = float(hours)
#     rate = input("what is your pay rate?: ")
#     rate = float(rate)
#     halftime = rate + (rate/2)
#     overtime = hours - 40
#     if hours > 40:
#         pay = (hours - 40) * halftime + (hours - overtime) * rate
#     else:
#         pay = hours * rate
#     return pay

# print(computepay())

# for i in [5, 4, 3, 2, 1]:
#     print(i)

# number = 0
# for num in [1, 2, 3, 4, 5]:
#     number = number + num
#     print(num, number)
# print(number)

# friends = ["Mary", "Bobby", "Sue", "Rachel"]
# foundSue = False
# for friend in friends:
#     print(friend)
#     if friend == "Sue":
#         foundSue = True
#         print("found Sue")
#         break


# Exercise 1: Write a program which repeatedly reads numbers until the user enters “done”. Once “done” is entered, print out the total, count, and average of the numbers. If the user enters anything other than a number, detect their mistake using try and except and print an error message and skip to the next number.
#
# from statistics import median


# done = False
# total = 0
# numbercount = 0
# while done == False:
#     donechoice = input("Would you like to enter a number type 'yes' to continue or type 'done' to quit: ")
#     if donechoice == "done":
#         done = True
#         break
#     else:
#         numberchoice = input("Please enter a numeric value")
#         numberchoice = int(numberchoice)
#         total += numberchoice
#         numbercount += 1
#         average = total/numbercount
#         print(total, numbercount, average)

# fruit = "banana"
# index = 0
# while index < len(fruit):
#     print(index, fruit[index])
#     index += 1


# friend = "Kellie"
# index = 0
# while index < len(friend):
#     print(index, friend[index])
#     index += 1

# friend = "Kellie"
# for letter in friend:
#     print(letter)

# count = 0
# word = "africa"
# for letter in word:
#     if letter == "a":
#         count +=1
# print(count)

# pizza = "sausage"
# index = 0
# while index < len(pizza):
#     print(index, pizza[index])
#     index += 1


# friend = "Kellie"
# # print(dir(friend))

# # print(friend.find("el"))
# print(friend.swapcase())

# Exercise 5: Take the following Python code that stores a string:

# str = 'X-DSPAM-Confidence:0.8475'

# Use find and string slicing to extract the portion of the string after the colon character and then use the float function to convert the extracted string into a floating point number.

# print(str.find(":"))
# colonpos = str.find(":")
# colonpos = float(colonpos)
# print(colonpos)


# fhand = open("mbox-short.txt")
# count = 0
# for line in fhand:
#     count = count + 1
# print("Line Count: ", count)

# fhand = open("mbox-short.txt")
# inp = fhand.read()
# print(inp)
# print(len(inp))
# print(inp[:20])

# fhand = open("mbox-short.txt")
# for line in fhand:
#     line = line.rstrip()
#     if line.startswith("From:"):
#         print(line)

# fhand = open("mbox-short.txt")

# for line in fhand:
#     line = line.rstrip()
#     if not '@uct.ac.za' in line:
#         continue
#     print(line)

# filename = input("Please enter a file name: ")
# try:
#     fhand = open(filename)
# except:
#     print("File cannot be opened")
#     quit()
# count = 0
# for line in fhand:
#     if line.startswith("Subject:"):
#         count += 1
# print(f"There were {count}, subject lines in {filename}")

# Exercise 1: Write a program to read through a file and print the contents of the file(line by line) all in upper case. Executing the program will look as follows:

# fhand = open("mbox-short.txt")
# for line in fhand:
#     print(line.upper())

# abc = "These three words"
# splitabc = abc.split()
# print(splitabc)
# for word in splitabc:
#     print(word)

# stringofstuff = "These,are,my,words"
# newstring = stringofstuff.split(",")
# print(newstring)

# Write a program to read through the mail box data and when you find line that starts with “From”, you will split the line into words using the split function. We are interested in who sent the message, which is the second word on the From line.
# You will parse the From line and print out the second word for each From line, then you will also count the number of From (not From:) lines and print out a count at the end. This is a good sample output with a few lines removed

# from unittest.util import _count_diff_hashable


# count = 0
# fhand = open("mbox-short.txt")
# for line in fhand:
#     line = line.rstrip()
#     if line.startswith("From"):
#         count += 1
#         line.split()
#         # print(line)
#         newline = line.split()
#         print(newline[1])

# print(count)

# basically create a range of n and times the index of n by x
# empty_list = []
# def count_by(x, n):
#     """
#     Return a sequence of numbers counting by `x` `n` times.
#     """
#     for i in range(1, n+1):
#         empty_list.append(i*x)
#     return empty_list
# print(count_by(2, 5))

# leap year
# years divisible by 4 are leap years
# but years divisible by 100 are not leap years
# but years divisible by 400 are leap years
# def isLeapYear(year):
#     return year % 100 != 0 and year % 4 == 0 or year % 400 == 0

# print(isLeapYear(1100))

# emptylist = []
# def count_by(x, n):
#     """
#     Return a sequence of numbers counting by `x` `n` times.
#     """
#     for i in range(1, n+1):
#         emptylist.append(i*x)
#     return emptylist

# print(count_by(3,5))
# count = {}
# pizzas = ["sausage", "pepperoni", "cheese", "cheese", "mushroom", "cheese"]
# for pizza in pizzas:
#     if pizza not in count:
#         count[pizza] = 1
#     else:
#         count[pizza] = count[pizza] + 1
# print(count)

# count = {}
# phrase = input("Please enter a line of text: ")
# phraselist = phrase.split()
# print(phraselist)
# for word in phraselist:
#     if word not in count:
#         count[word]= 1
#     else:
#         count[word] = count[word] + 1
# print(count)

# count = {}
# phrase = input('Please enter a phrase: ')
# newphrase = phrase.split()
# print(newphrase)
# for word in newphrase:
#     if word not in count:
#         count[word] = 1
#     else:
#         count[word] = count[word] + 1
# print(count)

# d= {'a': 10, 'b':1, 'c':22}
# print(d.items())
# sortedItems = sorted(d.items())
# print(sortedItems)

#  d= {'a': 10, 'b':1, 'c':22}

# for key, value in sorted(d.items()):
#     print(key, value)

# d= {'a': 10, 'b':1, 'c':22}
# tempList = []
# for key, value in d.items():
#     tempList.append((value, key))
# print(tempList)

# tempList = sorted(tempList)
# print(tempList)

# tempList = sorted(tempList, reverse=True)
# print(tempList)
# ----simple way-----
# d= {'a': 10, 'b':1, 'c':22}
# print(sorted( [ (v,k) for k,v in d.items() ] ))


# with open('mbox-short.txt') as f:
#     output= f.read()
#     print(output)

# ------------REGULAR EXPRESSIONS-----------
# import re

# hand = open('mbox-short.txt')
# for line in hand:
#     line = line.rstrip()
#     if re.search('From:', line):
#         print(line)


# -----------USING WEB SERVICES-----------
# 1.) XML- eXtensible Markup Language
        # primary purpose is to help information systems share structured data
    