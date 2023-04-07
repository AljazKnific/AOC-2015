f = open("Input.txt", "r")

def vowels(a) -> bool:
    vow = {'a', 'e', 'i', 'o', 'u'}
    
    return a in vow

def dup(a,b) -> bool:    
    return a == b

def naughty(a,b)->bool:
    if a == 'a' and b == 'b':
        return True
    if a == 'c' and b == 'd':
        return True
    if a == 'p' and b == 'q':
        return True
    if a == 'x' and b == 'y':
        return True
    return False

niceCounter = 0

while 1:
    line = f.readline()
    
    if not line:
        break
    
    vowCond = 0
    dupCond = False
    forr = True
        
    for i in range(0, len(line)):
        #print(line[i])
        if vowels(line[i]):
            #print("vow")
            vowCond +=1
        if i != len(line) - 1:
            if dup(line[i], line[i+1]):
                #print("dup")
                dupCond = True
            if naughty(line[i], line[i+1]):
                #print("naughty")
                forr = False
                
    if vowCond == 3 and dupCond and forr:
        niceCounter += 1
        
print(niceCounter)
        
        