# I realize there is a lot going on here but this is one of the more logicaly difficult problems we had to work on.
# this is not a script, rather a simple function. It is here to demonstrate the ability to follow a complex list of instructions and logically break it down step by step 
# to be understood by a computer program

'''Write a function move_knight which takes in a list coords_and_dirs, whose first element is a list, indicating the coordinates of the Knight's starting position, and whose second element is a four-character string, indicating where the Knight should move in one turn.

A Knight must move exactly three spaces, either two spaces in a vertical direction and one in a horizontal direction, or one space in a vertical direction and two spaces in a horizontal direction.

Assume the string at the first index of coords_and_dirs will always be formatted such that:

  The first character is either 'U' or 'D' (where 'U' is up and 'D' is down) and represents the file (vertical direction)

  The second character is either '1' or '2' and represents how many spaces in the vertical direction the Knight will travel
  
  The third character is either 'L' or 'R' (where 'L' is left and 'R' is right) and represents the rank (horizontal direction)
  
  The fourth character is either '1' or '2' and represents how many spaces in the horizontal direction the Knight will travel

For example: "U1L2" would read as "up one space, left two spaces".



The chess board is a grid, with each space identified as [file, rank]:

  [0, 7] --> .    .    .    .    .    .    .    . <-- [7, 7]

             .    .    .    .    .    .    .    .

             .    .    .    .    .    .    .    .

             .    .    .    .    .    .    .    .

             .    .    .    .    .    .    .    .

             .    .    .    .    .    .    .    .

             .    .    .    .    .    .    .    . 

  [0, 0] --> .    .    .    .    .    .    .    . <-- [7, 0]

For example: The starting coordinates [7, 7] would represent the knight starting in the upper right corner of the chess board.



If the given directions would be an illegal move, or if the move would cause the Knight to fall off the board, return the string "Illegal Move - Horsey Down!"

Else, the function should return a string with updated file and rank, formatted as such: "The knight has moved to [file, rank]."
'''

def move_knight(coords_and_dirs:list):
  # defines the function and it's parameter as explained above
  moves = coords_and_dirs[1]
  # takes the 2nd argument in the parameter and saves it as a variable "moves" 
  coords = coords_and_dirs[0]
  # takes the first argument in the parameter and saves it as a variable "coords"
  new_coords =[]
  # creats an empty list called new_coords to be used later
  if int(moves[1]) == 0 or int(moves[3]) == 0:
    # converts string entered that respresents the knights move to an integer and checks if they are equal to zero
    return("Illegal Move - Horsey Down!")
  #if the above statement is true this line tell the function to return a string explaining that the knight can not make that move
  if int(moves[1]) + int(moves[3]) != 3: # THis is genious - Ned
    # checks to make sure that the sum of the moves made is equal to 3 (knights move 3 spaces on a chess board)
    return("Illegal Move - Horsey Down!") 
    # returns a statement telling you the move was illegal if the total spaces moved does not equal 3
  if moves[0] == "U" and moves[2] == "R":
    # if statement checking the direction of the moves
    if int(moves[1]) + int(moves[3]) == 3:
      new_coords.append(int(moves[1]) + coords[1])
      new_coords.append(int(moves[3]) + coords[0]) 
      if new_coords[0] > 7 or new_coords[0] < 0:
        return "Illegal Move - Horsey Down!"
      elif new_coords[1] >7 or new_coords[1] <0:
        return "Illegal Move - Horsey Down!"
      else:
        return "The knight has moved to " + str(new_coords) + "."
      #lines 68 - 76 determine if the move made places the knight in a valid spot on the board, if it doesn't it returns an error statement, if it does it returns the knights new coordinates on the board
  if moves[0] == "U" and moves[2] == "L":
    # if statement checking the direction of the moves
    if int(moves[1]) + int(moves[3]) == 3:
      new_coords.append(coords[0] - int(moves[3]))
      new_coords.append(int(moves[1]) + coords[1])
      if new_coords[0] > 7 or new_coords[0] < 0:
        return "Illegal Move - Horsey Down!"
      elif new_coords[1] >7 or new_coords[1] <0:
        return "Illegal Move - Horsey Down!"
      else:
        return "The knight has moved to " + str(new_coords) + "." 
      #lines 80-88 determine if the move made places the knight in a valid spot on the board, if it doesn't it returns an error statement, if it does it returns the knights new coordinates on the board
  if moves[0] == "D" and moves[2] == "R":
    # if statement checking the direction of the moves
    if int(moves[1]) + int(moves[3]) == 3:
      new_coords.append(int(moves[3]) + coords[0])
      new_coords.append(coords[1] - int(moves[1]))
      if new_coords[0] > 7 or new_coords[0] < 0:
        return "Illegal Move - Horsey Down!"
      elif new_coords[1] >7 or new_coords[1] <0:
        return "Illegal Move - Horsey Down!"
      else:
        return "The knight has moved to " + str(new_coords) + "."   
      #lines 91-99 determine if the move made places the knight in a valid spot on the board, if it doesn't it returns an error statement, if it does it returns the knights new coordinates on the board
  if moves[0] == "D" and moves[2] == "L":
    # if statement checking the direction of the moves
    if int(moves[1]) + int(moves[3]) == 3:
      new_coords.append(coords[1] - int(moves[1]))
      new_coords.append(coords[0] - int(moves[3])) 
      if new_coords[0] > 7 or new_coords[0] < 0:
        return "Illegal Move - Horsey Down!"
      elif new_coords[1] >7 or new_coords[1] <0:
        return "Illegal Move - Horsey Down!"
      else:
        return "The knight has moved to " + str(new_coords) + "." 
      #lines 102-110 determine if the move made places the knight in a valid spot on the board, if it doesn't it returns an error statement, if it does it returns the knights new coordinates on the board
print(move_knight([[4,5], "D1L2"]))
#print statement to call and test the function
