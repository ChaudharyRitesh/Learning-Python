# list set dictionary

# list comprehension
# my_list = [char for char in 'hello']
# my_list2 = [num for num in range(0,100)]
# my_list3 = [num**2 for num in range(0,100)]
# my_list4 = [num**2 for num in range(0,100) if num % 2 == 0]

# # for i in 'hello':
# #     my_list.append(i)

# # print(my_list)
# # print(my_list2)
# print(my_list4)



# set comprehension

# my_list = {char for char in 'hello'}
# my_list2 = {num for num in range(0,100)}
# my_list3 = {num**2 for num in range(0,100)}
# my_list4 = {num**2 for num in range(0,100) if num % 2 == 0}

# print(my_list4)


# dictionary comprehension
simple_dict = {
    'a':1,
    'b':2
}

my_dict = {key:value**2 for key, value in simple_dict.items()}

print(my_dict)