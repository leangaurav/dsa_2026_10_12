# Write a function : 'rand_list' that takes a start, end and count and returns a list 
# of random numbers in the range start and end(inclusive). 
# Length of list should be equal to count.
# Example output: rand_list(-10,10, 3) -> [-1, 10, 0]

from random import randrange
def rand_list(start, end, count):
    res = []
    for i in range(count):
        res.append(randrange(start, end+1))
    return res


print(rand_list(-10,10,4)) 
print(rand_list(-10,10,0)) # test case
print(rand_list(-10,10,-1)) # test case
print(rand_list(10,-10,4)) # test case
