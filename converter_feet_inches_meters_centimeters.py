# FILE: converter_feet_inches_meters.py
# NAME: Length Converter
# AUTHOR: Anthony Gimei
# DATE: 4/16/2018
# PURPOSE: Converts Feet and Inches to Meters and Centimeters

while True:
    try:
        input_feet = float(input("enter feet: "))
        break
    except ValueError:
        print("Please enter Numbers only... try again")

while True:
    try:
        input_inches = float(input("enter inches: "))
        break
    except ValueError:
        print("Please enter Numbers only... try again")
        
output_centimeters = input_feet * 30.48
output_centimeters = output_centimeters + (input_inches * 2.54)
output_meters = output_centimeters/100

print()
print(output_meters," m")
