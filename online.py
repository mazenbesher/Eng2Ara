#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys, os
import pyperclip
from main import load_letters, eng2ara, LETTERS_TABLE
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, QPushButton,
                             QTextEdit, QGridLayout, QApplication)


class Example(QWidget):
    outputEdit = None
    letters = None

    def __init__(self):
        super().__init__()
        self.initUI()

    def textChanged(self, text):
        self.outputEdit.setText(eng2ara(text, self.letters))

    def copyClicked(self):
        pyperclip.copy(self.outputEdit.text())

    def openTableClickde(self):
        os.startfile(LETTERS_TABLE)

    def initUI(self):
        self.letters = load_letters()

        input = QLabel('Input')
        output = QLabel('Output')
        copyBtn = QPushButton('Copy', self)
        lettersBtn = QPushButton('Open Letters Table', self)

        inputEdit = QLineEdit()
        self.outputEdit = QLineEdit()

        inputEdit.textChanged.connect(self.textChanged)
        copyBtn.clicked.connect(self.copyClicked)
        lettersBtn.clicked.connect(self.openTableClickde)

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(input, 1, 0)
        grid.addWidget(inputEdit, 1, 1)

        grid.addWidget(output, 2, 0)
        grid.addWidget(self.outputEdit, 2, 1)

        grid.addWidget(copyBtn, 3, 0)
        grid.addWidget(lettersBtn, 3, 1)

        self.setLayout(grid)

        self.setGeometry(300, 300, 350, 30)
        self.setWindowTitle('Online')
        self.show()

        inputEdit.setFocus()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())