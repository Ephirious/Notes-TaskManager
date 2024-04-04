from PyQt6 import QtWidgets, QtGui, QtCore

class TextWindow(QtWidgets.QTextEdit):
    def __init__(self):
        super().__init__()
        #self.setFontPointSize(20) 
        self.setPlaceholderText("Input your text")
        self.textCursor().charFormat().setFontUnderline(True)


class ComboBoxTextSize(QtWidgets.QComboBox):
    def __init__(self):
        super().__init__()
        self.addItems(str(x) for x in range(20, 41))
        self.scroll = QtWidgets.QScrollArea()


class SettingsPanel(QtWidgets.QHBoxLayout):
    def __init__(self):
        super().__init__()
        self.cmbTextSize = ComboBoxTextSize()
        self.buttonToBoldText = QtWidgets.QPushButton("Bold")
        self.addWidget(self.cmbTextSize)
        self.addWidget(self.buttonToBoldText)



class TextEditor(QtWidgets.QBoxLayout):
    def __init__(self):
        super().__init__(self.Direction.TopToBottom)
        self.settingsPanel = SettingsPanel()
        self.textWindow = TextWindow()
        self.textSettingsPanel = QtWidgets.QHBoxLayout()
        self.settingsPanel.cmbTextSize.currentIndexChanged.connect(self.changeTextSize)
        self.settingsPanel.buttonToBoldText.clicked.connect(self.doBoldText)
        self.addLayout(self.settingsPanel)
        self.addWidget(self.textWindow)

    def changeTextSize(self):
        charFormatFontSize = QtGui.QTextCharFormat(self.textWindow.currentCharFormat())
        charFormatFontSize.setFontPointSize(float(self.settingsPanel.cmbTextSize.currentText()))
        self.textWindow.setCurrentCharFormat(charFormatFontSize)
        '''if not self.textWindow.textCursor().hasSelection():
            self.textWindow.setFontPointSize(int(self.settingsPanel.cmbTextSize.currentText()))
        else:
            for _ in range(self.textWindow.textCursor().selectionStart(), self.textWindow.textCursor().selectionEnd()):
                self.textWindow.textCursor().movePosition(QtGui.QTextCursor.MoveOperation.Right, QtGui.QTextCursor.MoveMode.MoveAnchor)
                self.textWindow.setFontPointSize(int(self.settingsPanel.cmbTextSize.currentText()))'''

    def doBoldText(self):
        charFormatBold = QtGui.QTextCharFormat(self.textWindow.currentCharFormat())
        charFormatNorm = QtGui.QTextCharFormat(self.textWindow.currentCharFormat())
        charFormatBold.setFontWeight(900)
        charFormatNorm.setFontWeight(400)
        if self.textWindow.textCursor().charFormat().fontWeight() == 400:
            self.textWindow.setCurrentCharFormat(charFormatBold)
        else:
            self.textWindow.setCurrentCharFormat(charFormatNorm)
        
                

class Window(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self, parent=None)
        self.textEditor = TextEditor()
        self.setLayout(self.textEditor)
    
    

if __name__ == "__main__":
    import sys
    application = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.show()
    application.exec()
    

