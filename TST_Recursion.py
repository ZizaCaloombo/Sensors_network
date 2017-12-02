def TST(m = []):#Timetable Sensor Tree
    import copy
    m1 = copy.deepcopy(m)

    def TTS(z = 0, father = 0):     #Timetable Sensor Tree
        for i in range(z,len(m1)):
            if m1[z][i] == 1 and z!=i :
                blocked = TTS(i,z) #in the brunch return (True or False for block output signal)
                if blocked == True:                   
                   blockIN.update({father:father})
                    
            if m1[z][z] != 0 and i == len(m1)-1 and z != 0 : #если не конец массива,если не сама точка,если уже не НУЛЕВАЯ
                if father not in blockOUT and z not in blockIN: #если отец не заблокирован ,и если сама точка не заблокирована
                    m1[z][z] -= 1 #decrement sensor
                    blockIN.update({z:z}) # """блокировка текущего сенсора на прием"""
                    blockOUT.update({z:z}) #  """блокировка текущего сенсора на отдач"""
                    m1[father][father] +=1 #increment father sensor
                    road.append([z,father]) # add in actual way
                    blockIN.update({father:father}) #sensor lock for transmission         
                    blockOUT.update({father:father})
                    return True
    way = []  # all Timetable 
    
    while m1[0][0] != len(m1):   # пока не соберем данные со всех сенсоров
        road = []   # zeroing out actual way
        blockOUT = {}  # запрет на отдачу
        blockIN = {} # запрет на прием
        TTS()       #sensor unlock for transmission
        way.append(road) #Adding an actual path to the general
    return way #out general TimetableSensors

#testing graph
"""   
m = [[1,1,0,0,1],
     [1,1,2,2,0],
     [0,2,1,3,0],
     [0,2,3,1,3],
     [1,0,0,3,1]]

m = [[1, 1, 0, 0, 1, 0, 0, 0, 0, 0], 
     [1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
     [0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
     [0, 1, 1, 1, 0, 1, 0, 0, 0, 0],
     [1, 0, 0, 0, 1, 1, 0, 0, 1, 0],
     [0, 0, 0, 1, 1, 1, 1, 1, 0, 1],
     [0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
     [0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
     [0, 0, 0, 0, 1, 0, 0, 0, 1, 1],
     [0, 0, 0, 0, 0, 1, 0, 0, 1, 1]] 
"""
m = [[1,1,1,1,1],
     [1,1,1,1,1],
     [1,1,1,1,1],
     [1,1,1,1,1],
     [1,1,1,1,1]]
 