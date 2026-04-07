import tkinter as tk

# Create the board
board = [' ' for _ in range(9)]
piece_history = {'X': [], 'O': []}
current_player = 'X'
game_over = False
buttons = []

def count_pieces(player):
    return board.count(player)

def remove_oldest_piece(player):
    if piece_history[player]:
        oldest = piece_history[player].pop(0)
        board[oldest] = ' '

def update_buttons():
    for i, button in enumerate(buttons):
        button.config(text=board[i])
        if board[i] == 'X':
            button.config(fg='red')
        elif board[i] == 'O':
            button.config(fg='green')
        else:
            button.config(fg='black')
            button.config(bg='#fafcff')

def is_board_full():
    return ' ' not in board

def is_winner(player):
    return (
        (board[0] == player and board[1] == player and board[2] == player) or
        (board[3] == player and board[4] == player and board[5] == player) or
        (board[6] == player and board[7] == player and board[8] == player) or
        (board[0] == player and board[3] == player and board[6] == player) or
        (board[1] == player and board[4] == player and board[7] == player) or
        (board[2] == player and board[5] == player and board[8] == player) or
        (board[0] == player and board[4] == player and board[8] == player) or
        (board[2] == player and board[4] == player and board[6] == player)
    )

def winning_positions(player):
    lines = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6),
    ]
    for a, b, c in lines:
        if board[a] == board[b] == board[c] == player:
            return [a, b, c]
    return []

def make_move(player, position):
    if board[position] != ' ':
        return False
    if count_pieces(player) >= 3:
        remove_oldest_piece(player)
    board[position] = player
    piece_history[player].append(position)
    return True

def on_button_click(position):
    global current_player, game_over
    if game_over:
        return
    if not make_move(current_player, position):
        return
    update_buttons()
    if is_winner(current_player):
        status_label.config(text=f"Player {current_player} wins!")
        for idx in winning_positions(current_player):
            buttons[idx].config(bg='lightgreen')
        game_over = True
        return
    if is_board_full():
        status_label.config(text="It's a tie!")
        game_over = True
        return
    current_player = 'O' if current_player == 'X' else 'X'
    status_label.config(text=f"Player {current_player}'s turn")

def reset_game():
    global board, piece_history, current_player, game_over
    board = [' ' for _ in range(9)]
    piece_history = {'X': [], 'O': []}
    current_player = 'X'
    game_over = False
    update_buttons()
    for button in buttons:
        button.config(bg='#fafcff')
    status_label.config(text=f"Player {current_player}'s turn")

root = tk.Tk()
root.title('Tic Tac Toe')
root.geometry('650x800')
root.resizable(False, False)
root.configure(bg='#1f1f2e')
frame = tk.Frame(root, padx=16, pady=16, bg='#252740')
frame.pack(padx=12, pady=12, fill='both', expand=True)

for i in range(3):
    frame.columnconfigure(i, weight=1)
    frame.rowconfigure(i + 3, weight=1)

title_label = tk.Label(frame, text='Tic Tac Toe', font=("Arial", 20, 'bold'), fg='#ffffff', bg='#252740')
title_label.grid(row=0, column=0, columnspan=3, pady=(0, 4))
status_label = tk.Label(frame, text=f"Player {current_player}'s turn", font=("Arial", 14), fg='#a0c4ff', bg='#252740')
status_label.grid(row=1, column=0, columnspan=3, pady=(0, 10))

info_label = tk.Label(frame, text='Mỗi người đánh 3 quân cho đến khi thắng.', font=("Arial", 10), fg='#cfd8ff', bg='#252740')
info_label.grid(row=2, column=0, columnspan=3, pady=(0, 14))

for index in range(9):
    button = tk.Button(
        frame,
        text=' ',
        width=10,
        height=5,
        font=("Arial", 26, 'bold'),
        bg='#fafcff',
        activebackground='#dfe7ff',
        command=lambda index=index: on_button_click(index)
    )
    button.grid(row=3 + index // 3, column=index % 3, padx=10, pady=8, sticky='nsew')
    buttons.append(button)

reset_button = tk.Button(frame, text='Reset', command=reset_game, bg='#4f5d75', fg='white', activebackground='#647c9b', relief='raised', bd=2)
reset_button.grid(row=6, column=0, columnspan=3, pady=(25, 0))

root.mainloop()
