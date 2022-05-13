# pyqt-color-button
Circle-shaped color button

## Requirements
* PyQt5 >= 5.8

## Setup
`python -m pip install pyqt-color-button`

## Class and Method Overview

Constructor - `ColorButton(size=20, r=255, g=255, b=255)`

You can make a new instance of ColorButton like below.

`btn = ColorButton(size=40, r=0, g=0, b=0)`

Size argument is value(px) of border-radius, color is value of background-color.

With `setColor(rgb: tuple)` or `setColor(rgb: QColor)`, you can set the color after you made a new instance.

`getColor()` let you get the current color of the box.

There is `colorChanged(QColor)` signal to detect the color of box changed.

## Preview

![image](https://user-images.githubusercontent.com/55078043/160053919-29dc6e08-4709-4d5e-8f6d-74a20f365357.png)




