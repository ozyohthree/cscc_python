fin = open('flat_files\\words.txt')

count = 0

for line in fin:
    count += 1

print("Line Count", count)
