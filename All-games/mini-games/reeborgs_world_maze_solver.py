# this program is referred from https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Newspaper%200&url=worlds%2Ftutorial_en%2Fnewspaper0.json

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
while not at_goal():
    if wall_in_front() and wall_on_right():
        turn_left()
        if wall_in_front():
            turn_left()
    elif wall_in_front() and not wall_on_right():
        turn_right()
    elif not wall_in_front() and wall_on_right():
        move()
        turn_left()
        if wall_in_front():
            turn_right()
    else:
        move()
        
