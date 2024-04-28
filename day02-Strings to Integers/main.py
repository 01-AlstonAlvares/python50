#Write a function called convert_add that takes a list of strings as an
#argument and converts it to integers and sums the list. For example
#[‘1’, ‘3’, ‘5’] should be converted to [1, 3, 5] and summed to 9.
def convert_add(stre):
    int_list = [int(num) for num in stre]
    total = sum(int_list)

    return total


input_list = ['1', '3', '5']
result = convert_add(input_list)
print(result)
