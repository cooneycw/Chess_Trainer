import chess
import chess.engine
import chess.svg
import tensorflow as tf
import numpy as np
from tensorflow import keras
from src_code.frameworks.frameworks import MuZeroConfig, make_chess_config
from src_code.selfplay.selfplay import run_selfplay
from src_code.storage.storage import SharedStorage, ReplayBuffer
from src_code.draw.utils import draw_board


def muzero(config: MuZeroConfig):
    storage = SharedStorage()
    replay_buffer = ReplayBuffer(config)

    for _ in range(config.num_actors):
        result = run_selfplay(config, storage, replay_buffer)

    train_network(config, storage, replay_buffer)

    return storage.latest_network()


def control():
    mz = make_chess_config(num_actors=1)
    latest = muzero(mz)
    draw_board(board, display=True)


    print(board)


if __name__ == '__main__':
    control()
