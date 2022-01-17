#problem: round each number into two decimal places, e.g from 93.036584 to 93.03

# people did this:
def two_decimal_places(number):
    #the "int" turns the number which was times by 10 into a whole number first, then it divides back into a decimal
    return int(number * 100) / 100.0

#easier way of explaining, first turn into a whole number(int) then return the number after dividing it by ten

def two_decimal_places(number):
    number = int (number * 100)
    return number/100