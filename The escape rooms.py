# Escape Room Sequence
from random import randint
print ("The Escape Room Sequence")
fealing_brave = True
score=0
while fealing_brave:
    ghost_door = randint(1, 3)
    ghost_door = randint(1, 3)
    print ("3 doors ahead...")
    print (" you have only one escape...")
    print (" if you chose wrong,.. you will DIE")
    door = input ("1, 2, or 3?")
    door_num=int(door)
    if door_num == ghost_door:
        print (" GHOST ")
    feeling_brave = False
else:
        print ("NO GHOST, YOUR SAFE")
        print ("NEXT DOOR")
        score = score + 1
if score == 2:
        print ( "You escaped the sequence!")
        print ("congradulations, You Win!!!")
    
        
