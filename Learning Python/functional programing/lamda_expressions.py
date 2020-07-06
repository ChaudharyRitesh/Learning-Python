# one time anonymous functions you only use them once

# lamda param: manipulation/function(param)

my_list = [1,2,3]

# def multiply(item):
#     return item * 2


print(list(map(lambda item: item*2, my_list)))
print(my_list)