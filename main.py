# This is a sample Python script.
from PyQt5.QtCore import QRectF, Qt
from PyQt5.QtGui import QTransform, QBrush
from PyQt5.QtWidgets import QGraphicsScene, QGraphicsView, QGraphicsRectItem

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


import sys
from PyQt5.QtWidgets import QGraphicsScene, QGraphicsView, QApplication

app = QApplication(sys.argv)

# Defining a scene rect of 400x200, with it's origin at 0,0.
# If we don't set this on creation, we can set it later with .setSceneRect
width = 800
team1 = Qt.blue
team2 = Qt.cyan
width -= width % 8
square_width = width / 8
scene = QGraphicsScene(0, 0, width, width)

for col in range(0, 8):
    for row in range(0, 8):
        xpos = square_width * col
        ypos = square_width * row
        square = QGraphicsRectItem(xpos, ypos, xpos + square_width, ypos + square_width)
        square.setBrush(QBrush(team1 if (col + row) % 2 == 0 else team2))
        scene.addItem(square)

view = QGraphicsView(scene)
view.show()
app.exec_()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
