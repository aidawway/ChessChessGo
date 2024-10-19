from PyQt5.QtCore import QRectF, Qt, QObject
from PyQt5.QtGui import QTransform, QBrush, QPainter, QPixmap, QColor
from PyQt5.QtWidgets import QWidget, QGraphicsScene, QGraphicsView, QGraphicsRectItem, QHBoxLayout, QLabel, QPushButton, \
    QGraphicsWidget

from src.frontend.chess_notation import ChessPieces
from src.frontend.models.fynn import FynnIter
from src.frontend.widgets.piece import Piece


class ChessSquare(QGraphicsRectItem):
    def __init__(self, x, y, height, color, scene):
        super().__init__(x, y, x + height, y + height)
        self.button = QPushButton()
        self.button.setGeometry(x, y, x + height, y + height)
        self.button.setStyleSheet("QPushButton { background-color: transparent; border: 0px }")
        self.brush = QBrush(color)
        self.setBrush(self.brush)
        self.selected = False
        scene.addWidget(self.button)
        self.button.clicked.connect(self.toggle_selected)

    def toggle_selected(self):
        self.selected = not self.selected
        if self.selected:
            self.setBrush(QBrush(QColor(Qt.red)))
        else:
            self.setBrush(self.brush)

class ChessBoard(QWidget):

    def __init__(self, width: int, parent=None):
        super().__init__(parent)
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

        for col in range(0, 8):
            for row in range(0, 8):
                xpos = square_width * col
                ypos = square_width * row
                # square = QGraphicsRectItem(xpos, ypos, xpos + square_width, ypos + square_width)
                # square.setBrush(QBrush(team1 if (col + row) % 2 == 0 else team2))
                square = ChessSquare(xpos, ypos, square_width, team2 if (col + row) % 2 == 0 else team1, self.scene)
                # scene.addItem(square.square)
                scene.addItem(square)
                # scene.addWidget(square.button)
                # square.button.setText("Hiiiii")

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
        for (piece, row, col) in FynnIter(fynn):
            self.add_piece(piece, 7 - row,  col - 1)
    #
    def setup(self):
        # self.set_state("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")
        self.set_state("rnbqkbnr/pppppppp/8/8/8/P7/1PPPPPPP/RNBQKBNR w KQkq - 0 1")

