import math
def direction_change(x1,y1,x2,y2,direction):
    global no_turn
    if x1==x2 or y1==y2:
        if y1==y2 and x1<x2 and direction !='E':
            no_turn+=5
            direction='W'
        else:
            pass
        if x1==x2 and y1<y2 and direction !='N':
            no_turn+=5
            direction='S'
        else:
            pass
    else:
        if x1<x2 and direction!='E':
            no_turn+= 5
            direction='W'
        if x1>x2 and direction !='W':
            no_turn+= 5
            direction='E'
        if y1<y2 and direction !='N':
            no_turn+= 5
            direction='S'
        if y1>y2 and direction !='S':
            no_turn+= 5
            direction='N'

def shortest_distance(x1,y1,x2,y2):
    global no_move
    dist=math.fabs(x1-x2)+math.fabs(y1-y2)
    no_move=dist*move

no_turn=0
no_move=0
Max_unit=200
turn=5
move=10
x1=int(input("x1 cordinate: "))
y1=int(input("y1 cordinate: "))
direction=input("initial direction of G-MAN (North = N, south = S,weast = W, East = E): ")
x2=int(input("enter x2 destination cordinate: "))
y2=int(input("enter y2 destination cordinate: "))
direction_change(x1,y1,x2,y2,direction)
shortest_distance(x1,y1,x2,y2)
add=no_move+no_turn
remaining=Max_unit-add
print("REMAINING_POWER_QUANTITY :",remaining)
