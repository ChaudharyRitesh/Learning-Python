# map() filter(), zip() reduce

from functools import reduce


my_list = [1,2,3]
your_list = [10, 20, 30]

def multiply_by2(item):
    return item * 2

print(list(map(multiply_by2, my_list)))


# filter
def check_odd(num):
    return num % 2 != 0

print(list(filter(check_odd, my_list)))


# zip()
print(list(zip(my_list, your_list)))


# reduce()

def accumalator(acc, item):
    print(acc, item)
    return acc + item

print(reduce(accumalator, my_list, 0))

print(my_list)