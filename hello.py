print ("Hello World")
print('Interest Calculator')

amount = float(input('Enter Principal amount : '))
roi = float(input('Enter Rate of Interest : '))
yrs = int(input('Enter Duration (no. of years) : '))

total = (amount * pow(1 + (roi/100), yrs))
interest = total - amount
print('\nInterest = %0.2f' %interest)
