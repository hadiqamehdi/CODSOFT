import sys
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedWidget

class Calculator(QMainWindow):
    def __init__(self):
        super(Calculator, self).__init__()
        loadUi("calculator.ui", self)
        self.result = 0  
        self.expression = ""
        
        self.zero.clicked.connect(self.number_clicked)
        self.one.clicked.connect(self.number_clicked)
        self.two.clicked.connect(self.number_clicked)
        self.three.clicked.connect(self.number_clicked)
        self.four.clicked.connect(self.number_clicked)
        self.five.clicked.connect(self.number_clicked)
        self.six.clicked.connect(self.number_clicked)
        self.seven.clicked.connect(self.number_clicked)
        self.eight.clicked.connect(self.number_clicked)
        self.nine.clicked.connect(self.number_clicked)
        self.plus.clicked.connect(self.number_clicked)
        self.minus.clicked.connect(self.number_clicked)
        self.divide.clicked.connect(self.number_clicked)
        self.multiply.clicked.connect(self.number_clicked)
        self.mod.clicked.connect(self.number_clicked)
        self.equalsto.clicked.connect(self.calculate_result)
        self.left.clicked.connect(self.number_clicked)
        self.right.clicked.connect(self.number_clicked)
        self.clear.clicked.connect(self.clear_text)

    def number_clicked(self):
        sender = self.sender()  
        self.expression += sender.text()  
        self.update_display() 

    def calculate_result(self):
        
        result = eval(self.expression)  
        self.expression = str(result)  
        self.update_display()
    def clear_text(self):
        self.expression = ""  # Clear the expression
        self.update_display()  # Update the display with an empty string

    def update_display(self):
        self.textEdit.setPlainText(self.expression)

app = QApplication(sys.argv)
cal = Calculator()
widget = QStackedWidget()
widget.addWidget(cal)
widget.setFixedHeight(514)
widget.setFixedWidth(432)
widget.show()
try:
    sys.exit(app.exec_())
except:
    print("Exiting")
