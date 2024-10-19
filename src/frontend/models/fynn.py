from abc import ABC
from collections.abc import Iterable

from src.frontend.chess_notation import ChessPieces
from src.frontend.widgets.piece import Piece


class FynnIter(Iterable):
    height = 20

    def __init__(self, state: str):
        self.state = iter(state)
        self.row = 7
        self.col = 0

    def __iter__(self):
        return self

    def __next__(self):

        n = next(self.state)
        print(f"{n}: {self.row} {self.col}")
        if n.isdigit(): self.col += int(n); return self.__next__()
        if n == "/": self.col = 0; self.row -= 1; return self.__next__()
        if n.isspace(): raise StopIteration

        assert n.isalpha()
        self.col += 1
        style = "white" if n.isupper() else "black"
        match n.lower():
            case "p": p = Piece(style=style, name=ChessPieces.Pawn, height=FynnIter.height)
            case "b": p = Piece(style=style, name=ChessPieces.Bishop, height=FynnIter.height)
            case "n": p = Piece(style=style, name=ChessPieces.Knight, height=FynnIter.height)
            case "r": p = Piece(style=style, name=ChessPieces.Rook, height=FynnIter.height)
            case "q": p = Piece(style=style, name=ChessPieces.Queen, height=FynnIter.height)
            case "k": p = Piece(style=style, name=ChessPieces.King, height=FynnIter.height)
            case _:
                raise Exception("Unknown Piece")

        return p, self.row, self.col

