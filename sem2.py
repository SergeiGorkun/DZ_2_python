# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр
# N = input('Введите число: ')
# N2 = str(N)
# N2 = N2.replace('.', '')
# lst_str = list(N2)
# number = map(int, lst_str)
# sum = sum(number)
# print(sum)

# 2. Задайте список из n чисел последовательности (1 + 1/n)**n и выведите на экран их сумму

n = int(input('Введите число n: '))
list_n = [round((1+1/i)**i, 3) for i in range (1, n+1)]
print(f'Для n = {n} : {list_n}/n Сумма: {round(sum(list_n), 3)}')


# 3. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N
# N = int(input('Введите число: '))
# print('Пусть N = ' , N, ', тогда: ')
# print('[ 1 ]')
# proiz = 1
# for i in range(1, N):
#     proiz = proiz * (i+1)
#     print('[',proiz,']')

# 4. Реализуйте алгоритм перемешивания списка
# import random 

# list_A = [12, 92, 43, 59, 2145] 
# print('Список изначальный: ', list_A)

# random.shuffle(list_A) 
# print('Список измененный: ', list_A)




# import random
# list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# newlist = []
# list_length = len(list)
# for i in range(list_length):
#         index_aleatory = random.randint(0, list_length - 1)
#         temp = list[i]
#         list[i] = list[index_aleatory]
#         list[index_aleatory] = temp
# newlist = mix_list(list)
# print("Начальный список: ", list)
# print("Итоговый список: ", newlist)

# эту задачу так и не смог решить...что делать надо знаю...тут только через функцию наверное можно решить...