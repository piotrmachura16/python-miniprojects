from PyQt5.QtWidgets import *
app = QApplication([])
button = QPushButton('Click')


def on_button_clicked():
    global window
    alert = QMessageBox()
    alert.setText('You clicked the button!')
    alert.setWindowTitle('WOW!')
    alert.exec_()
    window.close()


button.clicked.connect(on_button_clicked)

window = QWidget()
layout = QVBoxLayout()
layout.addWidget(button)
window.setLayout(layout)
window.setMinimumSize(500, 200)
window.setWindowTitle('First Qt5 app!')

window.show()
app.exec_()
