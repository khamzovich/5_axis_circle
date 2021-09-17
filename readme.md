# Circle center

Program defines coordinates of print head by three lines for printer calibration.

Desktop version is created with PyQt5.

Main window:

![image](https://github.com/khamzovich/axis5d_circle/raw/master/images/5_axis_circle_window.PNG)

Matplotlib diagram:

![image](https://github.com/khamzovich/axis5d_circle/raw/master/images/diagram.PNG)

Save Qt designer file to .py:

* pyuic5 qt.ui -o qt.py

Create app from script:

* pyinstaller -F main.pyw
* pyinstaller -F --icon=icon_4.ico main.pyw
