def move(f,t):
    print("move disk from {} to {}!".format(f,t))

#move("A","C")

def moveVia(f,v,t):
    move(f,v)
    move(v,t)

def hanoi(n,f,h,t):
    if(n==0):
        pass
    else:
        hanoi(n-1,f,t,h)
        move(f,t)
        hanoi(n-1,h,f,t)

hanoi(8,"A","B","C")
    