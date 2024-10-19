from PyQt5.QtWidgets import QWidget, QHBoxLayout

from src.frontend.widgets.board import ChessBoard


class ChessGame(QWidget):

    def __init__(self, parent = None):
        super().__init__(parent)
        board_size = 800
        self.setLayout(QHBoxLayout())

        self.board = ChessBoard(width=board_size, parent=self)
        self.layout().addWidget(self.board)
        self.setMinimumSize(board_size + 20, board_size + 20)

        self.board.setup()
