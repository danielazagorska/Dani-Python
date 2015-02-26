__author__ = 'Dani'
def computepay(pay_value,hours_value):
    salary = float()
    if hours_value <= 40:
        salary = hours_value * pay_value
        return salary
    elif hours_value > 40:
        salary = ((hours_value-40) * 1.5 * pay_value + 40* pay_value)
        return salary
hours = raw_input('Enter Hours')
hours_value = float(hours)
try:
    hours_value = float(hours)
except:
    print 'enter a numerical value'
    exit(1)
pay = raw_input('Enter Payrate')
pay_value = float(pay)
try:
    pay_value = float(pay)
except:
    print 'enter a numerical value'
    exit(1)
print ('Your salary will be ' + str(computepay(pay_value,hours_value)))