import sys
import os
import random
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedWidget

class GAME(QMainWindow):
    def __init__(self):
        super(GAME, self).__init__()
        loadUi("GAME.ui", self)
        self.player = 0
        self.text = ''
        self.computer_choice = random.randint(0, 2)  # Renamed the variable
        self.dis = ''
        self.enter.clicked.connect(self.computer_num)
        self.tryagain.clicked.connect(self.clearr)
        self.quit.clicked.connect(self.quitt)
    
    def user(self):
        self.text = self.input.toPlainText()
        if self.text=='rock':
            self.player=0
        if self.text=='paper':
            self.player=1
        if self.text=='scissor':
            self.player=2
    def quitt(self):
        tex= eval(self.scorep.text())
        tex2= eval(self.scorec.text())
        if tex>=tex2:
            self.dis="       YOU WON   "
            self.result.setText(self.dis)
        if tex ==tex2:
            self.dis="       Game Over   "
            self.result.setText(self.dis)
            
        else:
            self.dis="       COMPUTER WON   "
            self.result.setText(self.dis)
    
        
    def games(self):
        self.user()
        if self.player== 1 and self.computer_choice ==0:
            self.scorep.setText('1')
            self.scorec.setText('0')
        if self.player== 1 and self.computer_choice ==1:
            self.scorep.setText('0')
            self.scorec.setText('0')
        if self.player== 1 and self.computer_choice ==2:
            self.scorep.setText('0')
            self.scorec.setText('1')
        if self.player== 0 and self.computer_choice ==0:
            self.scorep.setText('0')
            self.scorec.setText('0')
        if self.player== 0 and self.computer_choice ==1:
            self.scorep.setText('0')
            self.scorec.setText('1')
        if self.player== 0 and self.computer_choice ==2:
            self.scorep.setText('1')
            self.scorec.setText('0')
        if self.player== 2 and self.computer_choice ==0:
            self.scorep.setText('0')
            self.scorec.setText('1')
        if self.player== 2 and self.computer_choice ==1:
            self.scorep.setText('1')
            self.scorec.setText('0')
        if self.player== 2 and self.computer_choice ==2:
            self.scorep.setText('0')
            self.scorec.setText('0')
    
    def show(self):
        self.user()
        
                
        if self.text.lower() == 'rock':
            image_path = os.path.abspath('rock.png')
            image_html = f'<img src="{image_path}" width="408" height="340" alt="Image">'
            cursor = self.textEdit.textCursor()
            cursor.insertHtml(image_html)
        if self.text.lower() == 'paper':
            image_path = os.path.abspath('papper.png')
            image_html = f'<img src="{image_path}" width="408" height="340" alt="Image">'
            cursor = self.textEdit.textCursor()
            cursor.insertHtml(image_html)
        if self.text.lower() == 'scissor':
            image_path = os.path.abspath('scissor.png')
            image_html = f'<img src="{image_path}" width="408" height="340" alt="Image">'
            cursor = self.textEdit.textCursor()
            cursor.insertHtml(image_html)
        # self.computer_num()

    def computer_num(self):  # Renamed the method
        self.show()
        self.games()
        
        if self.computer_choice == 0:
            image_path = os.path.abspath('compK.png')
            image_html = f'<img src="{image_path}" width="408" height="340" alt="Image">'
            cursor = self.textEdit_2.textCursor()
            cursor.insertHtml(image_html)
        if self.computer_choice == 1:
            image_path = os.path.abspath('compR.png')
            image_html = f'<img src="{image_path}" width="408" height="340" alt="Image">'
            cursor = self.textEdit_2.textCursor()
            cursor.insertHtml(image_html)
        if self.computer_choice == 2:
            image_path = os.path.abspath('compS.png')
            image_html = f'<img src="{image_path}" width="408" height="340" alt="Image">'
            cursor = self.textEdit_2.textCursor()
            cursor.insertHtml(image_html)
        self.res()
    def clearr(self):
        
        self.input.clear()
        self.textEdit.clear()
        self.textEdit_2.clear()
        self.result.clear()
        self.scorec.clear()
        self.scorep.clear()
    def update_display(self):
        self.result.setPlainText(self.dis)
    def res(self):
        
        tex= eval(self.scorep.text())
        tex2= eval(self.scorec.text())
        if tex<=tex2:
            self.dis="       COMPUTER WON   "
            
        if tex>=tex2:
            self.dis="          YOU WON   "
            
        if tex ==tex2:
            self.dis="           IT'S A TIE  "
            
        
        self.update_display()
    def update_display(self):
        self.result.setText(self.dis)
    def quitt(self):
        QApplication.quit()
app = QApplication(sys.argv)
cal = GAME()
cal.show()
widget = QStackedWidget()
widget.addWidget(cal)
widget.setFixedHeight(756)
widget.setFixedWidth(1095)
widget.show()
sys.exit(app.exec_())
