from tc import main


def test_win_check():
    # checking if player 2 won the match or not, since board is empty it should return false
    assert main.win_check(2) == False
    #assert main.win_check(1) == False

def test_available_spots():
    # checking if the board spot is empty
    assert main.available_spots(1,1) == 1


"""def test_is_board_full():
    # Filling some blocks of the TicTacToe board and checking if board is full or not
    for row in range(main.board_rows):
        for col in range(main.board_cols-1):
            main.board[row][col] = 1

    assert main.is_board_full() ==  False"""

