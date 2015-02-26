__author__ = 'Dani'
score = raw_input('Enter value between 0.0 and 1.0')
score_value = float(score)
if score_value >= 0.0 and score_value<= 1:
    if score_value >= 0.9:
        print 'A'
    elif score_value >= 0.8:
        print 'B'
    elif score_value >= 0.7:
        print 'C'
    elif score_value >= 0.6:
        print 'D'
    else:
        print 'F'
else:
    print('Value is outside of range')


