import time
import numpy as np
import matplotlib.pyplot as plt

from graph_gen import graph_generator, tree_generator, grid_generator
from main import TST, rasp_create
import validate  # Будет добавлено после тестирования корректности работы валидатора.

# while True:
#     try:
#         method = int(input('''Выберите метод генерации
#         1 - дерево;
#         2 - решетка;
#         3 - случайный граф
#
#         '''))
#         if method in [1, 2, 3]:
#             if method == 1:
#                 N = int(input('Введите число сенсоров в сети: '))
#                 adjacency_matrix = tree_generator(N)
#             elif method == 3:
#                 N = int(input('Введите число сенсоров в сети: '))
#                 adjacency_matrix = graph_generator(N)
#             elif method == 2:
#                 N = int(input('Введите длину стороны решетки (нечет.): '))
#                 if N % 2 == 0:
#                     raise ValueError
#                 else:
#                     adjacency_matrix = grid_generator(N)
#             break
#         else:
#             raise ValueError
#     except ValueError:
#         print('Вы ввели некоректное число, попробуйте снова!')

exec_time = time.clock()    # Начало замера выполнения программы

algo_creator_list = [
    'Пилюгин',
    'Сергеев'
]
# Массив для расчета и хранения результатов
n = 2  # Количество алгоритмов
m = 10  # Макс. размер тестового дерева (без учёта увеличивающего коэффициента)

valid = [0 for _ in range(n)]               # Массив проверок на работоспоссобность алгоритма
RaspLenData = [[0] * m for i in range(n)]
TimeExecData = [[0] * m for i in range(n)]

n2 = 25                                     # Число повторов генерации графа заданнного итерацией размера
tree_mult_coef = 10                         # Увеличивающий коэффициент количества сенсоров в графе

for i in range(1, m):  # Количество сенсоров
    for j in range(n2):  # n2 раз генерируем дерево с одинковым количеством сенсоров
        input_tree = graph_generator(i*tree_mult_coef)  # Генерация дерева c i*tree_mult_coef вершинами
        k = 0

        # Алгоритм Пилюгина
        func_exec_time = time.clock()
        schedule = TST(input_tree)
        RaspLenData[k][i] += len(schedule)
        TimeExecData[k][i] += time.clock() - func_exec_time
        try:
            validate.validateFunc(input_tree, schedule)
        except Exception:
            valid[k] += 1
        k += 1

        # Алгоритм Сергеева
        func_exec_time = time.clock()
        schedule = rasp_create(input_tree)
        RaspLenData[k][i] += len(schedule)
        TimeExecData[k][i] += time.clock() - func_exec_time
        try:
            validate.validateFunc(input_tree, schedule)
        except Exception:
            valid[k] += 1
        k += 1

RaspLenData = np.array(RaspLenData) / n2
TimeExecData = np.array(TimeExecData) / n2

print('Время выполнения теста равно ' + str(round(time.clock() - exec_time, 2)) + ' сек.')

x = [tree_mult_coef*i for i in range(m)]
plt.figure(1)
plt.xlabel('Количество сенсоров')
plt.ylabel('Длина расписания')
for i in range(n):
    plt.plot(x, RaspLenData[i],  label=algo_creator_list[i])
    plt.legend(loc='best')
plt.show()

plt.figure(2)
plt.xlabel('Количество сенсоров')
plt.ylabel('Среднее время выполнения, сек.')
for i in range(n):
    plt.plot(x, TimeExecData[i],  label=algo_creator_list[i])
    plt.legend(loc='best')
plt.show()

for i in range(n):
    print('Алгоритм '+str(i)+' построил расписание неправильно '+str(valid[i])+' раз.')
