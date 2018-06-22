# FILE: python_amusement_park_tierer.py
# NAME: Display amusement park guest tier
# AUTHOR: Anthony Gimei
# DATE: 4/20/2018
# PURPOSE: Accepts guest height then display Cost Tier
# Submission confirmation number: f6a012e1-59bc-423b-868c-37740107556b

while True:
    try:
        input_height = int(input("Enter Height in Inches (whole Number only):\n"))
        break
    except ValueError:
        print("Please enter Height in whole Numbers only... try again")

if (input_height > 0) and (input_height < 30):
    print("Tier: Gumpy, You come in FREE.")
elif (input_height >= 30) and (input_height < 36):
    print("Tier: Pollywog. Cost of Ticket = $2.")
elif (input_height >= 36) and (input_height < 42):
    print("Tier: Apprentice. Cost of Ticket = $5.")
elif (input_height >= 42) and (input_height < 48):
    print("Tier: Explorer. Cost of Ticket = $8.")
elif (input_height >= 48):
    print("Tier: Adventurer. Cost of Ticket = $10.")
else:
    print("You entered an invalid Height.... try again")

