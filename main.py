import chess
import chess.engine
import chess.svg
from src_code.draw.utils import draw_board
from config.mu_zero_config import MuZeroConfig


def control():

    config = MuZeroConfig()

    # engine = chess.engine.SimpleEngine.popen_uci('/usr/games/stockfish')

    board = chess.Board()
    draw_board(board, display=True)



    print(board)

if __name__ == '__main__':
    control()
