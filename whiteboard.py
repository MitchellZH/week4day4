# An infinite number of shelves are arranged one above the other in a staggered fashion.
# The cat can jump either one or three shelves at a time: from shelf i to shelf i+1 or i+3 (the cat cannot climb on the shelf directly above its head), according to the illustration:
#                  ┌────────┐
#                  │-6------│
#                  └────────┘
# ┌────────┐
# │------5-│
# └────────┘  ┌─────► OK!
#             │    ┌────────┐
#             │    │-4------│
#             │    └────────┘
# ┌────────┐  │
# │------3-│  │
# BANG!────┘  ├─────► OK!
#   ▲  |\_/|  │    ┌────────┐
#   │ ("^-^)  │    │-2------│
#   │ )   (   │    └────────┘
# ┌─┴─┴───┴┬──┘
# │------1-│
# └────────┘
# Input
# Start and finish shelf numbers (always positive integers, finish no smaller than start)
# Task
# Find the minimum number of jumps to go from start to finish
# Example
# Start 1, finish 5, then answer is 2 (1 => 4 => 5 or 1 => 2 => 5)

def shelves(start, finish):
    count = 0
    for cat in range(start, finish):
        if finish - cat >= 3:
            cat += 3
            print(cat)
        else:
            cat += 1
            print(cat)
        count += 1
        
    return count

print(shelves(1,7))

def shelves(start, finish):
    #start at:
    # finish at:
    i = start
    count = 0
    while finish - i >= 3:
        i += 3
        count += 1
    while finish - i > 0:
        i += 1
        count +=1
    return count

print(shelves(1,7))