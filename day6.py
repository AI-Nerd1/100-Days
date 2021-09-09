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