# FILE: lab_6_State_quiz.py
# NAME: Displays state abbreviation for user to guess
# AUTHOR: Anthony Gimei
# DATE: 5/24/2018
# PURPOSE: Accepts user guess of displayed State abbreviation and lets user know how many the got correct
# Submission confirmation ID: 61b97ce4562b43dc8e32809c3091974c

import random
random_low = 1
random_high = 50
continue_playing = True

states = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

correct = 0
incorrect = 0

while continue_playing:
    random_number = random.randint(random_low, random_high)
    try:
        counter = 0
        guess_state = ""
        for state in states:
            counter += 1
            if counter == random_number:
                guess_state = state
        user_guess_state = input("What state has abbreviation " + states[guess_state] + "\n")
        if user_guess_state.upper() == guess_state.upper():
            print("You got it!.\n")
            correct += 1
        else:
            print("Nope, its", guess_state, "\n")
            incorrect += 1

        want_to_continue = input("Do you want to play again(Type 'y' or 'yes' to play again)?\n")
        if want_to_continue.lower() == "y" or want_to_continue == "yes":
            continue_playing = True
        else:
            continue_playing = False
            print("You got", correct, "correct and", incorrect, "incorrect")

    except ValueError:
        print("Please Enter valid input only... try again")
