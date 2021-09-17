import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from qt import Ui_MainWindow
import calculation


def resource_path(relative):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative)
    else:
        return os.path.join(os.path.abspath("."), relative)


class StartProg(QtWidgets.QMainWindow):
    def __init__(self):
        super(StartProg, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.add_functions()



    def add_functions(self):
        self.ui.calc.clicked.connect(self.results)
        self.setWindowTitle('Центр касательной окружности 0.1')
        self.setWindowIcon(QIcon(resource_path('icon_4.png')))
        # self.tray_i

    # self.setWindowIcon(QtGui.QIcon(resource_path('runcubit_gui.ico')))
    # self.tray_icon.setIcon(QtGui.QIcon(resource_path('runcubit_gui.ico')))

    def results(self):
        # line 1 points coordinates
        y10 = float(self.ui.line1_y1.text())
        z10 = float(self.ui.line1_z1.text())
        y11 = float(self.ui.line1_y2.text())
        z11 = float(self.ui.line1_z2.text())

        # line 2 points coordinates
        y20 = float(self.ui.line2_y1.text())
        z20 = float(self.ui.line2_z1.text())
        y21 = float(self.ui.line2_y2.text())
        z21 = float(self.ui.line2_z2.text())

        # line 3 points coordinates
        y30 = float(self.ui.line3_y1.text())
        z30 = float(self.ui.line3_z1.text())
        y31 = float(self.ui.line3_y2.text())
        z31 = float(self.ui.line3_z2.text())

        # lines parameters
        Y1, a1, b1 = calculation.line_eq(y10, z10, y11, z11)
        Y2, a2, b2 = calculation.line_eq(y20, z20, y21, z21)
        Y3, a3, b3 = calculation.line_eq(y30, z30, y31, z31)

        # cross_point Y1_Y2
        x_a, y_a = calculation.cross_lines(a1, a2, b1, b2)

        # cross_point Y1_Y3
        x_b, y_b = calculation.cross_lines(a1, a3, b1, b3)

        # cross_point Y2_Y3
        x_c, y_c = calculation.cross_lines(a2, a3, b2, b3)

        # AB, AC, BC lengths
        a_b = calculation.line_length(x_a, y_a, x_b, y_b)
        a_c = calculation.line_length(x_a, y_a, x_c, y_c)
        b_c = calculation.line_length(x_b, y_b, x_c, y_c)

        # F-point coordinates on AC line
        x_f = (x_a + (a_b / b_c) * x_c) / (1 + (a_b / b_c))
        y_f = (y_a + (a_b / b_c) * y_c) / (1 + (a_b / b_c))

        # Bisector 1
        Y_b1, a_b1, b_b1 = calculation.line_eq(x_b, y_b, x_f, y_f)

        # Create point E on line1
        x_e, y_e = (0, a1 * 0 + b1)

        # AE lengths
        a_e = calculation.line_length(x_a, y_a, x_e, y_e)

        # K-point coordinates on EC line
        x_k = (x_e + (a_e / a_c) * x_c) / (1 + (a_e / a_c))
        y_k = (y_e + (a_e / a_c) * y_c) / (1 + (a_e / a_c))

        # Bisector 2
        Y_b2, a_b2, b_b2 = calculation.line_eq(x_a, y_a, x_k, y_k)

        # cross_point of bisectors
        x_cross_b, y_cross_b = calculation.cross_lines(a_b1, a_b2, b_b1, b_b2)

        # circle radius
        r = abs(((x_a - x_c) * (y_cross_b - y_c) - (y_a - y_c) * (x_cross_b - x_c)) / calculation.line_length(x_a, y_a, x_c, y_c))

        # self.ui.out_txt.setText(str(round(r, 5)))
        # self.ui.out_test.setText(str(round(r, 5)))
        self.ui.out_Y.setText(str(round(x_cross_b, 8)))
        self.ui.out_Z.setText(str(round(y_cross_b, 8)))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = StartProg()
    ui.show()
    sys.exit(app.exec_())
