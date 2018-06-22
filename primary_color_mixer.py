# FILE: primary_color_mixer.py
# NAME: Outputs new color name
# AUTHOR: Anthony Gimei
# DATE: 4/18/2018
# PURPOSE: Takes 2 primary colors as input and output new color name

print("Please enter any 2 Primary colors (Red, Blue or Yellow)")
while True:
    try:
        first_color = (input("Enter First Color:\n"))
        first_color = first_color.lower()
        if first_color == 'red' or first_color == 'blue' or first_color == 'yellow':
            break
    except ValueError:
        print("Please enter Valid Primary Color only... try again")

while True:
    try:
        second_color = (input("Enter Second Color:\n"))
        second_color = second_color.lower()
        if (second_color == 'red' or second_color == 'blue' or second_color == 'yellow') and (second_color != first_color):
            break
    except ValueError:
        print("Please enter Valid Primary Color only... try again")

if(first_color == 'red' or first_color == 'blue') and (second_color == 'red' or second_color == 'blue'):
    print(first_color.capitalize(), '+', second_color.capitalize(), '= Purple!')
if(first_color == 'blue' or first_color == 'yellow') and (second_color == 'blue' or second_color == 'yellow'):
    print(first_color.capitalize(), '+', second_color.capitalize(), '= Green!')
if(first_color == 'yellow' or first_color == 'red') and (second_color == 'yellow' or second_color == 'red'):
    print(first_color.capitalize(), '+', second_color.capitalize(), '= Orange!')
