from PyQt5.QtWidgets import *
import random
import base
import menuwind
import editwind

app = QApplication([])
app.setStyleSheet("""
    QWidget{
        
        background:qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,stop: 0 white, stop: 0.4 red,stop: 1 indigo);
    }
    QPushButton{
    border: 2px solid;
    border-color:qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,stop: 0 white, stop: 0.4 blue,stop: 1 violet);
        background:qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,stop: 0 white, stop: 0.4 yellow,stop: 1 violet);
    }
    QGroupBox{
        background: rgb(113,0,35);
        background:qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,stop: 0 white, stop: 0.4 gray,stop: 1 green);
    }
    QRadioButton{
        background:qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,stop: 0 white, stop: 0.4 gold,stop: 1 blue);
    }
    Qlabel{
        background:qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,stop: 0 white, stop: 0.4 pink,stop: 1 green);
    }
""")
window = QWidget()
window.resize(400 , 400)

mainline = QVBoxLayout()

menubut = QPushButton('меню')
editbut = QPushButton('Редагувати.')
restbtn = QPushButton('Відпочити')
timespn = QSpinBox()
timlb = QLabel('хвилин')


firstline = QHBoxLayout()
firstline.addWidget(menubut)
firstline.addWidget(restbtn)
firstline.addWidget(timespn)
firstline.addWidget(timlb)

mainline.addLayout(firstline)
quetext = QLabel('скільки кг поносу у серГЕЯ ?')
mainline.addWidget(quetext)

answersgroup = QGroupBox('варіанти відповідей')
answer1 = QRadioButton('8тонн')
answer2 = QRadioButton('10тонн')
answer3 = QRadioButton('7тонн')
answer4 = QRadioButton('14тонн')

ansbut = QPushButton('відповісти')
nextbut = QPushButton('наступне питання')
answers = [answer1, answer2, answer3, answer4]


answerline = QVBoxLayout()
answerline.addWidget(answer1)
answerline.addWidget(answer2)
answerline.addWidget(answer3)
answerline.addWidget(answer4)

result = QLabel("Результат: Гороховий суп смердить гірше, аніж підпашка")
answerline.addWidget(result)
result.hide()

answersgroup.setLayout(answerline)
mainline.addWidget(answersgroup)
mainline.addWidget(ansbut)
mainline.addWidget(nextbut)
mainline.addWidget(editbut)
nextbut.hide()

def setanswer():
    random.shuffle(answers)
    quetext.setText(base.quest[base.currencyque]["питання"])
    answers[0].setText(base.quest[base.currencyque]["правильна відповідь"])
    answers[1].setText(base.quest[base.currencyque]["неправильне1"])
    answers[2].setText(base.quest[base.currencyque]["неправильне2"])
    answers[3].setText(base.quest[base.currencyque]["неправильне3"])

def showquestion():
    random.shuffle(answers)
    base.currencyque += 1
    quetext.setText(base.quest[base.currencyque]["питання"])
    answers[0].setText(base.quest[base.currencyque]["правильна відповідь"])
    answers[1].setText(base.quest[base.currencyque]["неправильне1"])
    answers[2].setText(base.quest[base.currencyque]["неправильне2"])
    answers[3].setText(base.quest[base.currencyque]["неправильне3"])
    for i in range(4):
        answers[i].show()

def editfunc():
    window.hide()
    editwind.editwindow()
    window.show()

    setanswer()

setanswer()
def showResult():
    for i in range(4):
        answers[i].hide()
    result.show()
    ansbut.hide()
    nextbut.show()
    if answers[0].isChecked():
        result.setText("Гороховий суп смердить гірше, аніж підпашка")
    else:
        result.setText("Яке пояснення поноса?")




ansbut.clicked.connect(showResult)
nextbut.clicked.connect(showquestion)
menubut.clicked.connect(menuwind.menuWind)
editbut.clicked.connect(editfunc)

window.setLayout(mainline)
window.show()
app.exec()