alpha = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P","Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
str = "1-14-20-8-15-14-25 7-9-13-5-9"
word_array = str.split(" ")
decoded_words_array = []
print(word_array)
print()
num_words = len(word_array)
decoded_words_array = [''] * num_words
if num_words > 1:
    for i in range (0,num_words):
        word_to_decode = word_array[i]
        print(word_to_decode)
        word_to_decode_array = word_to_decode.split("-")
        decoded_word = ""
        for number in word_to_decode_array:
            print(number)
            # decode letter and put it in new string
            counter = 0
            for letter in alpha:
                counter += 1
                if int(number) == counter:
                    print(letter)
                    decoded_word = decoded_word + letter

        decoded_words_array[i] = decoded_word

    decoded_string = ""
    for word in decoded_words_array:
        decoded_string = decoded_string + word + " "

    print(decoded_string)



# counter = 0
# for letter in alpha:
#    counter += 1
#    print(letter + '=' + str(counter), end=",")
