# 1.	Используя функцию map() переписать функцию
# items = [1, 2, 3, 4, 5]
# squared = []
# for i in items:
#     squared.append(i**2)# решение:

# решение:
# items = [1, 2, 3, 4, 5]
# new_items = list(map(int, items))
# squared = []
# for i in items:
#     squared.append(i**2)
# print(squared)

# другой вариант
# items = [1, 2, 3, 4, 5]
# new_items = list(map(lambda i: i ** 2, items))
# squared = []
# for i in items:
#     squared.append(i**2)
# print(squared)

#----------------------------------------------------------------------

# 2.	Используйте функцию reduce() и перепишите код

# product = 1
# list = [1, 2, 3, 4]
# for num in list:
#     product = product * num
# print(product)

# решение:
# from functools import reduce
# list1 = [1, 2, 3, 4]
# product1 = reduce(lambda x, y: x * y, list1)
# print(product1)

#----------------------------------------------------------------------

# 3.	Используйте функцию map() и перепишите код
#
# numbers = [1, 2, 3, 4, 5]
# squared = []
# for num in numbers:
#        squared.append(num ** 2)
# print(squared)

# решение:
# numbers = [1, 2, 3, 4, 5]
# new_numbers = list(map(int, numbers))
# squared = []
# for num in numbers:
#        squared.append(num ** 2)
# print(squared)
#
# # другой вариант
# numbers1 = [1, 2, 3, 4, 5]
# new_numbers1 = list(map(lambda num: num ** 2, numbers1))
# squared1 = []
# for num in numbers1:
#        squared1.append(num ** 2)
# print(squared1)

#----------------------------------------------------------------------

# 4.	Объедините списки x = [1, 2, 3] и y = [4, 5, 6] с помощью функции zip()

# решение:
# x = [1, 2, 3]
# y = [4, 5, 6]
#
# res = list(zip(x, y))
# print(res)

#----------------------------------------------------------------------

# 5.	Используйте функцию zip() чтобы преобразовать код:
#
# name_hero = [
#     'Hulk',
#     'Mr. Fantastic',
#     'Invisible Woman',
#     'Doctor Strange',
#     'Doctor Octopus',
#     'Spider-Man',
# ]
#
# name_real = [
#     'Bruce Banner',
#     'Reed Richards',
#     'Sue Storm',
#     'Stephen Strange',
#     'Otto Octavius',
#     'Peter Parker',
# ]
#
# for i in range(len(name_hero)):
#     print(name_hero[i], '-', name_real[i])
#
# # решение:
# res = list(zip(name_hero, name_real))
# print(res)


#----------------------------------------------------------------------

# 6.	С помощью функции filter() переместите из списка numbers = [1, 2, 4, 5, 7, 8, 10, 11]
# нечетные элементы в новый список.

# решение:
# numbers = [1, 2, 4, 5, 7, 8, 10, 11]
#
# odd_elements = list(filter(lambda x: x % 2 != 0, numbers))
# print(odd_elements)
