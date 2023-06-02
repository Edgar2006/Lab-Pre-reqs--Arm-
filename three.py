print("0 1", end=" ")
a = 1
b = 2
c = b
while(True):
    print(a + b, end=" ")
    b += a 
    a = c
    c = b