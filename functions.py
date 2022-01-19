
# current position
position = 0

# implement function for increasing player position
def move_player():
    global position # access the variable outside the function
    position += 1
    print(position)
    
# call the function
move_player()

position = 0

# implement function to take in a parameters
def move_player(position, by_amount):
    position += by_amount
    # produce an output from the function
    return position
   
# pass values to the function 
position = move_player(position, 5)
position = move_player(position, 2)
print(position)