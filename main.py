import chess
import chess.engine
import chess.svg
from src_code.draw.utils import draw_board



def control():



    board = chess.Board()
    draw_board(board, display=True)

    print(board)


if __name__ == '__main__':
    control()
