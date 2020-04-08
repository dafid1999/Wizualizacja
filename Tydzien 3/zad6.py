import math
def promien(x = 2,y = 2,a = 2,b = 2):
    return math.sqrt((x-a)**2+(y-b)**2)

print(promien())
print(promien(10,9))
print(promien(a=9, b=5))