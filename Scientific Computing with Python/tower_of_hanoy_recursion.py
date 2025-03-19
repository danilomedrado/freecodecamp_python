#learn-recursion-by-solving-the-tower-of-hanoi-puzzle
#https://github.com/freeCodeCamp/freeCodeCamp/tree/main/curriculum/challenges/english/07-scientific-computing-with-python/learn-recursion-by-solving-the-tower-of-hanoi-puzzle
#The goal of the Tower of Hanoi is moving all the disks to the last rod. 
#To do that, you must follow three simple rules:

#You can move only top-most disks
#You can move only one disk at a time
#You cannot place larger disks on top of smaller ones

#In the Tower of Hanoi puzzle, you can identify the three rods according to their purpose:

#The first rod is the source, where all the disks are stacked on top of each other at the beginning of the game.
#The second rod is an auxiliary rod, and it helps in moving the disks to the target rod.
#The third rod is the target, where all the disks should be placed in order at the end of the game.

NUMBER_OF_DISKS = 5
#The Tower of Hanoi puzzle can be solved in 2n - 1 moves, where n is the number of disks.
number_of_moves = 2**NUMBER_OF_DISKS - 1
rods = {
    'A': list(range(NUMBER_OF_DISKS, 0, -1)),
    'B': [],
    'C': []
}

def make_allowed_move(rod1, rod2):    
    forward = False
    if not rods[rod2]:
        forward = True
    elif rods[rod1] and rods[rod1][-1] < rods[rod2][-1]:
        forward = True      
                
    if forward:
        print(f'Moving disk {rods[rod1][-1]} from {rod1} to {rod2}')
        rods[rod2].append(rods[rod1].pop())
    else:
        print(f'Moving disk {rods[rod2][-1]} from {rod2} to {rod1}')
        rods[rod1].append(rods[rod2].pop())
    
    # display our progress
    print(rods, '\n')

def move(n, source, auxiliary, target):
    # display starting configuration
    print(rods, '\n')
    for i in range(number_of_moves):
        remainder = (i + 1) % 3
        if remainder == 1:
            if n % 2 != 0:
                print(f'Move {i + 1} allowed between {source} and {target}')
                make_allowed_move(source, target)
            else:
                print(f'Move {i + 1} allowed between {source} and {auxiliary}')
                make_allowed_move(source, auxiliary)
        elif remainder == 2:
            if n % 2 != 0:
                print(f'Move {i + 1} allowed between {source} and {auxiliary}')
                make_allowed_move(source, auxiliary)
            else:
                print(f'Move {i + 1} allowed between {source} and {target}')
                make_allowed_move(source, target)
        elif remainder == 0:
            print(f'Move {i + 1} allowed between {auxiliary} and {target}')
            make_allowed_move(auxiliary, target)     

# initiate call from source A to target C with auxiliary B
move(NUMBER_OF_DISKS, 'A', 'B', 'C')

print('_________now the recursion__________')

A = list(range(NUMBER_OF_DISKS, 0, -1))
B = []
C = []

def move_rec(n, source, auxiliary, target):
    if n <= 0:
        return
    # move n - 1 disks from source to auxiliary, so they are out of the way
    move(n - 1, source, target, auxiliary)
    
    # move the nth disk from source to target
    target.append(source.pop())
    
    # display our progress
    print(A, B, C, '\n')
    
    # move the n - 1 disks that we left on auxiliary onto target
    move(n - 1,  auxiliary, source, target)
              
# initiate call from source A to target C with auxiliary B
move_rec(NUMBER_OF_DISKS, A, B, C)