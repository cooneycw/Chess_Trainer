import chess
import random


class ChessEnv:
    def __init__(self):
        self.board = chess.Board()
        self.current_player = 1

    def reset(self):
        self.board = chess.Board()
        self.current_player = 1

    def step(self, action):
        self.board.push(action)
        reward = random.random() # Placeholder reward
        done = self.board.is_game_over()
        self.current_player = -self.current_player
        return self.observation(), reward, done

    def legal_moves(self):
        return list(self.board.legal_moves)

    def observation(self):
        return self.board
