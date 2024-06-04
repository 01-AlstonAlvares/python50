#Write a function called string_range that takes a single number and
#returns a string of its range. The string characters should be
#separated by dots(.) For example, if you pass 6 as an argument,
#your function should return ‘0.1.2.3.4.5’

def string_range():
    num1 = int(input("Enter a number: "))
    if num1 > 0:
        for n in range(num1):
            print("." + str(n))
            if n == num1:
                break
    else:
        print("Enter a valid integer")


string_range()
