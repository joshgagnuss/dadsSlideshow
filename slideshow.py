import os
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QLabel

app = QApplication([])
app.setWindowFlags(Qt.FramelessWindowHint)
app.setOverrideCursor(Qt.BlankCursor)

folder = 'pictures'
images = [os.path.join(folder, i) for i in os.listdir(folder)]

label = QLabel()
label.setGeometry(app.desktop().screenGeometry())
label.setScaledContents(True)

def update_image():
    if images:
        label.setPixmap(QPixmap(images.pop(0)))
    else:
        images = [os.path.join(folder, i) for i in os.listdir(folder)]

timer = QTimer()
timer.timeout.connect(update_image)
timer.start(3000)

label.showFullScreen()
app.exec_()