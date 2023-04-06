from numpy import False_, True_


f = open("Input.txt", "r")

class Coordinates:
    def __init__(self,x,y) -> None:
        self.x = x
        self.y = y

HashSet = set()
x = 0
y = 0
beg = Coordinates(x,y)
HashSet.add(beg)
bool = False

while 1:
    bool = False
    char = f.read(1)
    
    if not char:
        break
    
   # if x == 0 and char == '<':
    #    print("X cannot be negative value")
     #   break
    #if y == 0 and char == 'v':
    #    print("Y cannot be negative value")
    #    break
    
    if char == 'v':
        y -= 1
    elif char == '<':
        x -= 1
    elif char == '>':
        x += 1
    elif char == '^':
        y += 1
    else:
        print("X")
    
        
    newCoor = Coordinates(x,y)
    for item in HashSet:
        if item.x == newCoor.x and item.y == newCoor.y:
            bool = True
            break
    if not bool:
        HashSet.add(newCoor)

print(len(HashSet))
    
    