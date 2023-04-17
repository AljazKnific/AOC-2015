import collections
import numpy
f = open("Input.txt", "r")
arr = numpy.zeros((1000, 1000))

def first():
    
    while 1:
        line = f.readline()
        
        if not line:
            break
        
        inst = line.split(' ')
        x = 2
        
        if inst[0] == 'toggle':
            x = 1
        start = inst[x].split(',')
        end = inst[x + 2].split(',')
        print(int(start[1]))
        print(end)
        
        
        if 'on' == inst[1]:
            arr[int(start[0]):int(end[0])+ 1][int(start[1]): int(end[1]) + 1] = 1
            
        elif 'off' == inst[1]:
            print('a')
            arr[int(start[0]):int(end[0])+ 1][int(start[1]): int(end[1]) + 1] = 0
            print(arr[int(start[0]):int(end[0]) + 1][int(start[1]) : int(end[1]) + 1])
            
            print(arr[int(start[0]):int(end[0]) + 1][int(start[1]) : int(end[1]) + 1])
        elif 'toggle' == inst[0]:
            for x in range(int(start[0]), int(end[0]) + 1):
                for y in range(int(start[1]), int(end[1]) + 1):
                    if arr[x][y] == 1:
                        arr[x][y] = 0
                    else:
                        arr[x][y] = 1
        
        
first()
print(numpy.count_nonzero(arr == 1))