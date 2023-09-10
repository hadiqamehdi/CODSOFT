import sys
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedWidget

class todo(QMainWindow):
    def __init__(self):
        super(todo, self).__init__()
        self.text=''
        loadUi("todo.ui", self)
        self.add.clicked.connect(self.data)
        self.clr.clicked.connect(self.clrr)
        self.dell.clicked.connect(self.dl)
    def data(self):
        self.text = self.input.text()
        self.lst.addItem(self.text)
        self.input.setText('')
    def clrr(self):
        self.lst.clear()
    def dl(self):
        a=self.lst.currentRow()
        self.lst.takeItem(a)
            
app = QApplication(sys.argv)
cal = todo()
widget = QStackedWidget()
widget.addWidget(cal)
widget.setFixedHeight(571)
widget.setFixedWidth(521)
widget.show()
try:
    sys.exit(app.exec_())
except:
    print("Exiting")
