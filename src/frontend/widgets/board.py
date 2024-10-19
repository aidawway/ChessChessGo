from typing import List

from PyQt5.QtCore import QRectF, Qt, QObject
from PyQt5.QtGui import QTransform, QBrush, QPainter, QPixmap, QColor
from PyQt5.QtWidgets import QWidget, QGraphicsScene, QGraphicsView, QGraphicsRectItem, QHBoxLayout, QLabel, QPushButton, \
    QGraphicsWidget

from src.frontend.chess_notation import ChessPieces
from src.frontend.gonefishing import Stockfish, Ply
from src.frontend.models.fynn import FynnIter
from src.frontend.widgets.piece import Piece

STOCKFISH = Stockfish("/opt/homebrew/Cellar/stockfish/17/bin/stockfish")

class ChessSquare(QGraphicsRectItem):
    def __init__(self, x, y, height, color, scene):
        super().__init__(x, y, x + height, y + height)
        self.highlighted = False
        self.button = QPushButton()
        self.button.setGeometry(x, y, x + height, y + height)
        self.button.setStyleSheet("QPushButton { background-color: transparent; border: 0px }")
        self.brush = QBrush(color)
        self.selected_brush = QBrush(QColor(Qt.red))
        self.highlight_brush = self.selected_brush
        self.setBrush(self.brush)
        self.selected = False
        scene.addWidget(self.button)
        self.button.clicked.connect(self.toggle_selected)

    def toggle_selected(self):
        self.selected = not self.selected
        if self.selected:
            self.setBrush(self.selected_brush)
        else:
            self.setBrush(self.highlight_brush if self.highlighted else self.brush)

    def highlight(self, brush=None):
        self.highlight_brush = brush if brush else self.highlight_brush
        self.setBrush(self.highlight_brush)
        self.highlighted = True

class ChessBoard(QWidget):

    def __init__(self, width: int, parent=None):
        super().__init__(parent)
        self.fynn = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
        color1 = QColor(Qt.cyan)
        color2 = QColor(Qt.blue)

        if color1.black() < color2.black():
            team1 = color1
            team2 = color2
        else:
            team2 = color1
            team1 = color2

        width -= width % 8
        square_width = int(width / 8)
        FynnIter.height = square_width
        self.square_width = int(square_width)
        scene = QGraphicsScene(0, 0, width + 10, width + 10)
        self.scene = scene
        self.setFixedSize(width, width)
        self.board: List[List[ChessSquare]] = list()
        self.selected_piece = None

        for col in range(0, 8):
            row = list()
            self.board.append(row)
            for r in range(0, 8):
                xpos = square_width * col
                ypos = square_width * r
                square = ChessSquare(xpos, ypos, square_width, team2 if (col + r) % 2 == 0 else team1, self.scene)
                scene.addItem(square)
                row.append(square)
            row.reverse()

        view = QGraphicsView(scene, self)
        # view.setRenderHint(QPainter.Antialiasing)
        view.show()
        self.view = view
        # self.view.fitInView(0, 0, width, width)
        self.setLayout(QHBoxLayout())
        self.layout().addWidget(view)

    def add_piece(self, piece,  row, col):
        # p = Piece(style, name, self.square_width, self.scene)
        pixmap_item = self.scene.addPixmap(piece.pixmap)

        xpos = int(self.square_width * col + (self.square_width - piece.pixmap.width()) / 2)
        ypos = row * self.square_width
        pixmap_item.setPos(xpos, ypos)
        # pixmap_item.show()
        self.scene.update()


    def set_state(self, fynn: str):
        self.fynn = fynn
        for (piece, row, col) in FynnIter(fynn):
            self.add_piece(piece, 7 - row,  col - 1)

    def highlight_sq(self, x: int, y: int, brush=None):
        assert 0 <= x < 8
        assert 0 <= y < 8
        self.board[x][y].highlight(brush)

    def highlight_move(self, move: str, brush: QBrush | None = None):
        def rank2row(r: str):
            return ord(r) - ord('a')
        assert len(move) == 4
        print(brush.color().name())
        self.highlight_sq(rank2row(move[0]), int(move[1]) - 1, brush)
        self.highlight_sq(rank2row(move[2]), int(move[3]) - 1, brush)

    def setup(self):
        self.set_state("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")
        moves: [Ply] = STOCKFISH.get_top_moves(num_top_moves=3)

        colors = [QBrush(QColor(Qt.yellow)), QBrush(QColor(Qt.darkYellow)), QBrush(QColor(Qt.magenta))]

        for (move, color) in zip(moves, colors):
            self.highlight_move(move.move, color)

