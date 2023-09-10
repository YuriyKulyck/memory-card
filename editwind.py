from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QLabel

import base

def editwindow():
    window = QDialog()
    window.resize(380, 380)
    editbut = QPushButton("Редагувати.")

    h1 = QHBoxLayout()
    questLbl = QLabel("Питання: ")
    queedit = QLineEdit()

    mainLine = QVBoxLayout()

    h1.addWidget(questLbl)
    h1.addWidget(queedit)
    mainLine.addLayout(h1)

    h2 = QHBoxLayout()
    rightanswerLbl = QLabel("Правильна відповідь")
    queedit2 = QLineEdit()

    h2.addWidget(rightanswerLbl)
    h2.addWidget(queedit2)
    mainLine.addLayout(h2)

    h3 = QHBoxLayout()
    unrightanswerLbl1 = QLabel("неправильне1")
    queedit3 = QLineEdit()

    h3.addWidget(unrightanswerLbl1)
    h3.addWidget(queedit3)
    mainLine.addLayout(h3)

    h4 = QHBoxLayout()
    unrightanswerLbl2 = QLabel("неправильне2")
    queedit4 = QLineEdit()

    h4.addWidget(unrightanswerLbl2)
    h4.addWidget(queedit4)
    mainLine.addLayout(h4)

    h5 = QHBoxLayout()
    unrightanswerLbl3 = QLabel("неправильне3")
    queedit5 = QLineEdit()

    h5.addWidget(unrightanswerLbl3)
    h5.addWidget(queedit5)
    mainLine.addLayout(h5)

    def balalayka():
        base.quest[base.currecyque] = {
            "питання": queedit.text(),
            "правильна відповідь": queedit2.text(),
            "неправильне1": queedit3.text(),
            "неправильне2": queedit4.text(),
            "неправильне3": queedit5.text(),
        }
        window.close()

    mainLine.addWidget(editbut)
    editbut.clicked.connect(balalayka)

    window.setLayout(mainLine)
    window.show()
    window.exec()