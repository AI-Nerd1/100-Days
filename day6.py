print("\n                 ==========Day 6==========")
print("\n                 ==========While Loop==========")


def print_function():
    print("Hello world")
    print("This is a sample function")

print_function()

print("\n                 ==========Reeborg==========")
time = 9
while 1:
    if time <= 1:
        done()
    for x in range(time):
        move()        
    turn_left()
    for x in range(time):
        move()
    turn_left()
    time-=1


def full_move():
    for x in range(9):
        move()
def turn_right():
        turn_left()
        turn_left()
        turn_left()
for x in range(4):
    full_move()
    turn_left()
    move()
    turn_left()

print("\n                 ==========Hurdles race==========")
def turn_right():
        turn_left()
        turn_left()
        turn_left()

def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
move()
for x in range(5):
    jump()
    move()
jump()
done()

print("\n                 ==========Hurdles race2==========")
def turn_right():
        turn_left()
        turn_left()
        turn_left()

def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
move()
for x in range(6):
    jump()
    move()
    if at_goal():
        done()

while not at_goal():
    jump()
done()

print("\n                 ==========Hurdles race3==========")
while not at_goal():
    if front_is_clear():
        move()
    if wall_in_front():
        jump()
done()

print("\n                 ==========Hurdles race4==========")
def turn_right():
        turn_left()
        turn_left()
        turn_left()

def jump():
    #move()
    turn_left()
    move()
    turn_right()
    while wall_in_front():
        turn_left()
        move()
        turn_right()
    if front_is_clear():
        move()
        turn_right()
        while front_is_clear():
            move()
    turn_left()
    #move()
    #turn_left()
    
#move()
#for x in range(6):
#    jump()
#    move()
#    if at_goal():
#        done()


while not at_goal():
    if front_is_clear():
        move()
    if wall_in_front():
        jump()
done()
print("\n                 ==========Maze==========")   
def turn_right():
        turn_left()
        turn_left()
        turn_left()

while not at_goal():
    while front_is_clear():
        move()
    if wall_in_front():
        if right_is_clear():
            turn_right()
        else:
            turn_left()
    #if wall_on_right():
        #turn_left()
        
done()

def turn_right():
        turn_left()
        turn_left()
        turn_left()

while 1:
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
        
done()
    