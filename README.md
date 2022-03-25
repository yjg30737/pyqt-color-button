# pyqt-color-button
Circle-shaped color button

## Requirements
* PyQt5 >= 5.8

## Setup
```pip3 install git+https://github.com/yjg30737/pyqt-color-button.git --upgrade```

## Class and Method Overview

You can make a new instance of ColorButton like below.

`btn = ColorButton(size=30, color='red')`

`btn = ColorButton(size=40, color='#000000')`

Size argument is value(px) of border-radius, color is value of background-color.

`setColor(rgb)` let you set the color after you made a new instance. rgb is the list of r, g, b. 
Element's type of list can be str or int.

`getColor()` let you get the current color of the box.

There is `colorChanged(QColor)` signal to detect the color of box changed.

## Preview

![image](https://user-images.githubusercontent.com/55078043/160053919-29dc6e08-4709-4d5e-8f6d-74a20f365357.png)




