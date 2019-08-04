from accumulate import *
from exam import *
from append import *
from review import *

from PyQt5.QtWidgets import QApplication,QMainWindow,QDialog
import sys


class ParentWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.main_ui = Ui_Accumulate()
        self.main_ui.setupUi(self)


class ExamWindow(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.exam = Ui_Examination()
        self.exam.setupUi(self)
        self.exam.setupfunc()

class AppendWindow(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.app = Ui_Append()
        self.app.setupUi(self)
        self.app.setupfunction()


class ReviewWindow(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.review = Ui_Dialog()
        self.review.setupUi(self)
        self.review.setupfunc()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    accu = ParentWindow()
    exam = ExamWindow()
    appd = AppendWindow()

    revw = ReviewWindow()
    accu.show()

    btnExm = accu.main_ui.btnExam
    btnExm.clicked.connect(exam.show)

    btnApd = accu.main_ui.btnAppend
    btnApd.clicked.connect(appd.show)

    btnRew = accu.main_ui.btnReview
    btnRew.clicked.connect(revw.show)

    sys.exit(app.exec_())
