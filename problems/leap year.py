__author__ = 'Dani'
year_entered = raw_input('enter year')
year = float(year_entered)
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        print('This is a leap year')
else:
        print('This is not a leap year')

