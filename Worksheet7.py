#Question1 Tic Tac Toe

board = [' '] * 9

def print_board():
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("-----------")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("-----------")
    print(f" {board[6]} | {board[7]} | {board[8]} ")

def check_win(p):
    win = [(0,1,2),(3,4,5),(6,7,8),
           (0,3,6),(1,4,7),(2,5,8),
           (0,4,8),(2,4,6)]
    for i in win:
        if board[i[0]] == board[i[1]] == board[i[2]] == p:
            return True
    return False

def check_tie():
    return ' ' not in board

player = 'X'

while True:
    print_board()
    pos = int(input(f"Player {player}, enter position (1-9): ")) - 1
    if board[pos] == ' ':
        board[pos] = player
        if check_win(player):
            print_board()
            print(player, "wins")
            break
        if check_tie():
            print_board()
            print("Tie")
            break
        player = 'O' if player == 'X' else 'X'

#Question2 To-Do List

tasks = []

def add_task():
    tasks.append(input("Enter task: "))

def view_tasks():
    for i,t in enumerate(tasks):
        print(i, t)

def delete_task():
    i = int(input("Enter index: "))
    if 0 <= i < len(tasks):
        tasks.pop(i)

while True:
    c = input("1.Add 2.View 3.Delete 4.Exit: ")
    if c == '1':
        add_task()
    elif c == '2':
        view_tasks()
    elif c == '3':
        delete_task()
    else:
        break