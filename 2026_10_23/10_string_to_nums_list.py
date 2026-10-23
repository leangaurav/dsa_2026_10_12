# Input a sequence of number separated by spaces and convert it into a list of numbers
nums = input('enter numbers separated by space: ')

result = []
for val in nums.split():
    result.append(int(val))

print(result, sum(result), min(result), max(result))
