from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QPushButton


class ColorButton(QPushButton):
    colorChanged = pyqtSignal(QColor)

    def __init__(self, size=20, r=255, g=255, b=255):
        super().__init__()
        self.__color = QColor(r, g, b)
        self.__initUi(size)

    def __initUi(self, size):
        self.setFixedSize(size, size)
        self.setStyleSheet(f'''
                            QPushButton 
                            {{
                            border-width:1px; 
                            border-radius: {str(size//2)};
                            background-color: {self.__color.name()}; 
                            }}
                            '''
                            )

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