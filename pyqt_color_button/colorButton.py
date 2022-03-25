from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QPushButton


class ColorButton(QPushButton):
    colorChanged = pyqtSignal(QColor)

    def __init__(self, size=20, color='white'):
        super().__init__()
        self.__color = QColor(0, 0, 0)
        self.__initUi(size, color)

    def __initUi(self, size, color):
        self.setFixedSize(size, size)
        self.setStyleSheet('QPushButton { border-width:1px; border-radius:' + str(size//2) + '; '
                           + 'background-color:' + color + '; }')

    def setColor(self, rgb):
        if isinstance(rgb, tuple):
            r = int(rgb[0])
            g = int(rgb[1])
            b = int(rgb[2])
            self.__color = QColor(r, g, b)
        elif isinstance(rgb, QColor):
            self.__color = rgb
        self.setStyleSheet(self.styleSheet()[:-1] + 'background:' + self.__color.name() + ';}')
        self.colorChanged.emit(self.__color)

    def getColor(self):
        return self.__color