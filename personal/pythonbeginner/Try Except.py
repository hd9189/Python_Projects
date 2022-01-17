try:
    print("Hi!")
    value = 10/2
    number = int(input("Enter a number: "))
    print(number)
    print("Yo!")
except ZeroDivisionError:
    print("ZeroDivisionError")
except ValueError:
    print("Invalid input")
finally:
    print("this works")