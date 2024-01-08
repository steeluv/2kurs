from PyQt6.QtWidgets import QMainWindow, QApplication, QWidget, QLabel, QLineEdit, QPushButton, QGridLayout,\
    QLCDNumber
import sys

class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(400,400,200,380)
        self.setWindowTitle("Calculator")
        self.res = QLabel(self)
        self.res.setText(' Результат:')
        self.res.move(1, 20)
        self.first = QLineEdit()
        self.first.setStyleSheet("background-color: ivory ")
        self.second = QLineEdit()
        self.second.setStyleSheet("background-color: ivory ")
        self.ce = QLineEdit()
        self.grid = QGridLayout()
        self.container = QWidget()
        self.container.setStyleSheet("background-color: old lace ")
        self.container.setLayout(self.grid)
        self.setCentralWidget(self.container)

        self.buttonplus = QPushButton('＋', self)
        self.buttonplus.clicked.connect(self.plusclicked)
        self.buttonplus.setStyleSheet("background-color: linen")

        self.button_ce = QPushButton('CE', self)
        self.button_ce.clicked.connect(self.ce_clicked)
        self.button_ce.setStyleSheet("background-color: plum ")

        self.buttonpercent = QPushButton('％', self)
        self.buttonpercent.clicked.connect(self.percentclicked)
        self.buttonpercent.setStyleSheet("background-color: powderblue ")

        self.buttonstep = QPushButton('x^', self)
        self.buttonstep.clicked.connect(self.stepclicked)
        self.buttonstep.setStyleSheet("background-color: lightcyan ")

        self.buttonfractional = QPushButton('⅟', self)
        self.buttonfractional.clicked.connect(self.fractionalclicked)
        self.buttonfractional.setStyleSheet("background-color: lightgray ")

        self.buttonminus = QPushButton('﹣', self)
        self.buttonminus.clicked.connect(self.minusclicked)
        self.buttonminus.setStyleSheet("background-color: mistyrose")

        self.buttondel = QPushButton('÷', self)
        self.buttondel.clicked.connect(self.delclicked)
        self.buttondel.setStyleSheet("background-color: beige ")

        self.buttonmult = QPushButton('×', self)
        self.buttonmult.clicked.connect(self.multclicked)
        self.buttonmult.setStyleSheet("background-color: lightpink ")

        self.button_2 = QPushButton('x²', self)
        self.button_2.clicked.connect(self.clicked_2)
        self.button_2.setStyleSheet("background-color: thistle ")

        self.buttonx = QPushButton('☣', self)
        self.buttonx.clicked.connect(self.x_clicked)
        self.buttonx.setStyleSheet("background-color: mintcream ")

        self.result = QLCDNumber(8)
        self.result.display(0)
        self.result.setStyleSheet("background-color: deeppink ")
        self.result.setMaximumSize(900,30)

        self.grid.addWidget(self.first,2,1)
        self.grid.addWidget(self.second,2,2)
        self.grid.addWidget(self.result,1,1)
        self.grid.addWidget(self.button_ce, 5, 3)
        self.grid.addWidget(self.buttonminus,3, 2)
        self.grid.addWidget(self.buttondel, 4, 1)
        self.grid.addWidget(self.buttonmult, 3,3)
        self.grid.addWidget(self.buttonstep, 4, 2)
        self.grid.addWidget(self.buttonpercent, 4, 3)
        self.grid.addWidget(self.buttonplus, 3, 1)
        self.grid.addWidget(self.buttonfractional, 5, 1)
        self.grid.addWidget(self.button_2, 5, 2)
        self.grid.addWidget(self.buttonx, 1, 2)

    def plusclicked(self):
        firsttext = float(self.first.text())
        secondtext = float(self.second.text())
        self.result.display(firsttext + secondtext)

    def x_clicked(self):
        self.result.display('LOUE U')

    def clicked_2(self):
        firstText = float(self.first.text())
        self.result.display(firstText * firstText)

    def fractionalclicked(self):
        firsttext = float(self.first.text())
        self.result.display(1 / firsttext)

    def ce_clicked(self):
        self.result.display(0)

    def minusclicked(self):
        firsttext = float(self.first.text())
        secondtext = float(self.second.text())
        self.result.display(firsttext - secondtext)

    def delclicked(self):
        firsttext = float(self.first.text())
        secondtext = float(self.second.text())
        self.result.display(firsttext / secondtext)

    def multclicked(self):
        firsttext = float(self.first.text())
        secondtext = float(self.second.text())
        self.result.display(firsttext * secondtext)

    def stepclicked(self):
        firsttext = float(self.first.text())
        secondtext = float(self.second.text())
        self.result.display(firsttext ** secondtext)

    def percentclicked(self):
        firsttext = float(self.first.text())
        secondtext = float(self.second.text())
        self.result.display((firsttext * 100)/secondtext)






if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Calculator()
    ex.show()
    sys.exit(app.exec())