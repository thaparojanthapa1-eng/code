import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QVBoxLayout)
from PyQt5.QtGui import QFont

from PyQt5.QtCore import QTimer, QTime, Qt

class Digital_clock(QWidget):
    def __init__(self):
        super().__init__()
        self.time_label=QLabel(self)
        self.timer=QTimer(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("DIgital Clock")
        self.setGeometry(600, 400, 300, 100)

        vbox=QVBoxLayout()
        vbox.addWidget(self.time_label)
        self.setLayout(vbox)

        self.time_label.setAlignment(Qt.AlignCenter)

        font = QFont('Courier', 150, QFont.Bold)  
        self.time_label.setFont(font)
        self.time_label.setStyleSheet

        self.timer.timeout.connect(self.curr_time)
        self.timer.start(1000)

        self.curr_time()

    def curr_time(self):
        time=QTime.currentTime().toString("hh:mm:ss")
        self.time_label.setText(time)

if __name__=="__main__":
    app=QApplication(sys.argv)
    clock=Digital_clock()
    clock.show()
    sys.exit(app.exec_())