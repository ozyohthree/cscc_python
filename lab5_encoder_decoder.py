# FILE: encoder_decoder.py
# NAME: Encodes Or Decodes user input
# AUTHOR: Anthony Gimei
# DATE: 5/6/2018
# PURPOSE: Encodes or Decodes input string from user using certain rules
# Submission confirmation number:

# encoding A=1,B=2,C=3,D=4,E=5,F=6,G=7,H=8,I=9,J=10,K=11,L=12,M=13,N=14,O=15,P=16,Q=17,R=18,S=19,T=20,U=21,V=22,W=23,X=24,Y=25,Z=26
alpha = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P","Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
alphabet = "abcdefghijklmnopqrstuvwxyz"

# Define a function for decoding
def encode(string_to_encode):
    string_to_encode = string_to_encode.upper()
    #print(string_to_encode)
    encoded_string = ""

    for character in string_to_encode:
        #print(character)
        if character == "-":
            encoded_string = encoded_string
        elif character == " ":
            encoded_string = encoded_string[:-1] + ' '
        else:
            counter = 0
            special_char = True
            for letter in alpha:
                #print(letter, character)
                counter += 1
                if character == letter:
                    encoded_string = encoded_string + str(counter) + '-'
                    special_char = False
                    break
            if special_char:
                encoded_string = encoded_string[:-1] + character + '-'

    return encoded_string[:-1]

def decode(string_to_decode):
    word_array = string_to_decode.split(" ")
    decoded_words_array = []
    # print(word_array)
    # print()
    num_words = len(word_array)
    decoded_words_array = [''] * num_words
    if num_words > 1:
        for i in range (0,num_words):
            word_to_decode = word_array[i]
            # print(word_to_decode)
            word_to_decode_array = word_to_decode.split("-")
            decoded_word = ""
            for number in word_to_decode_array:
                if len(number) > 2:
                    number = number[:2]
                # print(number)
                # decode letter and put it in new string
                counter = 0
                for letter in alpha:
                    counter += 1
                    if number.isnumeric():
                        if int(number) == counter:
                            #print(letter)
                            decoded_word = decoded_word + letter

            decoded_words_array[i] = decoded_word

    decoded_string = ""
    for word in decoded_words_array:
        decoded_string = decoded_string + word + " "

    return decoded_string.capitalize()


def decode_v2(string_to_decode):
    number_to_decode = ""
    decoded_word = ""
    counter = 0
    for char in string_to_decode:
        counter += 1
        if str(char).isnumeric():
            number_to_decode += char
        elif str(char) == "-" or str(char) == " ":
            # print(number_to_decode)
            # if not str(char) == "-":
            decoded_word += number_to_decode + char
            number_to_decode = ""
        else:
            # print(number_to_decode)
            decoded_word += number_to_decode + char
            number_to_decode = ""
        if str(char) == ' ':
            print(decoded_word)
            decoded_word = ""
        if counter  == len(string_to_decode):
            print(decoded_word)
            decoded_word = ""

    # return number_to_decode


def encode_v2(string_to_encode):
    string_to_encode = string_to_encode.lower()
    str_len = len(string_to_encode)
    decoded_str = ""
    for x in string_to_encode:
        if str(x).isalpha():
            index = alphabet.find(x)
            decoded_str += str(index + 1) + '-'
        else:
            decoded_str += x

    return decoded_str


while True:
    try:
        user_input = (input("Enter String to Encode or decode\n"))
        if user_input[0].isnumeric():
            print(decode(user_input))
            break
        else:
            print(encode(user_input))
            break
        break
    except ValueError:
        print("Please enter Valid string... try again")
