#1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# list = [2, 3, 5, 9, 3]
# result = 0
# for i in range ((len(list)-1)):
#     if i % 2 != 0:
#         result = result + list[i]
# print(result)

#2.Напишите программу, которая найдёт произведение пар чисел списка. 
#Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# list = (2, 3, 5, 9, 3)
# for i in range ((len(list)+1)//2):
#     a=list[i]*list[len(list)-1-i]
#     print(a)

#3. Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# my_list = [1.1, 1.2, 3.1, 5, 10.01]
# min = 1
# max = 0
# for i in my_list:
#     if (i - int(i)) <= min:
#         min = i - int(i)
#     if (i - int(i)) >= max:
#         max = i - int(i)  
# print(max-min)

#4.Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# a = int(input("Введите число: "))
# res = ""
# while a != 0:
#     res = str(a % 2) + res
#     a = a//2
# print (res)
