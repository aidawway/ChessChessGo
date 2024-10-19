import os
import sys

from PyQt5.QtCore import QRectF
from PyQt5.QtGui import QTransform
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QScrollArea, QPushButton, QTextEdit, \
    QMainWindow, QDockWidget, QToolBar, QStackedWidget, QVBoxLayout, QSizePolicy, QGraphicsView, QGraphicsScene

from src.frontend.view.game import ChessGame
from src.frontend.widgets.board import ChessBoard


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.stacked_widget = QStackedWidget()
        self.setWindowTitle("ChessChessGo")
        self.toolbar = QToolBar()
        self.page_buttons = []
        home_button = QPushButton()
        home_button.setText("Game")
        # home_button.clicked.connect(self.homepage)
        self.page_buttons.append(home_button)

        self.game = ChessGame(self.stacked_widget)
        self.layout().addWidget(self.game)
        self.setMinimumSize(self.game.size())







if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    # window()
    app.exec()
