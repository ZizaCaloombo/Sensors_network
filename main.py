import numpy as np
import networkx as nx


def rasp_create(adj_matrix):
    """
    Функция для составления расписания передачи сообщений от передатчиков к Базовой Станции (БС) в случайно
    связанной сети.
    :param adj_matrix: Матрица смежности. лист листов с описанием связей графового представления системы.
    :return: результат в формате расписания: [фрейм]
    """
    result_way = []  # Список передач за фрейм
    trans_num = len(adj_matrix)  # Число передатчиков
    bs_buf = 0  # Количество сообщений на БС
    graph = nx.from_numpy_matrix(np.matrix(adj_matrix))
    trans_routes = nx.shortest_path(graph, 0)  # Список маршрутов
    routes_p_node = np.zeros((trans_num,), dtype=np.int)  # Число маршрутов через вершину
    for node in trans_routes:
        routes_p_node[trans_routes[node]] += 1
    sort_routes = routes_p_node.argsort()
    '''
    routes_p_node = np.zeros((trans_num,), dtype=np.int)
        trans_routes = [[] for _ in range(trans_num)]
        for i in range(trans_num):
            trans_routes[i] = nx.shortest_path(graph, 0, i)
            routes_p_node[trans_routes[i]] += 1
            routes_p_node[0] = 0
            for j in trans_routes[i]:
                for e_num in graph[j]:
                    graph[j][e_num]['weight'] += routes_p_node[j] * trans_num ** -2
                    graph[e_num][j]['weight'] += routes_p_node[j] * trans_num ** -2
    else:
    '''
    while bs_buf < trans_num - 1:  # Пока все заявки не попадут на БС,...
        cur_transmission = []  # Список передач за слот
        trans_lock = [False] * trans_num  # Список заблокированных для передачи передатчиков
        receive_lock = [False] * trans_num  # Список заблокированных для приёма  передатчиков

        # В цикле исключена возможность передачи сообщения из БС (т.к. начинаем с 1)
        # Проходимся по сенсорам, проверяем возможность передачи и передаём
        for i in sort_routes:  # range(1, trans_num): # Замена на порядок с приоритетами
            # Проверка возможности передачи сообщения
            if len(trans_routes[i]) > 1:
                source = trans_routes[i][-1]  # откуда передавать
                receive = trans_routes[i][-2]  # куда передавать

                # Проверка возможности передачи сообщения
                trans_allowed = True
                if trans_lock[source] or receive_lock[receive]:
                    trans_allowed = False
                if trans_allowed:
                    # Добавление новой передачи в слот
                    cur_transmission.append([source, receive])
                    # Блокировка на передачу ближайших передатчиков
                    for j, neighbor in enumerate(adj_matrix[source]):
                        if neighbor == 1 or j == source:
                            receive_lock[j] = True
                    for j, neighbor in enumerate(adj_matrix[receive]):
                        if neighbor == 1 or j == receive:
                            trans_lock[j] = True
                    trans_lock[receive] = True
                    trans_lock[source] = True
                    trans_routes[i].pop()
                    if len(trans_routes[i]) == 1:
                        bs_buf += 1
                    for k in range(1, trans_num):
                        if k != i and len(trans_routes[k]) > 1 and trans_routes[k][-1] == source \
                                and receive == trans_routes[k][-2]:
                            trans_routes[k].pop()
                            if len(trans_routes[k]) == 1:
                                bs_buf += 1
        result_way.append(cur_transmission)  # Добавления слота во фрейм
    return result_way  # , len(result_way)                          # Вывод результата в формате [фрейм], число_слотов


def show_graph(graph):
    """
    Функция для отображения графа
    :param graph: матрица смежности (лист листов) или объект графа из библиотеки networkX
    :return:
    """
    import matplotlib.pyplot as plt

    if type(graph) == list:
        graph = nx.from_numpy_matrix(np.matrix(graph))
    nx.draw_networkx(graph, with_labels=True)
    plt.show()


def TST(m1):
    import copy

    m = copy.deepcopy(m1)
    if m[0][0] == 0:
        for i in range(len(m)):
            m[i][i]=1#Костыль
    def connects(i,ring):
        connect = []
        for j in range(len(m[i])):
            if j != i and m[i][j] != 0 and INring(j,ring):
                connect.append(j)
        return connect

    def connectors(i,ring,i2):
    #    for i in range(len(m)): #пока вес листа != длинне массива-1
    #        connect.append([])
        connect = []
        for j in range(len(m[i])):
            if  m[i][j] != 0 and INring(j,ring) and i!=j:
                connect.append(j)
        for qwe in range(i2): #Костыль
            for qwa in ring[qwe+1]:#Костыль
                if qwa in connect:#Костыль
                    connect.remove(qwa)      #Костыль

        wide = []
        for j in range(len(connect)):
            q = 0
            for z in range(len(m[j])):
                if m[j][z] != 0:
                    q +=m[j][z]


            wide.append(q-1)
            #кароч  надо наверх
            return connect[wide.index(max(wide))]
    def INring(n,ring):
        for i in range(len(ring)):
            if n in ring[i]:
                return False
            else:
                return True
    '''
    m = [[1,0,1,0,1,1,0,1,0],
         [0,1,1,0,1,0,0,0,0],
         [1,1,1,1,0,0,0,0,0],
         [0,0,1,1,0,1,0,0,0],
         [1,1,0,0,1,0,1,0,0],
         [1,0,0,1,0,1,0,0,1],
         [0,0,0,0,1,0,1,1,0],
         [1,0,0,0,0,0,1,1,1],
         [0,0,0,0,0,1,0,1,1]
            ]
    '''

    #''''''''''''''''''''''''''''''''''''
    def foo(ring,m):
        z = 0
        while sum(len(ring[i]) for i in range(len(ring)))  != len(m):
            s = []
            s1 = []
            for i in ring[z]:
                s.extend(connects(i,ring))

            for i in s:
                if i not in s1:
                    s1.append(i)

            for i in range(len(ring)):
                for j in ring[i]:
                    for z1 in range(s1.count(j)):
                        s1.remove(j)
            z +=1
            ring.append(s1)
        #''''''''''''''''''''''''''''''''''''

        ring.reverse()

    # 8

    def check(n,j,block): #check(n,j,blockIN,blockOUT):
        #blockIN.update({j:j})
        #blockIN.update({n:n})
        #blockOUT.update({j:j})
        #blockOUT.update({n:n})
        block.update({j:j})
        block.update({n:n})
        for i in range(len(m)):
            if m[n][i] != 0:
                block.update({i:i}) #blockIN.update({m[n][i]:m[n][i]})
        for i in range(len(m)):
            if m[j][i] != 0:
                block.update({i:i}) #            blockIN.update({m[j][i]:m[j][i]})
    def main(m)   :

        ring = [[0]]

        foo(ring,m)
        way = []
        while m[0][0] != len(m):
        #    print(m[0][0])
            road = []
            block = {}
            #blockIN = {}
            #blockOUT = {}
            for i in range(len(ring)):
                for j in ring[i]:
                    if m[j][j] != 0 and j not in block:

                        n = connectors(j,ring,i)#random.choice(connectors(j)) #пока без приоретета даздраствует тупой рандом!!


                        if j!=n and j!=0  and n not in block: #if j!=n and j!=0 and j not in blockOUT and n not in blockIN:if j!=n and j!=0 and j not in blockOUT and n not in blockIN:
                            #m[j][j] -=1
                            m[n][n] +=m[j][j]
                            m[j][j] = 0
                            road.append((j,n))
                            check(n,j,block)#check(n,j,blockIN,blockOUT)

            way.append(road)
          #  print("я жив")
        return way
    return main(m)

if __name__ == '__main__':
    from graph_gen import graph_generator, tree_generator, grid_generator
    import validate  # Будет добавлено после тестирования корректности работы валидатора.

    while True:
        try:
            method = int(input('''Выберите метод генерации
            1 - дерево;
            2 - решетка;
            3 - случайный граф

            '''))
            if method in [1, 2, 3]:
                if method == 1:
                    N = int(input('Введите число сенсоров в сети: '))
                    adjacency_matrix = tree_generator(N)
                elif method == 3:
                    N = int(input('Введите число сенсоров в сети: '))
                    adjacency_matrix = graph_generator(N)
                elif method == 2:
                    N = int(input('Введите длину стороны решетки (нечет.): '))
                    if N % 2 == 0:
                        raise ValueError
                    else:
                        adjacency_matrix = grid_generator(N)
                break
            else:
                raise ValueError
        except ValueError:
            print('Вы ввели некоректное число, попробуйте снова!')

    import time

    #show_graph(adjacency_matrix)
    print('Algo_Sergeev')
    start_time = time.time()
    schedule2 = rasp_create(adjacency_matrix)
    print('Is valid? {}'.format(validate.validateFunc(adjacency_matrix, schedule2)))
    print("--- %s seconds ---" % (time.time() - start_time))
    print(schedule2)
    print('Длина расписания равна {}'.format(len(schedule2)))

    print('Algo_Pilugin')
    start_time = time.time()
    schedule = TST(adjacency_matrix)
    print('Is valid? {}'.format(validate.validateFunc(adjacency_matrix, schedule)))
    print("--- %s seconds ---" % (time.time() - start_time))
    print(schedule)
    print('Длина расписания равна {}'.format(len(schedule)))