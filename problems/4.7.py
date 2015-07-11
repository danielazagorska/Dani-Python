__author__ = 'Dani'
def computegrade(score_value):
    if score_value >= 0.0 and score_value<= 1:
        if score_value >= 0.9:
            return 'A'
        elif score_value >= 0.8:
            return 'B'
        elif score_value >= 0.7:
            return 'C'
        elif score_value >= 0.6:
            return 'D'
        else:
            return 'F'
    else:
        return('Value is outside of range')
score = raw_input('Enter value between 0.0 and 1.0')
score_value = 1
try:
    score_value = float(score)
except:
    print ('Please enter a cat')
    exit(1)
print computegrade(score_value)
#comment