"""
Module 2
"""

# Random Import


# from random import randint
# length = int(input("Enter the length of a triangle: "))
# width = randint(1, length)
# area = length * width
# print(f"Width is, {width}")
# print(f"Area is, {area}")


# Creating Functions


# # Print a Line
# def print_line(length):
#     print("-" * length)
#
#
# print_line(20)
#
#
# # Main Function
# def main():
#     print_line(20)
#     print("Welcome!")
#     print_line(20)


# main()


# Using Functions


# def print_grid(number_of_rows, number_of_columns):
#     # print(f"{"*" * number_of_columns}\n" * number_of_rows)
#     for i in range(number_of_rows):
#         print("*" * number_of_columns)
#
#
# print_grid(3, 7)


# Using Return
# Used to return a functions output as the functions value so it can
# be used in a condition


# def main():
#     height = float(input("Enter height (m): "))
#     weight = float(input("Enter weight (kg): "))
#     bmi = calculate_bmi(height, weight)
#     print(f"Your BMI is {bmi:.2f}")
#
#
# def calculate_bmi(height, weight):
#     return weight / (height ** 2)

#
# main()


# from random import randint
#
# rand_number = randint(1, 100)
#
#
# def is_even(number):
#     return number % 2 == 0
#
#
# print(rand_number)
# print(is_even(rand_number))

# def get_limits():
#     low = int(input("Enter lower limit: "))
#     high = int(input("Enter upper limit: "))
#     return low, high
#
#
# def run_tests():
#     low_number, high_number = get_limits()
#     print(low_number, high_number)
#     print(type(low_number), type(high_number))
#
#
# run_tests()


# Function Demo

#
# import random
#
#
# def main():
#     name = ""
#     menu = """
#     ----------------
#     1 - Input Name
#     2 - Display Name
#     3 - Secret Name
#     Q - Quit
#     ----------------\n"""
#     print(menu)
#     choice = input(">>> ").upper()
#     while choice != 'Q':
#         if choice == '1':
#             name = get_name()
#         elif choice == '2':
#             display_name(name)
#         elif choice == '3':
#             display_secret_name(name)
#         else:
#             print("Invalid Input")
#         print(menu)
#         choice = input(">>> ").upper()
#     print("Closing Program")
#
#
# def display_name(name):
#     if name == "":
#         print("\nPlease enter a name first")
#     else:
#         print()
#         print_lines(len(name))
#         print(name)
#         print_lines(len(name))
#
#
# def display_secret_name(name):
#     if name == "":
#         print("\nPlease enter a name first")
#     else:
#         letters = list(name)
#         random.shuffle(letters)
#         name = "".join(letters)
#         print(f"\n{name}")
#
#
# def get_name():
#     """Get the users name"""
#     name = input("\nWhat's your name? \n")
#     while name == "":
#         print("Invalid Input")
#         name = input("\nWhat's your name? \n")
#     return name
#
#
# def print_lines(length):
#     print("-" * length)
#
#
# main()


# Function Names


# constants are ALL CAPS

# determine_grade
# convert_currency_usa_aud
# display_report
# calculate_list_average
# determine_if_even
# get_real_age

# Parameters

# def print_lines(length: int , pen: str): # Used to specify data type
# def print_lines(length, pen):
#     """Print a line of length pen characters"""
#     print(pen * length)
#
#
# print_lines(10, '-')


# Week 2 Lecture Questions

from random import randint

high_number = int(input("Enter a number: "))
low_number = int(input("Enter a lower number: "))

while high_number < low_number:
    print("Please ensure the second number is LOWER than the first number.")
    high_number = int(input("Enter a number: "))
    low_number = int(input("Enter a lower number: "))

rand_number = randint(low_number, high_number)

print(rand_number * ":)")
