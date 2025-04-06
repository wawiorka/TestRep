# 1
print("Задача 1.")
num1 = 20
num2 = 24
num3 = 6
print("Три целочисленные переменные:", num1, num2, num3)
res1 = num1 + num2 + num3
print("сумма:", res1)
res2 = num1 - num2 - num3
print("разность:", res2)
res3 = num1 * num2 * num3
print("произведение:", res3)
res4 = num1 - num2 + num3
print("отнять и прибавить:", res4)
res5 = (num1 * num2) / num3
print("произведение с делением:", res5)
res6 = (num1 + num2) % num3
print("остаток от деления произведения:", res6, end="\n\n")

# 2
print("Задача 2.")
cat_a = 4
cat_b = 5
print("дан прямоугольный треугольник с катетами:", cat_a, cat_b)
square = cat_a * cat_b / 2
print("площадь треугольника:", square)
gip = ((cat_a ** 2) + (cat_b ** 2)) ** (0.5)
print("гипотенуза треугольника:", gip, end="\n\n")


# 3
print("Задача 3.")
str3 = "test1 test2 test3 test4 test5"
# str3 = input("Введите строку с пробелами: ")  # убрала input
print("дана строка:", str3)
print("В строке", str3.count(" ") + 1, "слов(-о,-а)", end="\n\n")


# 4
print("Задача 4.")
str4 = "hhhabchghhh"
print("исходная строка:", str4)
time_str4 = str4[1:-1].replace("h", "H")
new_str4 = str4[0] + time_str4 + str4[-1]
print("новая строка", new_str4, end="\n\n")

# 5
print("Задача 5.")
str5 = "Homework"
print("для строки - ", str5, "- следующее решение:")
print(str5[2])  # m
print(str5[-2])  # r
print(str5[0:5])  # Homew
print(str5[:-2])  # Homewo
print(str5[::2])  # Hmwr
print(str5[1::2])  # oeok
print(str5[::-1])  # krowemoH
print(str5[::-2])  # koeo
print(len(str5), end="\n\n")  # 8

# 6
print("Задача 6.")
int6 = 125
print("последняя цифра числа", int6, "- это", int6 % 10, end="\n\n")

# 7
print("Задача 7.")
int7 = 230
print("число", int7, "состоит из", (int7 // 10) % 10, "десятков(-а)", end="\n\n")

# 8
print("Задача 8.")
int8 = 856
res8 = (int8 // 100) + ((int8 // 10) % 10) + (int8 % 10)
print("сумма цифр числа", int8, "равна", res8, end="\n\n")

# #camelCase
# fullName = "Add Daaa Noo"
#
# """snake_case
# full_name = "Add Daaa Noo"
# kebab-case
# full-name = "Add Daaa Noo"""""
#
# name = "Dfff Sdddf AAAA"
# print(name)
#
# name = "Dfff Sdddf"  # str (string)
# print(name)

# num1 = 5  # int (integer)
# # num2 = 10
# # num3 = num1 + num2
# # print(num3)
# #
# # balance = 125.225  # float
# #
# # is_adult = True # bool (boolean): True, False
# #
# # user = ["aa", "bb"] # list
# # print(type(num2))
#
# num1 = 10
# num2 = 4
#
# result = True
# print(result)
#
# result = num1 == num2  # falce
# print(result)
#
# result = num1 != num2  # true
# print(result)
#
# result = num1 > num2  # true
# print(result)
#
# result = num1 < num2  # false
# print(result)

# full_name = "Derty Tre"
# #   0    1    2    3    4    5    6    7    8                     - индексы
# # ['D', 'e', 'r', 't', 'y', ' ', 'T', 'r', 'e']
# print(full_name)
# print(full_name[8])
# # full_name[start:end] - невключительно!
# name = full_name[0:5]
# print(name)
# part1 = full_name[:5]
# print(part1)
# part2 = full_name[5:]
# print(part2)
# part3 = full_name[:]
# print(part3)
#
# # fulI_name[start:end:step]
# part4 = full_name[::1]
# print(part4)

# name = "Name"
# surname = "Surname"
# full_name = name + " " + surname
# # print(full_name)
# # str_length = len(name)
# # last_el = name[str_length - 1]
# # print(last_el)
# # print(len(name))
# # print(len(surname))
#
# print(name[0])
# print(name[-1])


# # методы
# full_name= "vaSya feDORov"
# print(full_name)
# print(full_name.upper())
# print(full_name.lower())
# print(full_name.capitalize())
# print(full_name.title())

# методы для валидации данных
# phone_num = "1256e3145rtt"
# print(phone_num.isdigit())
# print(phone_num)
# name = "Vasya124*"
# print(name.isalpha())
# print(name.isalnum())

# full_name = "Ann Siam"
# name = "Ann"
# print(full_name.find(name))
# surname = "Siam"
# print(full_name.find(surname))
# print(full_name.rfind(surname))  # поиск справа налево
# print(full_name.count(name))
# print(full_name.replace(name, "Aneshka"))
# new_full_name = full_name.replace(name, "Aneshka")
# print(new_full_name)
# print(full_name)

# full_name = "Ann Siam"
# print(full_name)
# print(id(full_name))
#
# full_name = "Ann"
# print(full_name)
# print(id(full_name))