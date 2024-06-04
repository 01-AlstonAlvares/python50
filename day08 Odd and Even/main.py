#Write a function called odd_even that has one parameter
#and takes a list of numbers as an argument. The function
#returns the difference between the largest even number in
#the list and the smallest odd number in the list. For example,
#if you pass [1,2,4,6] as an argument the function should
#return 6 -1= 5

def odd_even(numbers):
    large_even = None
    small_odd = None

    for num in numbers:
        if num % 2 == 0:
            if large_even is None or num > large_even:
                large_even = num
        else:
            if small_odd is None or num < small_odd:
                small_odd = num

    if large_even is None or small_odd is None:
        print("Enter valid numbers")
    difference = large_even - small_odd
    return difference

numbers = [1,2,4,6]
result = odd_even(numbers)
print(result)