# LAB 1
# We are baking brownies!  We have a recipe which calls for the following ingredients:
# 0.5 cups butter
# 2 eggs
# 1 teaspoon vanilla
# 1 cup sugar
# 0.5 cups flour
# 0.5 cups cocoa powder
# 0.25 teaspoons baking powder
# 0.25 teaspoons salt
# The ingredients in this recipe will make 9 brownies.
# Write a program which asks the user how many brownies they wish to bake,
# then displays the adjusted recipe with the correct amounts for making that number of brownies.
# Don't worry about converting teaspoons to cups (etc) - just display the amounts in their original measurements.

# AUTHOR: ANTHONY GIMEI
# DATE SUBMITTED: 4/14/2018
# Confirmation number: The submission confirmation number is 7493a083-1937-4139-bda5-dcc572f93423


number_brownies = int(input("Enter number of Brownies to make: "))
cooking_ratio = float(number_brownies/9)
#Now print the recipe
print(0.5*cooking_ratio,"cups butter")
print(2*cooking_ratio,"eggs")
print(1*cooking_ratio,"teaspoon vanilla")
print(1*cooking_ratio,"cup sugar")
print(0.5*cooking_ratio,"cups flour")
print(0.5*cooking_ratio,"cups cocoa powder")
print(0.25*cooking_ratio,"teaspoons baking powder")
print(0.25*cooking_ratio,"teaspoons salt")


