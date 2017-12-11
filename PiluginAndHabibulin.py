#def TST(m1):
#   import copy
#  m = copy.deepcopy(m1)
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
        #кароч бля, надо наверх
        return connect[wide.index(min(wide))]
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
  #  return main(m)

m = [[1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0],
     [0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
     [0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
     [0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0],
     [1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0],
     [1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0],
     [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0],
     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1]]
print(main(m))

"""
def conH():
    for i1 in range(len(ring)):
       j1 in range(len(ring[i1])):    
           if ring[i1][j1] != j and ring in connect:"""
'''
if __name__ == '__main__':
    from graph_gen import graph_generator, tree_generator, grid_generator
    import validate  # Будет добавлено после тестирования корректности работы валидатора.

    # while True:
    #     try:
    #         method = int(input(Выберите метод генерации
    #         1 - дерево;
    #         2 - решетка;
    #         3 - случайный граф
    #
    #         ))
    #         if method in [1, 2, 3]:
    #             if method == 1:
    #                 N = int(input('Введите число сенсоров в сети: '))
    #                 adjacency_matrix = tree_generator(N)
    #             elif method == 3:
    #                 N = int(input('Введите число сенсоров в сети: '))
    #                 adjacency_matrix = graph_generator(N)
    #             elif method == 2:
    #                 N = int(input('Введите длину стороны решетки: '))
    #                 if N % 2 == 0:
    #                     raise ValueError
    #                 else:
    #                     adjacency_matrix = grid_generator(N)
    #
    #         else:
    #             raise ValueError
    #     except ValueError:
    #         print('Вы ввели некоректное число, попробуйте снова!')

    import time

    start_time = time.time()
    adjacency_matrix = graph_generator(11)
    schedule = TST(adjacency_matrix)
    print('Is valid? {}'.format(validate.validateFunc(adjacency_matrix, schedule)))
    print("--- %s seconds ---" % (time.time() - start_time))
    print(schedule)
    print('Длина расписания равна {}'.format(len(schedule))) '''
