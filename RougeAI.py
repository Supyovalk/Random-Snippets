#This Program Solves A Generalized version of the TedEd Rogue AI Riddle.
#0-unplayable,1-winner,2-loser,3-undecided
def is_winner(floor,moves):
    if(floor<min(moves)):
        return 0
    for move in moves:
        if is_winner(floor-move,moves)==2 or floor-move==0:
            return 1
    return 2
def print_floor_state(floor,moves):
   print("floor %d-%d" % (floor,is_winner(floor,moves)))
def total_floor_state(max_floor,moves):
    for floor in range(max_floor,0,-1):
         print_floor_state(floor,moves)
def min(moves):
    min=moves[0]
    for i in moves:
        if(i<min):
            min=i
    return min
total_floor_state(25,[1,3,4])