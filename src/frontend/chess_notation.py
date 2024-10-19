from enum import Enum


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


class ChessPieces(Enum):
    Bishop = "bishop"
    King = "king"
    Knight = "knight"
    Pawn = "pawn"
    Queen = "queen"
    Rook = "rook"

class ChessPosition(Enum):
    A1 = Point(0, 7)
    A2 = Point(0, 6)
    A3 = Point(0, 5)
    A4 = Point(0, 4)
    A5 = Point(0, 3)
    A6 = Point(0, 2)
    A7 = Point(0, 1)
    A8 = Point(0, 0)

    B1 = Point(1, 7)
    B2 = Point(1, 6)
    B3 = Point(1, 5)
    B4 = Point(1, 4)
    B5 = Point(1, 3)
    B6 = Point(1, 2)
    B7 = Point(1, 1)
    B8 = Point(1, 0)

    C1 = Point(2, 7)
    C2 = Point(2, 6)
    C3 = Point(2, 5)
    C4 = Point(2, 4)
    C5 = Point(2, 3)
    C6 = Point(2, 2)
    C7 = Point(2, 1)
    C8 = Point(2, 0)

    D1 = Point(3, 7)
    D2 = Point(3, 6)
    D3 = Point(3, 5)
    D4 = Point(3, 4)
    D5 = Point(3, 3)
    D6 = Point(3, 2)
    D7 = Point(3, 1)
    D8 = Point(3, 0)

    E1 = Point(4, 7)
    E2 = Point(4, 6)
    E3 = Point(4, 5)
    E4 = Point(4, 4)
    E5 = Point(4, 3)
    E6 = Point(4, 2)
    E7 = Point(4, 1)
    E8 = Point(4, 0)

    F1 = Point(5, 7)
    F2 = Point(5, 6)
    F3 = Point(5, 5)
    F4 = Point(5, 4)
    F5 = Point(5, 3)
    F6 = Point(5, 2)
    F7 = Point(5, 1)
    F8 = Point(5, 0)

    G1 = Point(6, 7)
    G2 = Point(6, 6)
    G3 = Point(6, 5)
    G4 = Point(6, 4)
    G5 = Point(6, 3)
    G6 = Point(6, 2)
    G7 = Point(6, 1)
    G8 = Point(6, 0)

    H1 = Point(7, 7)
    H2 = Point(7, 6)
    H3 = Point(7, 5)
    H4 = Point(7, 4)
    H5 = Point(7, 3)
    H6 = Point(7, 2)
    H7 = Point(7, 1)
    H8 = Point(7, 0)
