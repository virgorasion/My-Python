from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QGridLayout, QPushButton

class Window2(QWidget):
    def __init__(self) -> None:
        QWidget.__init__(self)
        self.setWindowTitle("Basic Grid 2")
        self.button = QPushButton("Close",self)
        self.button.clicked.connect(self.close)
        layout = QGridLayout(self)
        layout.addWidget(QPushButton("Cls"),0,0,1,1)
        layout.addWidget(QPushButton("Bck"),0,1,1,1)
        layout.addWidget(self.button,0,3,1,1)
        layout.addWidget(QPushButton("7"),1,0,1,1)
        layout.addWidget(QPushButton("8"),1,1,1,1)
        layout.addWidget(QPushButton("9"),1,2,1,1)
        layout.addWidget(QPushButton("/"),1,3,1,1)
        layout.addWidget(QPushButton("4"),2,0,1,1)
        layout.addWidget(QPushButton("5"),2,1,1,1)
        layout.addWidget(QPushButton("6"),2,2,1,1)
        layout.addWidget(QPushButton("*"),2,3,1,1)
        layout.addWidget(QPushButton("1"),3,0,1,1)
        layout.addWidget(QPushButton("2"),3,1,1,1)
        layout.addWidget(QPushButton("3"),3,2,1,1)
        layout.addWidget(QPushButton("-"),3,3,1,1)
        layout.addWidget(QPushButton("0"),4,0,1,1)
        layout.addWidget(QPushButton("."),4,1,1,1)
        layout.addWidget(QPushButton("="),4,2,1,1)
        layout.addWidget(QPushButton("+"),4,3,1,1)
    def close(self):
        self.exit()
        
class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.button = QPushButton('i-3', self)
        self.button.clicked.connect(self.handleButton)
        layout = QGridLayout(self)
        layout.addWidget(self.button,0,0,1,3)
        layout.addWidget(QPushButton("4, 7"),1,0,2,1)
        layout.addWidget(QPushButton("4"),1,1,1,1)
        layout.addWidget(QPushButton("5"),1,2,1,1)
        layout.addWidget(QPushButton("6"),2,1,1,1)
        layout.addWidget(QPushButton("7"),2,2,1,1)

    def handleButton(self):
        self.window2 = Window2()
        self.window2.show()
        self.hide()

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
    