#Create a function called biggest_odd that takes a string of numbers
#and returns the biggest odd number in the list. For example, if you
#pass ‘23569’ as an argument, your function should return 9. Use list
#comprehension

def biggest_odd(s):
    odd_num=[int(char) for char in s if int(char) % 2 != 0]
    return max(odd_num) if odd_num else None

print(biggest_odd('23569'))
