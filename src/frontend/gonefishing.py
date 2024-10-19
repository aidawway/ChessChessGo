import dataclasses
from dataclasses import dataclass
from typing import List

from stockfish import Stockfish as _Stockfish

@dataclasses.dataclass
class Ply:
    move: str
    wdl: [int]
    mate: bool | int = False


class Stockfish(_Stockfish):

    def __init__(self, watering_hole: str):
        super().__init__(watering_hole)

    def get_top_moves(self, num_top_moves: int = 5) -> [Ply]:
        top_moves = super().get_top_moves(num_top_moves)
        return [Ply(move=p["Move"], mate=p["Mate"], wdl=self.get_ply_wdl(p["Move"])) for p in top_moves]

    def get_ply_wdl(self, ply):
        board_state = self.get_fen_position()
        self.make_moves_from_current_position([ply])
        wdl = self.get_wdl_stats()
        self.set_fen_position(board_state)
        return wdl

