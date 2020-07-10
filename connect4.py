#!/usr/bin/env python

import argparse
import numpy as np
import sys


class Board(object):
    def __init__(self, dim=(6, 7)):
        self._board = np.zeros(dim, dtype=int)

    """Check winner."""
    def check(self):
        winner = None

        for i, _ in enumerate(self._board):
            for j, _ in enumerate(self._board[i]):
                pass  # TODO

        return winner

    """Do move."""
    def move(self, player, col):
        col -= 1

        # TODO: check bounds

        for n, e in reversed(list(enumerate(self._board))):
            if self._board[n, col] == 0:
                self._board[n, col] = player + 1
                break

    """Print board."""
    def show(self):
        print(self._board)


if __name__ == '__main__':
    # parser = argparse.ArgumentParser()
    # parser.add_argument('--width', type=int)
    # parser.add_argument('--height', type=int)

    board = Board()
    player = 1

    while True:
        line = sys.stdin.readline()

        if line == '':
            break

        try:
            board.move(player, int(line))
        except Exception as e:  # noqa
            pass  # TODO

        board.show()

        if board.check() is not None:
            break

        player ^= 1
