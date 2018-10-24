# The different Data structures and how to use them


#List = Array / mutable
myLanguageList = ['Java', 'Python', 'Go']
anIntegersList = [10, 20, 30]
#print(myLanguageList)
#looping through my list

#for language in myLanguageList:
#    print(language)

list_1 = ['spam', 2.0, 5, [10, 20]]
#for item in list_1:
#   print(item)

myNestedList = [['Ok language', 'VB'], ["Better Language", "Java"]]
#print(myNestedList[0][1])

myDictionary = dict()
myDictionary['key'] = 'value'

#print(myDictionary)

#slicing: The operator [n:m] returns the part from the "n-eth" to the "m-eth",
# including the first but excluding the last.
# If you omit the first index, the slice starts at the beginning.
# If you omit the second, the slice goes to the end.
# So if you omit both, the slice is a copy of the whole list.
# use negative numbers to slice backwards
# eg e[-6:-1]) We start 6th posn from the end
# and end at 1st posn from the end of the string.


# List of Months
months = ["January", "February", "March","April", "May", "June", "July", "August", "September","October", "November", "December"]

# Using List Slicing to
# create a new list "summer" months
# summer_months = (June, July, and August)
summer_months = months[5:8]
print('\nSummer Months are:')
for month in summer_months:
    print(month)

#tax_season = jan, feb, march
print('\nTax Season Months are:')
tax_season = months[:4]
for month in tax_season:
    print(month)

#shopping_season = nov, dec
print('\nShopping Months are:')
shopping_season = months[10:]
for month in shopping_season:
    print(month)

#fall_months = sep, oct, nov, dec
print('\nFall Months are:')
fall_months = months[-4:]
for month in fall_months:
    print(month)


        


