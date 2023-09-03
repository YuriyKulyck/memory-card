from PyQt5.QtWidgets import *

import base


def menuWind():
    window = QDialog()
    window.resize(350, 350)

    addbut = QPushButton("Добавити.")

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

    def addFunc():
        base.quest.append(
            {
            "питання": queedit.text(),
            "правильна відповідь": "",
            "неправильне1": "",
            "неправильне2": "",
            "неправильне3": "",
            }
        )

    mainLine.addWidget(addbut)
    addbut.clicked.connect(addFunc)

    window.setLayout(mainLine)
    window.show()
    window.exec()