from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QPushButton

from src.frontend.chess_notation import ChessPieces



class Piece:
    root = "assets"

    # scale_map = {
    #     "black-pawn": 100
    # }

    def __init__(self, style, name: ChessPieces, height, parent=None):
        self.style = style
        self.name = name
        self.height = height


        self.pixmap = QPixmap(f"{Piece.root}/pieces/{style}/{name.value.lower()}.png")
        # self.pixmap = self.pixmap.scaledToHeight(Piece.scale_map.get(f"{style}-{name}"))
        self.pixmap = self.pixmap.scaledToHeight(height)



