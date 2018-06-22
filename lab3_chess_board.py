# FILE: chess_board.py
# NAME: Displays text-only chess board
# AUTHOR: Anthony Gimei
# DATE: 4/25/2018
# PURPOSE: Prints out a text-only chess board
# Submission confirmation number: c9484f51-7e8c-4893-8aea-716ecf390ec0

rows = [8, 7, 6, 5, 4, 3, 2, 1]
columns = ["a", "b", "c", "d", "e", "f", "g", "h"]

print("-----------------------------------------", end="")
for row in rows:
    print("\n| ", end="")
    for column in columns:
        print(column, row, " | ", sep="", end="")
    else:
        print("\n-----------------------------------------", end="")

