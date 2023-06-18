def turn_right():
    turn_left()
    turn_left()
    turn_left()

turn_count = 0
while not at_goal():
    # If we are just ran a full circle
    # then try to move to the front or if
    # that's not possible then turn left
    if right_is_clear() and turn_count < 4:
            turn_right()
            move()
            turn_count += 1
    elif front_is_clear():
        move()
        turn_count = 0
    else:
        turn_left()
        # Don't reset the turn count if we 
        # just ran a full loop, until we are
        # in the clear
        if turn_count < 4:
            turn_count = 0
